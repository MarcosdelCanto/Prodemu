from django import forms

class crearNombreCliente(forms.Form):
    nombre_cli = forms.CharField(label=False)

class crearEmailCliente(forms.Form):
    email_cli = forms.EmailField(label=False)

class crearPasswordCliente(forms.Form):
    password_cli = forms.CharField(label=False, widget=forms.PasswordInput)