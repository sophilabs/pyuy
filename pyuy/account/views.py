from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import forms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import views as aviews
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import re
from django.contrib import messages

@login_required
def profile(request):
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user = request.user
            user.username = username
            user.email = username
            messages.add_message(request, messages.SUCCESS, 'Profile updated successfully.')
            user.first_name=first_name
            user.last_name=last_name
            user.save()

            return HttpResponseRedirect('')
    else:
        form = ProfileForm(instance=request.user)
    return render_to_response('profile.html', {'form' : form}, context_instance=RequestContext(request))
#    if request.method == "POST":
#        form = forms.ProfileForm(request.POST)
#        if form.is_valid():
#            user = request.user
#            user.first_name = form.cleaned_data['first_name']
#            user.last_name = form.cleaned_data['last_name']
#            user.username = form.cleaned_data['email']
#            user.email = form.cleaned_data['email']
#            user.save()
#            user.profile.imdb_url = form.cleaned_data['imdb_url']
#            user.profile.reel_url = form.cleaned_data['reel_url']
#            user.profile.save()
#            if user.pitch_set.count() == 0:
#                return HttpResponseRedirect(reverse("filmmakers:pitch"))
#            else:
#                messages.add_message(request, messages.INFO, "Profile Saved")
#    else:
#        form = forms.ProfileForm()
#        form.initial['first_name'] = request.user.first_name
#        form.initial['last_name'] = request.user.last_name
#        form.initial['email'] = request.user.email
#        form.initial['imdb_url'] = request.user.profile.imdb_url
#        form.initial['reel_url'] = request.user.profile.reel_url
#    return render_to_response(
#        "profile.html",
#            { 'form': form },
#        context_instance=RequestContext(request))

def login(request):
    return aviews.login(request,
        template_name="login.html",
        authentication_form=forms.AuthenticationForm)

def logout(request):
    return aviews.logout(request, next_page=reverse('main:index'))

def password_reset(request):
    return aviews.password_reset(request, is_admin_site=False,
        template_name='password_reset_form.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt',
        password_reset_form=forms.PasswordResetForm,
        post_reset_redirect=reverse('account:password_reset_done'))

def password_reset_done(request):
    return aviews.password_reset_done(request,
        template_name='password_reset_done.html')

def password_reset_complete(request):
    return aviews.password_reset_complete(request,
        template_name='password_reset_complete.html')

def password_reset_confirm(request, uidb36, token):
    return aviews.password_reset_confirm(request, uidb36, token,
        template_name='password_reset_confirm.html',
        set_password_form=forms.SetPasswordForm,
        post_reset_redirect=reverse('account:password_reset_confirm_done'))

def password_reset_confirm_done(request):
    return aviews.password_reset_complete(request,
        template_name='password_reset_confirm_done.html')

def password_change(request):
    return aviews.password_change(request,
        template_name='password_change.html',
        post_change_redirect=reverse('account:password_change_done'),
        password_change_form=forms.PasswordChangeForm)

def password_change_done(request):
    return aviews.password_change_done(request,
        template_name='password_change_done.html')