from django import template
from django.conf import settings
from django.templatetags.future import url

register = template.Library()

class ABSURLNode(template.Node):
    def __init__(self, base_node):
        self.base_node = base_node

    def render(self, context):
        return settings.BASE_URL + self.base_node.render(context)

@register.tag
def absurl(parser, token):
    return  ABSURLNode(url(parser, token))