from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

GENDER = (
    ('М', 'Мужчина'),
    ('Ж', 'Женщина')
)

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, initial='+996')
    date_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER, required=True)

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'phone_number',
            'date_birth',
            'gender'
        )
    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.gender = self.cleaned_data['gender']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user