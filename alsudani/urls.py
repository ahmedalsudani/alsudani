from django.conf.urls import patterns, include, url
from django.http import HttpResponse
import alsudani.views


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
    url(r'^$', alsudani.views.about, name='index'),
    url(r'^projects/$', alsudani.views.projects_home, name='projects_home'),
    url(r'^projects/(?P<slug>[-\w]+)', alsudani.views.project_page, name='project'),
    url(r'^healthcheck/', lambda request: HttpResponse('OK'), name='healthcheck'),
)
