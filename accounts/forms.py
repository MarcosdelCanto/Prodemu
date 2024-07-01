from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Requerido. Ingresa una dirección de correo electrónico válida.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("El nombre de usuario ya está en uso. Por favor, elige otro.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("username")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo electrónico ya está en uso. Por favor, elige otro.")
        return email

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user