from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Member
from .forms import MemberForm
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm



def home(request):
    context={}
    return render(request, 'PPS_Home.html', context)


def login(request):
    authform = AuthenticationForm(request.POST or None)
    context = {'loginpage': authform}
    return render(request, 'login.html', context)


def account(request):
    context={}
    return render(request, 'account.html', context)


def chat(request):
    context={}
    return render(request, 'chat.html', context)


def calendar(request):
    context={}
    return render(request, 'calendar.html', context)


def resources(request):
    context={}
    return render(request, 'resources.html', context)


def contact(request):
    context={}
    return render(request, 'contact.html', context)


def spprtgroups(request):
    context={}
    return render(request, 'spprtgroups.html', context)

