from django.conf.urls import *

urlpatterns = patterns('pycon.views',
    url(r"^proposal$", 'proposal_add', name='proposal_add'),
    url(r"^proposal-sent$", 'proposal_sent', name='proposal_sent'),
)

