from django import template
import re

register = template.Library()

@register.simple_tag
def active(request, pattern):
    if re.search(pattern, request.path):
        return 'class="active"'
    else:
        return ''

@register.simple_tag
def url_active(request, url):
    pattern = '^%s' % url
    if re.search(pattern, request.path):
        return 'class="active"'
    else:
        return ''
