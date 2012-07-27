# Create your views here.
import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from symposion.speakers.models import Speaker
from forms import ProposalForm
from symposion.proposals.models import Proposal
from django.template import RequestContext
from pycon.forms import SpeakerForm, UserCreateForm, ProfileForm, PasswordForm

def index(request):
    return render_to_response('index.html')

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
                    name = formS.cleaned_data['name']
                    biography = formS.cleaned_data['biography']
                    annotation = formS.cleaned_data['annotation']

                    speaker = Speaker.objects.create(user=request.user, name=name, biography=biography, annotation=annotation, invite_email=request.user.email, invite_token="")
                    speaker.save()
            else:
                return render_to_response('proposal_add.html', {
                    'formP':formP, 'formS':formS
                }, RequestContext(request))

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


def sign_up(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect('../signed')
    else:
        form = UserCreateForm()

    return render_to_response('sign_up.html', {'form' : form}, context_instance=RequestContext(request))

def signed(request):
    return render_to_response('signed.html')

def proposal_sent(request):
    return render_to_response('proposal_sent.html')

@login_required
def profile(request):
    data = {'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email}
    if request.method == 'POST':
        form = ProfileForm(request.POST, data)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            user = User.objects.get(username=request.user.username)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.save()
            return HttpResponseRedirect('../profile')
    else:
        form = ProfileForm(data)
    return render_to_response('profile.html', {'form' : form}, context_instance=RequestContext(request))