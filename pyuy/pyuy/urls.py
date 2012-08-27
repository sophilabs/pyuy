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
    url(r'', include('account.urls', namespace='account')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {
        'sitemaps': {
            'cmspages': CMSSitemap,
            'blogentries': BlogSitemap
        }
    }),
    url(r'^', include('cms.urls')),
)