from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from .models import ResourcePage


# Unauthenticated Views
def home(request):
    # This view is the primary page for the website.
    authform = AuthenticationForm(request.POST or None)
    context = {'login_dialog': authform}

    return render(request, 'PPS_Home.html', context)


def create_member(request):
    # This view allows visitors to register for Membership so that they can see the Authenticated pages of the site.
    regform = MemberForm(request.POST or None)
    context = {'registration': regform}
    if regform.is_valid():
        reg = regform.save(commit=False)
        reg.save()
        return redirect()

    return render(request, 'create_member.html', context)


def resources(request):
    '''
    This view allows a visitor to navigate to a Resource Page appropriate to per particular situation (Survivor, Caregiver,
    Health Care Professional).
    '''
    authform = AuthenticationForm(request.POST or None)
    context = {'login_dialog': authform}

    return render(request, 'resources.html', context)

def resource_type(request, slug):
    # This view allows a Member to look for situation-specific Resources.
    authform = AuthenticationForm(request.POST or None)
    page = ResourcePage.objects.get(slug=slug)
    context = {'login_dialog': authform, 'page': page}

    return render(request, 'ResourcePage.html', context)


def contact(request):
    # This view allows visitors to contact the site admin via e-mail (request info, report bugs, etc.).
    authform = AuthenticationForm(request.POST or None)
    pagename = 'Contact Us'
    context = {'login_dialog': authform, 'page_title': pagename}

    return render(request, 'contact.html', context)


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


