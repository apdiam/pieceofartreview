from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)

    def __int__(self):
        self.fields['password1'].required = False
        self.fields['password2'].required = False

    def save(self):
        user = super(UserCreationForm, self).save(commit=False)
        clean_username = self.cleaned_date["username"]
        user.username = clean_username
        if commit:
            user.save()
        custom_user = CustomUser()
        custom_user.id = user
        custom_user.save()
        return user


