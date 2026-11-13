from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label="E-mail", required=True)
    first_name = forms.CharField(label="Nome", max_length=150, required=True)
    last_name = forms.CharField(label="Sobrenome", max_length=150, required=False)

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ("username", "first_name", "last_name", "email", "sexo", "data_nascimento")
        widgets = {"data_nascimento": forms.DateInput(attrs={"type": "date"})}

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if Usuario.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Já existe uma conta cadastrada com este e-mail.")
        return email


class UsuarioAdminForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ("username", "first_name", "last_name", "email", "sexo", "data_nascimento", "is_active")
        widgets = {"data_nascimento": forms.DateInput(attrs={"type": "date"})}
