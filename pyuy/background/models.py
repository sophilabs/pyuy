from django.db import models
from pyuy.settings import LANGUAGES

class Background(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    place = models.CharField(max_length=20)
    autor = models.CharField(max_length=30)
    language = models.CharField(max_length=2, choices=LANGUAGES)
    order = models.IntegerField(default=0)
    source = models.URLField()
    image = models.ImageField(upload_to="backgrounds")
    latitude = models.DecimalField(decimal_places=6, max_digits=8)
    longitude = models.DecimalField(decimal_places=6, max_digits=8)

    def __unicode__(self):
        return self.name