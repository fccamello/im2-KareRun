from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, [])

@register.filter
def filter_sizes(inclusions, inclusion_type):
    sizes = []
    for inclusion in inclusions:
        if isinstance(inclusion, dict) and inclusion.get('inclusion') == inclusion_type and inclusion.get('size'):
            sizes.append(inclusion['size'])
    return sizes