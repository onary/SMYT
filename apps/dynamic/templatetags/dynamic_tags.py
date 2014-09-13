from datetime import date, datetime

from django import template
from django.utils.datastructures import SortedDict

register = template.Library()

@register.filter(name='sort')
def simple_sort(value):
    if isinstance(value, dict):
        new_dict = SortedDict()
        key_list = value.keys()
        key_list.sort()
        for key in key_list:
            new_dict[key] = value[key]
        return new_dict
    elif isinstance(value, list):
        new_list = list(value)
        new_list.sort()
        return new_list
    else:
        return value
    simple_sort.is_safe = True

@register.filter
def is_date(value):
    return type(value) == date

@register.filter
def getattr(d, key_name):
    return d[key_name]

@register.filter
def field_type(field):
    return field.field.__class__.__name__
