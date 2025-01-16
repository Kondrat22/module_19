from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, required=True, label='Введите логин: ')
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, required=True, label='Введите пароль: ')
    repeat_password = forms.CharField(widget=forms.PasswordInput(), min_length=8, required=True,
                                      label='Повторите пароль: ')
    age = forms.IntegerField(max_value=100, min_value=1)