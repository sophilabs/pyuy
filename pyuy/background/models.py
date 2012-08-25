from django.db import models
from pyuy.settings import LANGUAGES

class Background(models.Model):

    title = models.CharField(max_length=40)
    description = models.TextField()
    place = models.CharField(max_length=20)
    author = models.CharField(max_length=30, null=True, blank=True)
    language = models.CharField(max_length=2, choices=LANGUAGES)
    order = models.IntegerField(default=0)
    source = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to="backgrounds")
    latitude = models.DecimalField(decimal_places=6, max_digits=8)
    longitude = models.DecimalField(decimal_places=6, max_digits=8)
    tag = models.CharField(max_length=50)
    box_css_class = models.CharField(max_length=20, default='std-box')

    def __unicode__(self):
        return self.title