from django.contrib import admin
from . import models


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('project_name', )}

admin.site.register(models.Project, ProjectAdmin)
