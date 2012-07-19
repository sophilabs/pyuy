from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url("", include("pycon.urls")),
    url(r"^speaker/", include("symposion.speakers.urls")),
    url(r"^proposal/", include("symposion.proposals.urls")),
    url(r"^review/", include("symposion.review.urls")),
    url(r"^sponsors/", include("symposion.sponsors_pro.urls")),
    url(r"^schedule/", include("symposion.schedule.urls")),
    url(r'^admin/', include(admin.site.urls)),
)
