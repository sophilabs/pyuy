from django.conf import settings
from django import template
register = template.Library()

@register.simple_tag
def background_map_image(background, width, height):
    return "http://maps.google.com/maps/api/staticmap?center=%s,%s&zoom=15&size=%sx%s&maptype=roadmap&sensor=false" % \
        (background.latitude, background.longitude, width, height)

@register.simple_tag
def background_map_url(background):
    return "http://maps.google.com.uy/maps?ll=%s,%s" % \
           (background.latitude, background.longitude)

