from django.conf.urls import *

urlpatterns = patterns('pycon.views',
    url(r"^$", 'index'),
    url(r"^proposal_add/$", 'proposal_add'),
    url(r"^proposal_sent/$", 'proposal_sent'),
    url(r"^sign_up/$", 'sign_up'),
    url(r"^accounts/profile/$", 'profile'),
    url(r"^password/change/$", 'my_password_change'),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r"^accounts/login/", 'login', {'template_name': 'log_in.html'}),
    url(r"^accounts/log_out/$", 'logout_then_login', {'login_url': '../login'}),
    url(r'^password/reset/$','password_reset',{'template_name': 'password_reset.html'}),
    url(r'^password/reset/done/$','password_reset_done',{'template_name': 'password_reset_done.html'}),
    url(r'^password/reset/confirm/(?P<uidb36>[-\w]+)/(?P<token>[-\w]+)/$','password_reset_confirm',{'template_name': 'password_reset_confirm.html'}),
    url(r'^password/reset/complete/$','password_reset_complete',{'template_name': 'password_reset_complete.html'}),
)