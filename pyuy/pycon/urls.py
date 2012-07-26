from django.conf.urls import *


urlpatterns = patterns('pycon.views',
    url(r"^$", 'index'),
    url(r"^proposal_add/$", 'proposal_add'),
    url(r"^proposal_sent/$", 'proposal_sent'),
    url(r"^sign_up/$", 'sign_up'),
    url(r"^signed/$", 'signed'),
    url(r"^accounts/profile/$", 'profile'),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r"^accounts/login/", 'login', {'template_name': 'log_in.html'}),
    url(r"^accounts/log_out/$", 'logout_then_login', {'login_url': '../login'}),
)