# Create your views here.
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from symposion.speakers.models import Speaker
from forms import ProposalForm, SignForm
from symposion.proposals.models import Proposal
from django.template import RequestContext
from django.contrib.auth.admin import User

def index(request):
    return render_to_response('index.html')

@login_required
def proposal_add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ProposalForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            kind =  form.cleaned_data['kind']
            category =  form.cleaned_data['category']
            abstract = form.cleaned_data['abstract']
            audience_level = form.cleaned_data['audience_level']
            additional_notes = form.cleaned_data['additional_notes']
            extreme =  form.cleaned_data['extreme']
            duration =  form.cleaned_data['duration']
            additional_speakers = form.cleaned_data['additional_speakers']
            submitted = datetime.datetime.now()
            speaker = Speaker.objects.get(user=request.user)

            p = Proposal.objects.create(title=title, description=description, kind=kind, category=category, abstract=abstract, audience_level=audience_level, additional_notes=additional_notes, extreme=extreme, duration=duration, speaker=speaker, submitted=submitted, cancelled=False)
            if additional_speakers is not None:
                p.additional_speakers.add(additional_speakers)

            p.save()
            return HttpResponseRedirect('/proposal_sent/') # Redirect after POST
    else:
        form = ProposalForm() # An unbound form

    return render_to_response('proposal_add.html', {
        'form': form,
        }, RequestContext(request))


def sign_up(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            biography = form.cleaned_data['biography']
            username = form.cleaned_data['user_name']
            annotation = form.cleaned_data['annotation']
            email= form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                speaker = Speaker.objects.create(user=user, name=name, biography=biography, annotation=annotation, invite_token="")
                speaker.save()
                ret= HttpResponseRedirect('/signed/')
            except IntegrityError:
                ret= render_to_response('sign_up.html', {
                    'form': form,
                    })

            return ret
    else:
        form = SignForm() # An unbound form

    return render_to_response('sign_up.html', {
        'form': form,
        }, RequestContext(request))


def signed(request):
    return render_to_response('signed.html')


def proposal_sent(request):
    return render_to_response('proposal_sent.html')