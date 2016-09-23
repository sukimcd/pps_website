from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


# Unauthenticated Views
def create_member(request):
    # This view allows visitors to register for Membership so that they can see the Authenticated pages of the site.
    regform = MemberForm(request.POST or None)
    context = {'registration': regform}
    if regform.is_valid():
        reg = regform.save(commit=False)
        reg.save()
        return redirect()

    return render(request, 'create_member.html', context)


def spprtgroups(request):
    '''
    This view allows a Member to locate either an online Support Group, or a face-to-face Support Group within a preset
    distance radius of a specific geographical region (based on their current location when provided, otherwise based on
    a specific city name).
    '''
    authform = AuthenticationForm(request.POST or None)
    pagename = 'Find a Support Group'
    context = {'login_dialog': authform, 'page_title': pagename}

    return render(request, 'spprtgroups.html', context)


# Authenticated Views
def account(request):
    '''
    This view allows Members to make changes to Member Account info, and therefore must accept both POST and GET
    requests.
    '''
    pagename = 'Manage Your Member Account'
    context = {'page_title': pagename}

    return render(request, 'account.html', context)
