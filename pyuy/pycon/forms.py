from django import forms
from symposion.proposals.models import PresentationCategory, PresentationKind, Proposal
from symposion.speakers.models import Speaker
from bootstrap.forms import BootstrapForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError("This email address is already in use. Please supply a different email address.")
        return self.cleaned_data['email']

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self):
        user = super(UserCreateForm, self).save()
        user.email = self.cleaned_data["email"]
        return user

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


class ProfileForm(BootstrapForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField()
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('Email addresses must be unique.')
        return email

class PasswordForm(PasswordChangeForm):
    pass

class PassResetForm(PasswordResetForm):
    pass

