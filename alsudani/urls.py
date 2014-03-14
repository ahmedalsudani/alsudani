from django.conf.urls import patterns, include, url
from django.http import HttpResponse
import home.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alsudani.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Parked URL patterns:
    # url(r'portfolio/', include('')),
    # url(r'lab/', include('')),
    # url(r'projects/', include('')),

    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^$', home.views.index, name='index'),
    url(r'^about/$', home.views.about, name='about'),
    url(r'blog/', include('simpleblog.urls'), name='blog'),
    url(r'^healthcheck/', lambda request: HttpResponse('OK'), name='healthcheck'),
)
