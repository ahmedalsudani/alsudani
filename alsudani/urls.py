from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alsudani.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Parked URL patterns:
    # url(r'blog/', include('')),
    # url(r'portfolio/', include('')),
    # url(r'lab/', include('')),
    # url(r'projects/', include('')),


    url(r'^admin/', include(admin.site.urls)),
)
