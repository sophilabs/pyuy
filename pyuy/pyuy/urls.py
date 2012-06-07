from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r"^speaker/", include("symposion.speakers.urls")),
    url(r"^proposal/", include("symposion.proposals.urls")),
    url(r"^review/", include("symposion.review.urls")),
    url(r"^sponsors/", include("symposion.sponsors_pro.urls")),
    url(r"^schedule/", include("symposion.schedule.urls")),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
