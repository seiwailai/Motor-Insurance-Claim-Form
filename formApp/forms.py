from django.forms import ModelForm
from .models import Claims
from django.forms.widgets import (
    TextInput, 
    NumberInput, 
    EmailInput,
    DateTimeInput,
    ClearableFileInput,
    Select,
    Textarea
)
from django.utils.translation import gettext_lazy as _
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from django.forms.utils import ErrorList
from django.forms.models import apply_limit_choices_to_to_formfield, model_to_dict


# def convert_datetime_to_html_readable_value(datetime):



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
            'pdf_document': ClearableFileInput(attrs={'class':'form-control-file mb-2', 'placeholder': 'PDF Documents of Insurance Cover', 'type': 'file'})
        }