from django.db import models
from django.contrib.auth.models import User
from .choices import COUNTRIES, STATES, PROVINCES

PRONOUNS = (
    ('F', '\"she\" and \"her\"'),
    ('M', '\"he\" and \"him\"'),
    ('NP', '\"they\" and \"their\"'),
    ('NS1', '\"zie\" and \"zir\"'),
    ('NS2', '\"per\" and \"per\"'),
)


MEMBER_CLASS = (
    ('PS', 'Polio Survivor'),
    ('CG', 'Caregiver'),
    ('FM', 'Family Member'),
    ('HCP', 'Health Care Provider'),
    ('IO', 'Interested Other'),
    ('NR', 'Choose Not to Respond'),
)


GROUP_TYPE = (
    ('IP', 'In Person'),
    ('PH', 'Phone Conference Call'),
    ('OL', 'Online'),
    ('MX', 'Mixed (In Person +)'),
)


OL_GROUP_TYPE = (
    ('AO', 'Audio Only'),
    ('CH', 'Chat'),
    ('FB', 'Facebook'),
    ('FT', 'FaceTime'),
    ('G+', 'Google+'),
    ('SK', 'Skype'),
    ('YG', 'Yahoo Groups'),
)


class Address(models.Model):
    country = models.CharField(max_length=50, null=True, blank=True, choices=COUNTRIES, default='USA')
    address = models.CharField(max_length=256, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True, choices=STATES, default='OR')
    zip = models.PositiveSmallIntegerField(null=True, blank=True)
    province = models.CharField(max_length=2, null=True, blank=True, choices=PROVINCES, default='BC')
    postal_code = models.CharField(max_length=7, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return "{}, {}".format(self.city, self.state)


class SupportGroup(models.Model):
    group_name = models.CharField(max_length=50, null=True, blank=True)
    group_type = models.CharField(max_length=2, chioces=GROUP_TYPE)
    is_restricted = models.BooleanField(default=False)
    contact_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    next_mtg_date = models.DateField()
    next_mtg_time = models.DateField()
    mtg_repeat_pattern = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        if self.group_name:
            return "{}, {}".format(self.group_name, self.contact_number)
        else:
            return "{}, {}".format(self.contact_name, self.contact_number)

class InPersonSupptGrp(SupportGroup):
    loc_addr = models.ForeignKey(Address, related_name='group_location_is')

    def __str__(self):
        if self.group_name:
            return "{}, {}".format(self.group_name, self.loc_addr)
        else:
            return "{}, {}".format(self.contact_name, self.loc_addr)

class PhoneSupptGrp(SupportGroup):
    call_in_num = models.CharField(max_length=15, null=False, blank=False)
    participant_key = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        if self.group_name:
            return "{}, {}".format(self.group_name, self.call_in_num)
        else:
            return "{}, {}".format(self.contact_name, self.call_in_num)

class OnlineSupptGrp(SupportGroup):
    access_point = models.URLField(null=True, blank=True)
    ol_group_type = models.CharField(max_length=2, chioces=OL_GROUP_TYPE)
    facilitator_username = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        if self.group_name:
            return "{}, {}".format(self.group_name, self.ol_group_type)
        else:
            return "{}, {}".format(self.contact_name, self.ol_group_type)


class Member(models.Model):
    user = models.OneToOneField(User)
    offline_name = models.TextField()
    address = models.ForeignKey(Address, related_name='member_address_is')
    birthdate = models.DateField(auto_now_add=False)
    joindate = models.DateField(auto_now_add=True)
    gender = models.TextField(null=True, blank=True)
    pronouns = models.CharField(max_length=3, null=True, blank=True, choices=PRONOUNS)
    bio = models.TextField()
    profile_img = models.ImageField(null=True)
    profile_img_thumb = models.ImageField(null=True)
    issubscribed = models.BooleanField(default=False)
    sppt_grp_memb = models.ManyToManyField(SupportGroup, blank=True)
    group_coord = models.BooleanField(default=False)
    siteadmin = models.BooleanField(default=False)

    def __str__(self):
        return "{}, {}".format(self.username, self.state)


class Classification(models.Model):
    member = models.ManyToManyField(Member)
    class_title = models.CharField(max_length=25, null=False, blank=False, choices=MEMBER_CLASS)

    def __str__(self):
        return "{}, {}".format(self.username, self.class_title)


class Chat_Session(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)
    chat_topic = models.CharField(max_length=50, null=True, blank=True)
    chat_members = models.ManyToManyField(Member)
    datetime_ended = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{}, {}".format(self.chat_topic, self.chat_members)


class Chat_Message(models.Model):
    sending_user = models.OneToOneField(Member)
    datetime_sent = models.DateTimeField(auto_now_add=True)
    message_content = models.TextField()
    message_session = models.ForeignKey(Chat_Session)

    def __str__(self):
        return "{}, {}".format(self.sending_user, self.datetime_sent)