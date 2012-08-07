from django import forms
from symposion.proposals.models import PresentationCategory, PresentationKind, Proposal
from symposion.speakers.models import Speaker
from bootstrap.forms import BootstrapForm, BootstrapModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
    username = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

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
    additional_speakers = forms.ModelChoiceField(Speaker.objects.all().order_by('name'), required=False)


class ProfileForm(BootstrapModelForm):
    class Meta:
        model=User
        fields = ('username', 'first_name', 'last_name')

    def clean_username(self):
        username = self.cleaned_data['username']
        user = self.instance
        if username != user.username and User.objects.filter(username=username).count() > 0:
            raise forms.ValidationError(u'%s already exists' % username)
        return username


class PasswordForm(PasswordChangeForm):
    pass

class PassResetForm(PasswordResetForm):
    pass

