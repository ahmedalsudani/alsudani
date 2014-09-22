from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    slug = models.SlugField()
    project_url = models.URLField()
    summary = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.project_name
