from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Member
from .forms import MemberForm
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm


# Unauthenticated Views
def home(request):
    # This view is the primary page for the website.
    authform = AuthenticationForm(request.POST or None)
    pagename = 'Post-Polio Syndrome'
    context = {'login_dialog': authform, 'page_title': pagename}
    return render(request, 'PPS_Home.html', context)


def create_member(request):
    # This view allows visitors to register for Membership so that they can see the Authenticated pages of the site.
    regform = MemberForm(request.POST or None)
    pagename = 'Create a Member Account'
    context = {'registration': regform, 'page_title': pagename}
    if regform.is_valid():
        reg = regform.save(commit=False)
        reg.save()
        return redirect()

    return render(request, 'create_member.html', context)


def resources(request):
    '''
    This view allows a visitor to look for Resources appropriate to per particular situation (Survivor, Caregiver,
    Health Care Professional).
    '''
    authform = AuthenticationForm(request.POST or None)
    pagename = 'Post-Polio Syndrome Resources'
    context = {'login_dialog': authform, 'page_title': pagename}

    return render(request, 'resources.html', context)

def survivor_resources(request):
    # This view allows a Survivor to look for Survivor-specific Resources.
    authform = AuthenticationForm(request.POST or None)
    pagename = 'Resources for Polio Survivors'
    context = {'login_dialog': authform, 'page_title': pagename}

    return render(request, 'survivor_resources.html', context)

def caregiver_resources(request):
    # This view allows a Caregiver to look for Caregiver-specific Resources.
    authform = AuthenticationForm(request.POST or None)
    pagename = 'Resources for Post-Polio Syndrome Caregivers'
    context = {'login_dialog': authform, 'page_title': pagename}

    return render(request, 'caregiver_resources.html', context)

def hcp_resources(request):
    # This view allows a Health-Care Professional to look for HCP-specific Resources.
    authform = AuthenticationForm(request.POST or None)
    pagename = 'Resources for Post-Polio Syndrome Health-Care Professionals'
    context = {'login_dialog': authform, 'page_title': pagename}

    return render(request, 'hcp_resources.html', context)


def contact(request):
    # This view allows visitors to contact the site admin via e-mail (request info, report bugs, etc.).
    authform = AuthenticationForm(request.POST or None)
    pagename = 'Contact Us'
    context = {'login_dialog': authform, 'page_title': pagename}

    return render(request, 'contact.html', context)


def spprtgroups(request):
    '''
    This view allows a Member to locate either an online Support Group, or a face-to-face Support Group within a pre-set
    distance radius of a specific geographical region (based on their current location when provided, otherwise based on
    a specific city name).
    '''
    authform = AuthenticationForm(request.POST or None)
    pagename = 'Find a Support Group'
    context = {'login_dialog': authform, 'page_title': pagename}

    return render(request, 'spprtgroups.html', context)


def unauth_error(request):
    '''
    This view displays an error message notifying Members when a page has been requested that requires Authentication.
    It displays the login dialog box and a link to the "Create a New Member Account".
    '''
    authform = AuthenticationForm(request.POST or None)
    pagename = 'Authentication Required'
    context = {'login_dialog': authform, 'page_title': pagename}

    return render(request, 'unauth_error.html', context)


# Authenticated Views
def account(request):
    '''
    This view allows Members to make changes to Member Account info, and therefore must accept both POST and GET
    requests.
    '''
    pagename = 'Manage Your Member Account'
    context = {'page_title': pagename}

    return render(request, 'account.html', context)


def chat(request):
    # This view allows Members to enter real-time chat sessions with one another, either one-on-one or in groups.
    pagename = 'Chat with Other Members'
    context = {'page_title': pagename}

    return render(request, 'chat.html', context)


def calendar(request):
    '''
    This view allows Members to view the Event Calendar and to make or change selections for the distance radius (based
    on their current location when given, otherwise based on a specific city name) within which the events they wish to
    see will be located. It therefore must accept both POST and GET requests.
    '''
    pagename = 'View the Event Calendar'
    context = {'page_title': pagename}

    return render(request, 'calendar.html', context)


def mailing_list(request):
    '''
    This view allows Members to join the Mailing List and to make or change selections regarding what mail they wish to
    receive and how often those messages should be sent. It therefore must accept both POST and GET requests.
    '''
    pagename = 'Join the Mailing List'
    context = {'page_title': pagename}

    return render(request, 'chat.html', context)
