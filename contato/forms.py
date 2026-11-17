from django import forms
from .models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ["nome", "email", "mensagem"]
        widgets = {
            "nome": forms.TextInput(attrs={"placeholder": "Seu nome"}),
            "email": forms.EmailInput(attrs={"placeholder": "seu@email.com"}),
            "mensagem": forms.Textarea(attrs={"rows": 5, "placeholder": "Escreva sua mensagem"}),
        }
