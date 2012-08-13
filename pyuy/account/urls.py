from django.conf.urls import *

urlpatterns = patterns('account.views',
    url(r"^sign-up$", 'sign_up', name='sign_up'),
    url(r"^sign-in$", 'sign_in', name="sign_in"),
    url(r"^sign-out$", 'sign_out', name="sign_out"),
    url(r"^password-change$", 'password_change', name="password_change"),
    url(r"^password-change$/done$", 'password_change_done', name="password_change_done"),
    url(r"^password-reset$", 'password_reset', name="password_reset"),
    url(r"^password-reset/done$", 'password_reset_done', name="password_reset_done"),
    url(r"^password-reset/confirm/(?P<uidb36>[-\w]+)/(?P<token>[-\w]+)$", 'password_reset_confirm', name="password_reset_confirm"),
    url(r"^password/reset/complete$", 'password_reset_complete', name="password_reset_complete"),
    url(r"^profile$", 'profile', name="profile"),

)

