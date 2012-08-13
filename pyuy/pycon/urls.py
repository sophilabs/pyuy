from django.conf.urls import *

urlpatterns = patterns('pycon.views',
    #url(r"^$", 'index'),
    url(r"^proposal_add/$", 'proposal_add', name='proposal_add'),
    url(r"^proposal_sent/$", 'proposal_sent', name='proposal_sent'),
)

