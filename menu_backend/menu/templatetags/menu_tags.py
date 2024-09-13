from django import template
from ..models import MenuItem


register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = MenuItem.objects.filter(menu__name=menu_name).select_related('parent').prefetch_related('children')
    menu_tree = build_menu_tree(menu_items)
    mark_active(menu_tree, request.path)
    return {'menu_tree': menu_tree}

def build_menu_tree(menu_items):
    menu_dict = {item.id: item for item in menu_items}
    root_items = []

    for item in menu_items:
        if item.parent_id:
            parent = menu_dict[item.parent_id]
            if not hasattr(parent, 'children'):
                parent.children = []
            parent.children.append(item)
        else:
            root_items.append(item)

    return root_items

def mark_active(menu_items, current_path):
    for item in menu_items:
        item.active = (item.get_url() == current_path)
        if hasattr(item, 'children'):
            mark_active(item.children, current_path)
            if any(child.active for child in item.children):
                item.active = True
