from cms.sitemaps.cms_sitemap import CMSSitemap
from cmsplugin_blog.sitemaps import BlogSitemap
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()


urlpatterns = patterns('pyuy.views',
    url(r"^$", 'index'),
    url(r"^sign_up/$", 'sign_up'),
    url(r"^accounts/profile/$", 'profile'),
    url(r"^password/change/$", 'my_password_change'),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r"^accounts/login/$", 'login', {'template_name': 'log_in.html'}),
    url(r"^accounts/log_out/$", 'logout_then_login', {'login_url': '../login'}),
    url(r'^password/reset/$','password_reset',{'template_name': 'password_reset.html'}),
    url(r'^password/reset/done/$','password_reset_done',{'template_name': 'password_reset_done.html'}),
    url(r'^password/reset/confirm/(?P<uidb36>[-\w]+)/(?P<token>[-\w]+)/$','password_reset_confirm',{'template_name': 'password_reset_confirm.html'}),
    url(r'^password/reset/complete/$','password_reset_complete',{'template_name': 'password_reset_complete.html'}),
)

urlpatterns += patterns('',
    url(r"^pycon/", include("pycon.urls")),
    url(r"^speaker/", include("symposion.speakers.urls")),
    url(r"^proposal/", include("symposion.proposals.urls")),
    url(r"^review/", include("symposion.review.urls")),
    url(r"^sponsors/", include("symposion.sponsors_pro.urls")),
    url(r"^schedule/", include("symposion.schedule.urls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {
        'sitemaps': {
            'cmspages': CMSSitemap,
            'blogentries': BlogSitemap
        }
    }),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns