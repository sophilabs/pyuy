from django.db import models

class Background(models.Model):

    name = models.CharField(max_length=30)
    source = models.URLField()
    image = models.ImageField(upload_to="images")
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    map_source = models.URLField(editable=False)

    def get_map_source(self):
        url_left = "http://maps.google.com/maps/api/staticmap?center="
        url_right = "&zoom=15&size=300x300&maptype=roadmap&sensor=false"
        url_middle = self.latitude+","+self.longitude
        url = url_left+url_middle+url_right
        return url

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-name"]