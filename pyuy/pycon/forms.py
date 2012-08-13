from django import forms
from symposion.proposals.models import PresentationCategory, PresentationKind, Proposal
from symposion.speakers.models import Speaker
from bootstrap.forms import BootstrapForm

class SpeakerForm(BootstrapForm):

    biography = forms.CharField(widget=forms.Textarea)
    annotation = forms.CharField(widget=forms.Textarea)

class ProposalForm(BootstrapForm):

    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    kind = forms.ModelChoiceField(PresentationKind.objects.all().order_by('name'))
    category = forms.ModelChoiceField(PresentationCategory.objects.all().order_by('name'))
    abstract = forms.CharField(widget=forms.Textarea)
    audience_level = forms.ChoiceField(choices=Proposal.AUDIENCE_LEVELS)
    additional_notes = forms.CharField(widget=forms.Textarea(), required=False)
    extreme = forms.BooleanField(required=False)
    duration = forms.ChoiceField(choices=Proposal.DURATION_CHOICES)
    #additional_speakers = forms.ModelChoiceField(Speaker.objects.all().order_by('name'), required=False)