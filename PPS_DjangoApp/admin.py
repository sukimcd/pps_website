from django.contrib import admin
from .models import Page, TextPage, ResourcePage

# Register your models here.

admin.site.register(Page)
admin.site.register(TextPage)
admin.site.register(ResourcePage)