from cms.models.pluginmodel import CMSPlugin
from django.db import models

class Background(models.Model):

    name = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    source = models.URLField()
    image = models.ImageField(upload_to="images")
    latitude = models.DecimalField(decimal_places=6, max_digits=8)
    longitude = models.DecimalField(decimal_places=6, max_digits=8)
    googlemap_url = models.URLField(editable=False)

    def get_googlemap_url(self):
        url = "http://maps.google.com/maps/api/staticmap?center=%s,%s&zoom=15&size=200x200&maptype=roadmap&sensor=false" % (self.latitude, self.longitude)
        return url
    get_googlemap_url.alters_data = False

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-name"]

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
