from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Member
from .forms import MemberForm
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm


#Unauthenticated Views
def home(request):
    authform = AuthenticationForm(request.POST or None)
    context = {'login_dialog': authform}
    return render(request, 'PPS_Home.html', context)


def create_member(request):
    regform = MemberForm(request.POST or None)
    context = {'registration': regform}
    return render(request, 'create_member.html', context)


def resources(request):
    authform = AuthenticationForm(request.POST or None)
    context = {'login_dialog': authform}
    return render(request, 'resources.html', context)


def contact(request):
    authform = AuthenticationForm(request.POST or None)
    context = {'login_dialog': authform}
    return render(request, 'contact.html', context)


def spprtgroups(request):
    authform = AuthenticationForm(request.POST or None)
    context = {'login_dialog': authform}
    return render(request, 'spprtgroups.html', context)


def unauth_error(request):
    authform = AuthenticationForm(request.POST or None)
    context = {'login_dialog': authform}
    return render(request, 'unauth_error.html', context)



#Authenticated Views
def account(request):
    context={}
    return render(request, 'account.html', context)


def chat(request):
    context={}
    return render(request, 'chat.html', context)


def calendar(request):
    context={}
    return render(request, 'calendar.html', context)

