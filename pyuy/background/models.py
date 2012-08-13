from django.db import models

class Background(models.Model):
    name = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    source = models.URLField()
    image = models.ImageField(upload_to="backgrounds")
    latitude = models.DecimalField(decimal_places=6, max_digits=8)
    longitude = models.DecimalField(decimal_places=6, max_digits=8)

    def __unicode__(self):
        return self.name