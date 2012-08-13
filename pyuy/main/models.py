from cms.models.pluginmodel import CMSPlugin
from django.db import models

class MenuObject(CMSPlugin):
    choices = (
        ('authenticated','User must be authenticated'),('always','Show always'),('not_authenticated','User must not be authenticate')
    )
    name = models.CharField(max_length=30)
    a_class = models.CharField(max_length=30, default="")
    a_id = models.CharField(max_length=30, default="")
    a_link = models.CharField(max_length=30)
    condition = models.CharField(max_length=100, choices=choices)

    def __unicode__(self):
        return self.name

    def copy_relations(self, oldinstance):
        self.sections = oldinstance.sections.all()
