from cms.models import CMSPlugin, Page
from django.db import models
from django.utils.translation import ugettext_lazy as _

class MenuPlugin(CMSPlugin):

    title = models.CharField(max_length=30)
    url = models.CharField(max_length=30, null=True, blank=True)
    page = models.ForeignKey(Page, verbose_name=_("page"), blank=True, null=True, help_text=_("A link to a page has priority over a text link."))
    target = models.CharField(_("target"), blank=True, max_length=100, choices=((
        ("", _("same window")),
        ("_blank", _("new window")),
        ("_parent", _("parent window")),
        ("_top", _("topmost frame")),
    )))
    css_class = models.CharField(max_length=30, null=True, blank=True)
    condition = models.CharField(max_length=1, choices=(
        ('A', _('User must be authenticated')),
        ('B', _('Show always')),
        ('U', _('User must not be authenticated'))
    ))

    def __unicode__(self):
        return self.title
