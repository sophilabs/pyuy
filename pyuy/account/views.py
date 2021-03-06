from cms.models.pagemodel import Page as Page_cms
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import forms
from django.contrib.auth import views as aviews, authenticate
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def profile(request):
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.instance.username = form.cleaned_data['username']
            form.instance.first_name = form.cleaned_data['first_name']
            form.instance.last_name = form.cleaned_data['last_name']
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Profile updated successfully.')
            return HttpResponseRedirect('')
    else:
        form = forms.ProfileForm(instance=request.user)
    return render_to_response('profile.html', {
        'form' : form,
    }, context_instance=RequestContext(request))

def sign_up(request, next_page=None):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.instance.username = form.cleaned_data['username']
            form.instance.password = form.cleaned_data['password1']
            form.instance.email = form.cleaned_data['username']
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Account created successfully.')
            authenticate(username=form.instance.username, password=form.instance.password)
            return HttpResponseRedirect(next_page or reverse('account:profile'))
    else:
        form = forms.UserCreationForm()
    return render_to_response('sign_up.html',{
        'form' : form,
        }, context_instance=RequestContext(request))

def sign_in(request):
    return aviews.login(request,
        template_name="sign_in.html",
        authentication_form=forms.AuthenticationForm)

def sign_out(request, next_page=None):
    return aviews.logout(request, next_page=next_page or '/')

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

def password_reset_confirm(request, uidb36, token, post_reset_redirect=None):
    return aviews.password_reset_confirm(request, uidb36, token,
        template_name='password_reset_confirm.html',
        set_password_form=forms.SetPasswordForm,
        post_reset_redirect=post_reset_redirect or reverse('account:password_reset_confirm_done'))

def password_reset_confirm_done(request):
    return aviews.password_reset_complete(request,
        template_name='password_reset_confirm_done.html')

def password_change(request):
    return aviews.password_change(request,
        template_name='password_change_form.html',
        post_change_redirect=reverse('account:password_change_done'),
        password_change_form=forms.PasswordChangeForm)

def password_change_done(request):
    return aviews.password_change_done(request,
        template_name='password_change_done.html')