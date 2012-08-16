from django.conf.urls import *

urlpatterns = patterns('main.views',

    url(r"^$", 'index', name="index"),
)

