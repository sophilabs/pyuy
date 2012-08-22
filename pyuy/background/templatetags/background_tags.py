from django.conf import settings
from django import template
from background.models import Background

register = template.Library()

@register.simple_tag(takes_context=True)
def backgrounds(context, tag):
    context['backgrounds'] = Background.objects.filter(language=context['request'].LANGUAGE_CODE, tag=tag).order_by('?')
    return ''

@register.simple_tag
def background_map_image(background, width, height):
    if background:
        return "http://maps.google.com/maps/api/staticmap?center=%s,%s&zoom=15&size=%sx%s&maptype=roadmap&sensor=false" % \
            (background.latitude, background.longitude, width, height)
    else:
        return "#"

@register.simple_tag
def background_map_url(background):
    if background:
        return "http://maps.google.com.uy/maps?ll=%s,%s" % \
            (background.latitude, background.longitude)
    else:
        return "#"

