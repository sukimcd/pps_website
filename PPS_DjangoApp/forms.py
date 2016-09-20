from django import forms
from .models import Member

class MemberRegForm(forms.Form):
    pass


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class MailListRegForm(forms.ModelForm):
    username = forms.TextInput()
    class Meta:
        model = Member
        fields = '__all__'


class MailMsgForm(forms.Form):
    username = forms.TextInput()
