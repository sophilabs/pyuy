from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from models import MenuPlugin

class Menu(CMSPluginBase):
    model = MenuPlugin
    name = _("Menu")
    render_template = "menu.html"

    def render(self, context, instance, placeholder):
        if instance.url:
            link = instance.url
        elif instance.page:
            link = instance.page.get_absolute_url()
        else:
            link = ""
        user = context.get('user')
        show = instance.condition == 'B' or \
            (instance.condition == 'A' and user.is_authenticated()) or \
            (instance.condition == 'U' and not user.is_authenticated())
        context.update({
            'show': show,
            'title': instance.title,
            'link': link,
            'class': instance.css_class,
            'target':instance.target,
            'placeholder': placeholder,
            'object': instance
        })
        return context

plugin_pool.register_plugin(Menu)