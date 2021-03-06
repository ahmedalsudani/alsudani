from django.contrib import admin
from django.db import models as django_models
from pagedown.widgets import AdminPagedownWidget
from . import models


class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        django_models.TextField: {'widget': AdminPagedownWidget}
    }
    prepopulated_fields = {'slug': ('project_name', )}


class PageAdmin(admin.ModelAdmin):
    formfield_overrides = {
        django_models.TextField: {'widget': AdminPagedownWidget}
    }
    prepopulated_fields = {'slug': ('page_name', )}


admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.EphemeralPage, PageAdmin)
