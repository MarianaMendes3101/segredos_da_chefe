from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

Usuario = get_user_model()


# Cadastro feito pelo próprio cliente
class CadastroForm(UserCreationForm):
    email = forms.EmailField(label="E-mail")
    first_name = forms.CharField(label="Nome", max_length=150)
    last_name = forms.CharField(label="Sobrenome", max_length=150, required=False)

    class Meta:
        model = Usuario
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "sexo",
            "data_nascimento",
        ]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if Usuario.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        return email


# Cadastro de usuários feito pelo administrador
class UsuarioAdminForm(CadastroForm):
    is_staff = forms.BooleanField(
        label="É administrador?",
        required=False
    )

    class Meta(CadastroForm.Meta):
        fields = CadastroForm.Meta.fields + ["is_staff"]


# Edição de usuários pelo administrador
class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "sexo",
            "data_nascimento",
            "is_staff",
            "is_active",
        ]

    def clean_email(self):
        email = self.cleaned_data["email"]
        usuarios = Usuario.objects.filter(email__iexact=email)
        if self.instance.pk:
            usuarios = usuarios.exclude(pk=self.instance.pk)
        if usuarios.exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        return email


# Formulário de login
from django.contrib.auth.forms import AuthenticationForm


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={
            "autofocus": True,
            "placeholder": "Digite seu e-mail"
        })
    )

    def clean(self):
        email = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if email and password:
            try:
                usuario = Usuario.objects.get(email__iexact=email)
                self.cleaned_data["username"] = usuario.get_username()
            except Usuario.DoesNotExist:
                raise forms.ValidationError("E-mail ou senha incorretos.")
            except Usuario.MultipleObjectsReturned:
                raise forms.ValidationError(
                    "Este e-mail está associado a mais de uma conta."
                )

        return super().clean()
