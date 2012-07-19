from django.conf.urls import *


urlpatterns = patterns('pycon.views',
    url(r"^$", 'index'),
    url(r"^proposal_add/$", 'proposal_add'),
)
