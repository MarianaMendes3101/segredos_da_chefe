
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

Usuario = get_user_model()


class EmailAuthenticationForm(AuthenticationForm):

    username = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(
            attrs={
                "autofocus": True,
                "placeholder": "Digite seu e-mail",
            }
        )
    )

    def clean(self):
        email = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if email and password:
            try:
                usuario = Usuario.objects.get(email__iexact=email)
            except Usuario.DoesNotExist:
                raise forms.ValidationError(
                    "E-mail ou senha incorretos."
                )
            except Usuario.MultipleObjectsReturned:
                raise forms.ValidationError(
                    "Este e-mail está associado a mais de uma conta."
                )

            self.cleaned_data["username"] = usuario.get_username()

        return super().clean()
