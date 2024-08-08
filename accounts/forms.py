from django import forms
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        fields = ('username', 'email')

        def clean_confirm_password(self):
            password = self.cleaned_data.get('password')
            confirm_password = self.cleaned_data.get('confirm_password')
            if password == confirm_password and password != confirm_password:
                raise ValidationError('Password dont match')
            return confirm_password

        def save(self, commit=False):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user