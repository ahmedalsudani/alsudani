from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

# Create your views here.

def index(request, template='index.html'):
    t = loader.get_template(template)
    # How ugly
    return HttpResponse(t.render(Context({
        'title': 'Hello, world!'
    })))

def about(request, template='about.html'):
    t = loader.get_template(template)
    return HttpResponse(t.render(Context({'title': 'About'})))