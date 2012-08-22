from cms.sitemaps.cms_sitemap import CMSSitemap
from cmsplugin_blog.sitemaps import BlogSitemap
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic.simple import redirect_to

from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +patterns('',
    url(r'', include('main.urls', namespace='main')),

    url(r'^pycon$', redirect_to, {'url': '/pycon/2012' }),
    url(r'^pycon/2012', include('pycon2012.urls', namespace='pycon2012')),

    url(r'^speaker', include('symposion.speakers.urls')),
    url(r'^proposal', include('symposion.proposals.urls')),
    url(r'^review', include('symposion.review.urls')),
    url(r'^sponsors', include('symposion.sponsors_pro.urls')),
    url(r'^schedule', include('symposion.schedule.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account', include('account.urls', namespace='account')),

    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {
        'sitemaps': {
            'cmspages': CMSSitemap,
            'blogentries': BlogSitemap
        }
    }),
    url(r'^', include('cms.urls')),
)