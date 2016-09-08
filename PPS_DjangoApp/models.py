from django.db import models
from django.contrib.auth.models import User


STATES=(('key','arg'),)

class Member(models.Model):
    user = models.OneToOneField(User)
    birthdate = models.DateField(auto_now_add=False)
    issubscribed = models.BooleanField(default=False)
    resstate = models.CharField(max_length=30, choices=STATES)
