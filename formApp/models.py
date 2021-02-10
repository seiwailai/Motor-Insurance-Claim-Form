from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime


# Create your models here.
class Claims(models.Model):
    class Meta:
        verbose_name_plural = "Claims"

    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    mobile_number = PhoneNumberField(blank=False)
    year_choices = ((x, x) for x in range(1950, datetime.now().year + 1))
    vehicle_year_make = models.IntegerField(choices=year_choices)
    vehicle_model = models.CharField(max_length=100, blank=False)
    vehicle_number = models.CharField(max_length=100, blank=False)
    accident_datetime = models.DateTimeField(blank=False)
    location = models.CharField(max_length=100, blank=False)
    loss_type_choices = (
        ('Own Damage', 'Own Damage'),
        ('Knock for Knock', 'Knock for Knock'), 
        ('Windscreen Damage', 'Windscreen Damage'),
        ('Theft', 'Theft')
    )
    loss_type = models.CharField(max_length=17, choices=loss_type_choices, blank=False)
    loss_description = models.TextField(max_length=1000, blank=False)
    yes_no_choices = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    police_report_lodged = models.CharField(max_length=3, choices=yes_no_choices, blank=False)
    anybody_injured = models.CharField(max_length=3, choices=yes_no_choices, blank=False)
    photo = models.ImageField(upload_to='photos/', blank=False)
    pdf_document = models.FileField(upload_to='pdfs/', blank=False)
    claim_progress_choices = (
        ('In Progress', 'In Progress'),
        ('Accepted', 'Accepted')
    )
    claim_progress = models.CharField(max_length=11, choices=claim_progress_choices, default='In Progress')


    def __str__(self):
        return self.vehicle_number + ' by ' + self.name + ' ' + str(self.pk)
