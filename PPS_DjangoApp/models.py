from django.db import models
from django.contrib.auth.models import User
from .choices import COUNTRIES, STATES, PROVINCES, PRONOUNS


class Address(models.Model):
    country = models.CharField(max_length=50, null=True, blank=True, choices=COUNTRIES, default='USA')
    address = models.CharField(max_length=256, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True, choices=STATES, default='OR')
    zip = models.PositiveSmallIntegerField(null=True, blank=True)
    province = models.CharField(max_length=2, null=True, blank=True, choices=PROVINCES, default='BC')
    postal_code = models.CharField(max_length=7, null=True, blank=True)

    def __str__(self):
        return "{}, {}".format(self.address.city, self.address.state)


class Member(models.Model):
    user = models.OneToOneField(User)
    offline_name = models.TextField()
    address = models.ForeignKey(Address, related_name='member_address_is')
    birthdate = models.DateField(auto_now_add=False)
    gender = models.TextField(null=True, blank=True)
    pronouns = models.CharField(max_length=3, null=True, blank=True, choices=PRONOUNS)
    bio = models.TextField()
    issubscribed = models.BooleanField(default=False)
    group_coord = models.BooleanField(default=False)

    def __str__(self):
        return "{}, {}".format(self.user.username, self.address.state)


class SupportGroup(models.Model):
    loc_addr = models.ForeignKey(Address, related_name='group_address_is')
    mtg_day = models.DateField()
    mtg_time = models.DateField()
    members = models.ManyToManyField(Member)

