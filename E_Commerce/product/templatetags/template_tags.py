from django import template

register = template.Library()

filters = ''

@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    query = context['request'].GET.copy()
    for k, v in kwargs.items():
        query[k] = v
        filters = query
    print("Query : ", query)
            
    return query.urlencode()

# @register.simple_tag()
# def checked_box(context):
#     if context in filters['brandSelections']:
#         return True
    

