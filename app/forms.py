from django import forms
from .models import Profile, Post
from allauth.account.forms import SignupForm


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'info')


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'text', 'image')


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user