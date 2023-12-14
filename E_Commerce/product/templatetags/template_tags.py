from django import template
from django.http import QueryDict
from django.utils.datastructures import MultiValueDict

register = template.Library()

filters = {}

@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    query = context['request'].GET.copy()
    for k, v in kwargs.items():
        query[k] = v
    global filters
    filters=MultiValueDict(query)
    # print("Query : ", query)
            
    return query.urlencode()

@register.simple_tag()
def checked_box(context):
    global filters
    filters = dict(filters)
    # print("Filters : ", filters)

    
    

