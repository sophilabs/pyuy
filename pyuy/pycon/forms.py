from django import forms
from symposion.proposals.models import PresentationCategory, PresentationKind, Proposal
from bootstrap.forms import BootstrapForm


class ProposalForm(BootstrapForm):
    title = forms.CharField(max_length=100)
    description = forms.CharField()
    kind = forms.ModelChoiceField(PresentationKind.objects.all().order_by('name'))
    category = forms.ModelChoiceField(PresentationCategory.objects.all().order_by('name'))
    absctract = forms.CharField(widget=forms.Textarea())
    audience_level = forms.ChoiceField(choices=Proposal.AUDIENCE_LEVELS)
    aditional_notes = forms.CharField(widget=forms.Textarea())
    extreme = forms.BooleanField()
    duration = forms.ChoiceField(choices=Proposal.DURATION_CHOICES)

