from django.db import models
from PPS_AccountsApp.models import Address


class Page(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(null=False)


class TextPage(Page):
    text_content = models.TextField(null=False, blank=False)


class ResourcePage(Page):
    resource_listing = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title


class ResourceListing(models.Model):
    resource_page = models.ForeignKey(ResourcePage, related_name='listings')
    ext_ref = models.URLField(null=True)
    ext_source = models.TextField()
    resource_title = models.CharField(max_length=250)
    resource_locator = models.OneToOneField(Address)

    def __str__(self):
        return self.resource_title