from django.contrib.auth import forms as aforms
from bootstrap.forms import BootstrapMixin, BootstrapModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class AuthenticationForm(BootstrapMixin, aforms.AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "E-mail"

class PasswordResetForm(BootstrapMixin, aforms.PasswordResetForm):
    pass

class SetPasswordForm(BootstrapMixin, aforms.SetPasswordForm):
    pass

class PasswordChangeForm(BootstrapMixin, aforms.PasswordChangeForm):
    pass

class UserCreateForm(UserCreationForm):
    username = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

class ProfileForm(BootstrapModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')