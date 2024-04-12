import re
from django import forms
from django.core.exceptions import ValidationError


class NewCustomerForm(forms.Form):
    name = forms.CharField(max_length=255, required=True, label='Имя', help_text='Имя'),
    phone = forms.IntegerField(required=True, label='Телефон', help_text='Телефон'),

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if re.match(pattern='7\d{10}$', string=phone) is None:
            raise ValidationError(message='Некорректный формат телефона')

        return phone
