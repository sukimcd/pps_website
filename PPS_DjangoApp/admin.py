from django.contrib import admin
from .models import Address, Member, SupportGroup

# Register your models here.

admin.site.register(Address)
admin.site.register(Member)
admin.site.register(SupportGroup)