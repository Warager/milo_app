from django import forms
from milo_task.account.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'birthday', 'random')