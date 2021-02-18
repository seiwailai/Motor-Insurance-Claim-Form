from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User
from .models import Claims
from django.forms.widgets import (
    TextInput, 
    NumberInput, 
    EmailInput,
    DateTimeInput,
    ClearableFileInput,
    Select,
    Textarea,
    PasswordInput
)
from django.utils.translation import gettext_lazy as _
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from django.contrib.auth import authenticate


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class':'form-control mb-2', 'placeholder': 'Password'})
        self.fields['password2'].widget = PasswordInput(attrs={'class':'form-control mb-2', 'placeholder': 'Confirm Password'})
        self.fields['username'].widget = TextInput(attrs={'class':'form-control mb-2', 'placeholder': 'Username'})
        self.fields['password1'].label = _('Password')
        self.fields['password1'].label = _('Confirm Password')


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(LoginForm, self).__init__(request, *args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Username', 'id':'username'})
        self.fields['password'].widget = PasswordInput(attrs={'class': 'form-control mb-2','placeholder': 'Password','id': 'password'})


class ClaimsForm(ModelForm):    
    class Meta:
        model = Claims
        fields = [
            'name',
            'email',
            'mobile_number',
            'vehicle_year_make',
            'vehicle_model',
            'vehicle_number',
            'accident_datetime',
            'location',
            'loss_type',
            'loss_description',
            'police_report_lodged',
            'anybody_injured',
            'photo',
            'pdf_document',
        ]
        labels = {
            'name': _('Full Name'),
            'email': _('Email'),
            'mobile_number': _('Mobile Phone Number'),
            'vehicle_year_make': _('Vehicle Year Make'),
            'vehicle_model': _('Vehicle Model'),
            'vehicle_number': _('Vehicle Number'),
            'accident_datetime': _('Datetime of Accident'),
            'location': _('Accident Location'),
            'loss_type': _('Types of Loss'),
            'loss_description': _('Description of Loss'),
            'police_report_lodged': _('Police Report Lodged?'),
            'anybody_injured': _('Anybody Injured?'),
            'photo': _('Photos'),
            'pdf_document': _('PDF Documents of Insurance Cover'),
        }
        widgets = {
            'name': TextInput(attrs={'class':'form-control mb-2', 'placeholder': 'Full Name'}),
            'email': EmailInput(attrs={'class':'form-control mb-2', 'placeholder': 'Email'}),
            'mobile_number': PhoneNumberInternationalFallbackWidget(attrs={'class':'form-control mb-2', 'placeholder': 'Mobile Phone Number'}),
            'vehicle_year_make': Select(attrs={'class':'form-control mb-2', 'placeholder': 'Vehicle Year Make'}),
            'vehicle_model': TextInput(attrs={'class':'form-control mb-2', 'placeholder': 'Vehicle Model'}),
            'vehicle_number': TextInput(attrs={'class':'form-control mb-2', 'placeholder': 'Vehicle Number'}),
            'accident_datetime': DateTimeInput(attrs={'class':'form-control mb-2', 'placeholder': 'Datetime of Accident', 'type': 'datetime-local'}, format='%Y-%m-%d'+'T'+'%H:%M'),
            'location': TextInput(attrs={'class':'form-control mb-2', 'placeholder': 'Accident Location'}),
            'loss_type': Select(attrs={'class':'form-control mb-2', 'placeholder': 'Types of Loss'}),
            'loss_description': Textarea(attrs={'class':'form-control mb-2', 'placeholder': 'Description of Loss'}),
            'police_report_lodged': Select(attrs={'class':'form-control mb-2', 'placeholder': 'Police Report Lodged?'}),
            'anybody_injured': Select(attrs={'class':'form-control mb-2', 'placeholder': 'Anybody Injured?'}),
            'photo': ClearableFileInput(attrs={'class':'form-control-file mb-2', 'placeholder': 'Photos', 'type': 'file'}),
            'pdf_document': ClearableFileInput(attrs={'class':'form-control-file mb-2', 'placeholder': 'PDF Documents of Insurance Cover', 'type': 'file', 'accept':'application/pdf'})
        }