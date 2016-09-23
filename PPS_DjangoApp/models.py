from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField()


class TextPage(Page):
    text_content = models.TextField(null=False, blank=False)


class ResourcePage(Page):
    resource_listing = models.TextField(null=False, blank=False)
    resource_title = models.CharField(max_length=)


