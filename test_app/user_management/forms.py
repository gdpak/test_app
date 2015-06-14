from django.forms import ModelForm

from user_management.models import UserInformation


class UserInformationForm(ModelForm):
    class Meta:
        model  = UserInformation
        fields = ['first_name', 'last_name', 'IBAN_account']
