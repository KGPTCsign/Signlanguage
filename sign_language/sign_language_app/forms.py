from django.forms import ModelForm

from sign_language_app.models import * 


class UserForm(ModelForm):
    class Meta:
        model=UserTable
        fields='__all__'