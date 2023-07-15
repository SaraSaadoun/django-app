from django import forms
from .models import Login

# disable = True --u can't type in
# help_text="val"
# required = !blank
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=50, label="username", initial='enter username')
#     password = forms.CharField(max_length=50, label="password", widget=forms.PasswordInput)


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__' # ['username', 'password']