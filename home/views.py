from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

# Create your views here.

def index(request):
    t = loader.get_template('index.html')
    # How ugly
    return HttpResponse(t.render(Context({})))