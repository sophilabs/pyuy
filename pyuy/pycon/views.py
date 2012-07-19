# Create your views here.
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from forms import ProposalForm
from symposion.proposals.models import Proposal

def index(request):
    return render_to_response('index.html')

def proposal_add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ProposalForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            kind =  form.cleaned_data['kind']
            category =  form.cleaned_data['category']
            extreme =  form.cleaned_data['extreme']
            duration =  form.cleaned_data['duration']
            abstract = form.cleaned_data['abstarct']
            audience_level = form.cleaned_data['audience_level']
            additional_notes = form.cleaned_data['additional_notes']

            #Me falta capturar los speaker
            #Proposal.objects.create(title, description, kind, category, abstract, audience_level, additional_notes, extreme, duration, datetime.datetime.now, False)
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ProposalForm() # An unbound form

    return render_to_response('proposal_add.html', {
        'form': form,
        })