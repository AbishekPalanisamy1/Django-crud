from django import forms 
from accounts.models import Accounts


class AccountForm(forms.ModelForm):
    class Meta:
        model=Accounts
        fields='__all__'