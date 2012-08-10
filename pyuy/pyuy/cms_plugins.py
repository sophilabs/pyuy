from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from pyuy.models import MenuObject

class AddMenu(CMSPluginBase):
    model = MenuObject
    name = _("Add menu object")
    render_template = "add_menu.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(AddMenu)