from django.db import models
from django.contrib.auth.models import User


STATES = (
    ('AK', 'Alaska'),
    ('AL', 'Alabama'),
    ('AR', 'Arkansas'),
    ('AS', 'American Samoa'),
    ('AZ', 'Arizona'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DC', 'District of Columbia'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('FM', 'Federated States of Microsnesia'),
    ('GA', 'Georgia'),
    ('GU', 'Guam'),
    ('HI', 'Hawaii'),
    ('IA', 'Iowa'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('MA', 'Massachusetts'),
    ('MD', 'Maryland'),
    ('ME', 'Maine'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MO', 'Missouri'),
    ('MP', 'Northern Mariana Islands'),
    ('MS', 'Mississippi'),
    ('MT', 'Montana'),
    ('NA', 'National'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('NE', 'Nebraska'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NV', 'Nevada'),
    ('NY', 'New York'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('PR', 'Puerto Rico'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VA', 'Virginia'),
    ('VI', 'Virgin Islands'),
    ('VT', 'Vermont'),
    ('WA', 'Washington'),
    ('WI', 'Wisconsin'),
    ('WV', 'West Virginia'),
    ('WY', 'Wyoming')
  )

PROVINCES = (
    ('AB', 'Alberta'),
    ('BC', 'British Columbia'),
    ('LB', 'Labrador'),
    ('MB', 'Manitoba'),
    ('NB', 'New Brunswick'),
    ('NF', 'Newfoundland'),
    ('NS', 'Nova Scotia'),
    ('NU', 'Nunavut'),
    ('NW', 'North West Terr.'),
    ('ON', 'Ontario'),
    ('PE', 'Prince Edward Is.'),
    ('QC', 'Quebec'),
    ('SK', 'Saskatchewen'),
    ('YU', 'Yukon')
)


class Address(models.Model):
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATES, default='OR')
    zip = models.PositiveSmallIntegerField()
    province = models.CharField(max_length=2, choices=PROVINCES, default='BC')
    postal_code = models.CharField(max_length=7)


class Member(models.Model):
    user = models.OneToOneField(User)
    address = models.ForeignKey(Address, related_name='member_address_is')
    birthdate = models.DateField(auto_now_add=False)
    gender = models.TextField(null=True, blank=True)
    pronouns = models.TextField(null=True, blank=True)
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

