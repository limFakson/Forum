import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    firstname = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'placeholder': 'Firstname', 'class': 'custom-input name'}))
    lastname = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'placeholder': 'Lastname', 'class': 'custom-input name'}))
    username = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'custom-input'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'custom-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'custom-input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'custom-input'}))

    class Meta:
        model = User
        fields = ['firstname', 'lastname','username', 'email', 'password1', 'password2']

        def clean(self):
            cleaned_data = super().clean()
            username = cleaned_data.get('username')
            firstname = cleaned_data.get('firstname')
            lastname = cleaned_data.get('lastname')
            email = cleaned_data.get('email')

            if User.objects.filter(username=username).exists():
                self.add_error('username', 'Username already exists.')
            if UserProfile.objects.filter(firstname=firstname).exists():
                self.add_error('firstname', 'Firstname already exists.')
            if UserProfile.objects.filter(lastname=lastname).exists():
                self.add_error('lastname', 'Lastname already exists.')
            if UserProfile.object.filter(email=email).exists():
                self.add_error('email', 'Email is associated to another user.')

            return cleaned_data


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['matricNumber', 'Department', 'faculty', 'profile_picture']
        widgets = {
            'matricNumber': forms.TextInput(attrs={'placeholder': 'DEPT/XX/XXXX', 'class': 'custom-input'}),
            'Department': forms.TextInput(attrs={'placeholder': 'Department', 'class': 'custom-input'}),
            'faculty': forms.Select(attrs={'placeholder': 'Faculty', 'class': 'custom-input'}),
            'profile_picture': forms.FileInput(attrs={'class': 'custom-input'}),
            'user': forms.HiddenInput()
        }

    def clean_matricNumber(self):
        matricNumber = self.cleaned_data.get('matricNumber')
        pattern = re.compile(r'^[a-z,A-Z][a-z,A-Z][a-z,A-Z]/[0-9][0-9]/[0-9][0-9][0-9][0-9]$')
        if not pattern.match(matricNumber):
            raise forms.ValidationError('Invalid matric number format. Example format: EXX/19/1201')
        if UserProfile.objects.filter(matricNumber=matricNumber).exists():
            raise forms.ValidationError('matic number is associated with another user.')
        return matricNumber
