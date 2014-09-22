from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader, Context as DjangoContext
from django.conf import settings
from . import models
# Create your views here.


class Context (DjangoContext):
    def __init__(self, dict_=None,*args, **kwargs):
        if dict_ is None:
            dict_ = {
                'ga_code': settings.GA_CODE,
                'sc_project': settings.SC_PROJECT,
                'sc_security': settings.SC_SECURITY
            }
        else:
            dict_['ga_code'] = settings.GA_CODE
            dict_['sc_project'] = settings.SC_PROJECT
            dict_['sc_security'] = settings.SC_SECURITY
        super(Context, self).__init__(dict_, *args, **kwargs)


def index(request, template='alsudani/index.html'):
    t = loader.get_template(template)
    # How ugly
    return HttpResponse(t.render(Context({})))


def about(request, template='alsudani/about.html'):
    t = loader.get_template(template)
    return HttpResponse(t.render(Context({'title': 'About', })))


def projects_home(request, template='alsudani/projects_home.html'):
    t = loader.get_template(template)
    projects = models.Project.objects.all()
    return HttpResponse(t.render(Context({'title': 'Projects', 'projects': projects})))


def project_page(request, slug, template='alsudani/project.html'):
    project_query = models.Project.objects.filter(slug=slug)
    if (project_query):
        project = project_query[0]
        t = loader.get_template(template)
        return HttpResponse(t.render(Context({'title': project.project_name, 'project': project})))
    else:
        raise Http404
