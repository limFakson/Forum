import re
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['matricNumber', 'Department', 'faculty', 'profile_picture']
        widgets = {
            'matricNumber': forms.TextInput(attrs={'placeholder': 'DEPT/XX/XXXX',
                                                   'class': 'shadow '}),
            'Department': forms.TextInput(attrs={'class': 'shadow '}),
            'faculty': forms.Select(attrs={'class': 'shadow '}),
            'profile_picture': forms.FileInput(attrs={'class': 'shadow '}),
        }

    def clean_matricNumber(self):
        matricNumber = self.cleaned_data.get('matricNumber')
        pattern = re.compile(r'^[a-z,A-Z][a-z,A-Z][a-z,A-Z]/[0-9][0-9]/[0-9][0-9][0-9][0-9]$')
        if not pattern.match(matricNumber):
            raise forms.ValidationError('Invalid matric number format. Example format: EXX/19/1201')
        return matricNumber
