# Create your views here.
import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import password_change
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from symposion.speakers.models import Speaker
from symposion.proposals.models import Proposal
from django.template import RequestContext
from pycon.forms import SpeakerForm, UserCreateForm, ProfileForm, ProposalForm

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

@login_required
def proposal_add(request):
    if request.method == 'POST': # If the form has been submitted...
        formP = ProposalForm(request.POST) # A form bound to the POST data
        formS = SpeakerForm(request.POST)
        try:
            Speaker.objects.get(user=request.user)
            speaker = Speaker.objects.get(user=request.user)
        except Speaker.DoesNotExist:
            if formS.is_valid():
                    biography = formS.cleaned_data['biography']
                    annotation = formS.cleaned_data['annotation']

                    speaker = Speaker.objects.create(user=request.user, name=request.user.first_name+' '+request.user.last_name, biography=biography, annotation=annotation, invite_email=request.user.email, invite_token="")
                    speaker.save()
            else:
                return render_to_response('proposal_add.html', {
                    'formP':formP, 'formS':formS
                }, context_instance=RequestContext(request))

        if formP.is_valid():
            title = formP.cleaned_data['title']
            description = formP.cleaned_data['description']
            kind =  formP.cleaned_data['kind']
            category =  formP.cleaned_data['category']
            abstract = formP.cleaned_data['abstract']
            audience_level = formP.cleaned_data['audience_level']
            additional_notes = formP.cleaned_data['additional_notes']
            extreme =  formP.cleaned_data['extreme']
            duration =  formP.cleaned_data['duration']
            additional_speakers = formP.cleaned_data['additional_speakers']
            submitted = datetime.datetime.now()

            proposal = Proposal.objects.create(title=title, description=description, kind=kind, category=category, abstract=abstract, audience_level=audience_level, additional_notes=additional_notes, extreme=extreme, duration=duration, speaker=speaker, submitted=submitted, cancelled=False)
            if additional_speakers is not None:
                proposal.additional_speakers.add(additional_speakers)

            proposal.save()
            return HttpResponseRedirect('/proposal_sent/') # Redirect after POST
    else:
        try:
            Speaker.objects.get(user=request.user)
            formS = ""
        except Speaker.DoesNotExist:
            formS = SpeakerForm()
        formP = ProposalForm()

    return render_to_response('proposal_add.html', {
        'formP':formP, 'formS':formS
        }, RequestContext(request))

def proposal_sent(request):
    return render_to_response('proposal_sent.html', context_instance=RequestContext(request))


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
            if User.objects.filter(username=username).count() > 0:
                if username != user.username:
                    messages.add_message(request, messages.ERROR, u'%s already exists' % username)
            else:
                user.username = username
                user.first_name=first_name
                user.last_name=last_name
                user.email = username
                user.save()
                messages.add_message(request, messages.SUCCESS, 'Profile updated successfully.')

            return HttpResponseRedirect('')
    else:
        form = ProfileForm(data)
    return render_to_response('profile.html', {'form' : form}, context_instance=RequestContext(request))

def my_password_change(request):
    response = password_change(request, template_name='password_change.html', post_change_redirect= '../../accounts/profile')
    if isinstance(response, HttpResponseRedirect):
        messages.add_message(request, messages.SUCCESS, 'Password changed successfully.')
    return response