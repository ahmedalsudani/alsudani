from datetime import datetime, timedelta
from django.db import models


def a_week_from_now():
    return datetime.now() + timedelta(days=7)

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    slug = models.SlugField()
    project_url = models.URLField()
    summary = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.project_name

class Page (models.Model):
    page_name = models.CharField(max_length=200)
    slug = models.SlugField()
    contents = models.TextField()

    def __unicode__(self):
        return self.page_name

class EphemeralPage(Page):
    expiration = models.DateTimeField(default=a_week_from_now, blank=True)
