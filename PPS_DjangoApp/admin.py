from django.contrib import admin
from .models import Page, TextPage, ResourcePage, ResourceListing

# Register your models here.

admin.site.register(Page)
admin.site.register(TextPage)
admin.site.register(ResourcePage)
admin.site.register(ResourceListing)