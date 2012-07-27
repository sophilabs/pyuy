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
    url(r'^password/change/$', 'password_change', {'template_name': 'chng_pass.html'}),
    url(r'^password/change/done/$', 'password_change_done', {'template_name': 'pass_chnged.html'}),
    url(r'^password/reset/$','password_reset',{'template_name': 'reset_pass.html'}),
    url(r'^password/reset/done/$','password_reset_done',{'template_name': 'reset_pass_done.html'}),
    url(r'^password/reset/confirm/(?P<uidb36>[-\w]+)/(?P<token>[-\w]+)/$','password_reset_confirm',{'template_name': 'reset_pass_confirm.html'}),
    url(r'^password/reset/complete/$','password_reset_complete',{'template_name': 'reset_pass_complete.html'}),
)