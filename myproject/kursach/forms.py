from django import forms


class RegForm(forms.Form):
    username = forms.CharField(min_length=2, max_length=40, label="Введите логин")
    email = forms.EmailField(min_length=2, max_length=40, label="Введите почту")
    password = forms.CharField(min_length=2, max_length=30, widget = forms.PasswordInput, label="Введите пароль")
    password1 = forms.CharField(min_length=2, max_length=30, widget = forms.PasswordInput, label="Повторите пароль")

class LogForm(forms.Form):
    username = forms.CharField(min_length=2, max_length=40, label="Введите логин")
    password = forms.CharField(min_length=2, max_length=30, widget=forms.PasswordInput, label="Введите пароль")

class searchpr(forms.Form):
    pr = forms.CharField(min_length=1, max_length=100, label="Введите наименование товара")

class ExpertForm(forms.Form):
    product1mark = forms.IntegerField()
    product2mark = forms.IntegerField()
    product3mark = forms.IntegerField()