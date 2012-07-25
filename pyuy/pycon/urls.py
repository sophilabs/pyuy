from django.conf.urls import *


urlpatterns = patterns('pycon.views',
    url(r"^$", 'index'),
    url(r"^proposal_add/$", 'proposal_add'),
    url(r"^proposal_sent/$", 'proposal_sent'),
    url(r"^sign_up/", 'sign_up'),
    url(r"^signed/$", 'signed'),
)

urlpatterns += patterns('',
    url(r"^accounts/login/", 'django.contrib.auth.views.login', {'template_name': 'log_in.html'}),
    url(r"^accounts/log_out/$", 'django.contrib.auth.views.logout_then_login', {'login_url': '../login'}),
)