# Create your views here.
import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from symposion.speakers.models import Speaker
from symposion.proposals.models import Proposal
from django.template import RequestContext
from pycon.forms import SpeakerForm, ProposalForm
from django.core.urlresolvers import reverse

def index(request):
    return render_to_response(reverse('pycon:index'), context_instance=RequestContext(request))

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
            #additional_speakers = formP.cleaned_data['additional_speakers']
            submitted = datetime.datetime.now()

            proposal = Proposal.objects.create(title=title, description=description, kind=kind, category=category, abstract=abstract, audience_level=audience_level, additional_notes=additional_notes, extreme=extreme, duration=duration, speaker=speaker, submitted=submitted, cancelled=False)
            if additional_speakers is not None:
                proposal.additional_speakers.add(additional_speakers)

            proposal.save()
            return HttpResponseRedirect('/pycon/proposal_sent/') # Redirect after POST
    else:
        try:
            Speaker.objects.get(user=request.user)
            formS = ""
        except Speaker.DoesNotExist:
            formS = SpeakerForm()
        formP = ProposalForm()

    return render_to_response('proposal_add.html', {
        'formP':formP, 'formS':formS
        }, context_instance=RequestContext(request))

def proposal_sent(request):
    return render_to_response('proposal_sent.html', context_instance=RequestContext(request))