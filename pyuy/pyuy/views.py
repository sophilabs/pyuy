from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import password_change
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from pycon.forms import ProfileForm, UserCreateForm

def index(request):
    return render_to_response('base.html', context_instance=RequestContext(request))

def sign_up(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            new_user = User.objects.create_user(username=username, email=username, password=password1)
            new_user.save()
            new_user= authenticate(username=username, password=password1)
            login(request, new_user)
            messages.add_message(request, messages.SUCCESS, 'You were registered successfully.')
            return HttpResponseRedirect('../accounts/profile')
    else:
        form = UserCreateForm()

    return render_to_response('sign_up.html', {'form' : form}, context_instance=RequestContext(request))

@login_required
def profile(request):
    data = {'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,}
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user = request.user
            if username != user.username:
                if User.objects.filter(username=username).count() > 0:
                    messages.add_message(request, messages.ERROR, u'%s already exists' % username)
                    messages.add_message(request, messages.SUCCESS, 'Personal data updated correctly.')
            else:
                user.username = username
                user.email = username
                messages.add_message(request, messages.SUCCESS, 'Profile updated successfully.')
            user.first_name=first_name
            user.last_name=last_name
            user.save()


            return HttpResponseRedirect('')
    else:
        form = ProfileForm(data)
    return render_to_response('profile.html', {'form' : form}, context_instance=RequestContext(request))

def my_password_change(request):
    response = password_change(request, template_name='password_change.html', post_change_redirect= '../../accounts/profile')
    if isinstance(response, HttpResponseRedirect):
        messages.add_message(request, messages.SUCCESS, 'Password changed successfully.')
    return response