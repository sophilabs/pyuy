from django.conf.urls import *

urlpatterns = patterns('pycon2012.views',
    url(r"^$", 'index', name='index'),
    url(r"^/proposal$", 'proposal_add', name='proposal_add'),
    url(r"^/about$", 'about', name='about'),
    url(r"^/proposal-sent$", 'proposal_sent', name='proposal_sent'),
)