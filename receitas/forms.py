from django import forms
from django.utils.text import slugify
from .models import Categoria, Receita


class CategoriaForm(forms.ModelForm):
    slug = forms.SlugField(
        required=False,
        label="Slug / URL",
        help_text="Se ficar vazio, será gerado automaticamente.",
        widget=forms.TextInput(attrs={
            "placeholder": "Pode deixar vazio para gerar automaticamente"
        })
    )

    class Meta:
        model = Categoria
        fields = ["nome", "slug", "ordem"]
        widgets = {
            "nome": forms.TextInput(attrs={
                "placeholder": "Ex.: Sobremesas"
            }),
            "ordem": forms.NumberInput(attrs={"min": 1}),
        }

    def clean_slug(self):
        slug = (self.cleaned_data.get("slug") or "").strip()

        if not slug:
            slug = slugify(self.cleaned_data.get("nome", ""))

        if not slug:
            raise forms.ValidationError(
                "Informe um nome que permita gerar uma URL."
            )

        qs = Categoria.objects.filter(slug=slug)

        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError(
                "Já existe uma categoria com esta URL. Escolha outra."
            )

        return slug


class ReceitaForm(forms.ModelForm):
    slug = forms.SlugField(
        required=False,
        label="Slug / URL",
        help_text="Se ficar vazio, será gerado automaticamente.",
        widget=forms.TextInput(attrs={
            "placeholder": "Pode deixar vazio para gerar automaticamente"
        })
    )

    class Meta:
        model = Receita
        fields = [
            "titulo",
            "slug",
            "tempo_preparo",
            "ingredientes",
            "modo_preparo",
            "imagem",
            "categoria",
            "destaque"
        ]
        widgets = {
            "titulo": forms.TextInput(attrs={
                "placeholder": "Nome da receita"
            }),
            "tempo_preparo": forms.TextInput(attrs={
                "placeholder": "Ex.: 30 min"
            }),
            "ingredientes": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": "Um ingrediente por linha"
            }),
            "modo_preparo": forms.Textarea(attrs={
                "rows": 6,
                "placeholder": "Explique o preparo por etapas"
            }),
        }

    def clean_slug(self):
        slug = (self.cleaned_data.get("slug") or "").strip()

        if not slug:
            slug = slugify(self.cleaned_data.get("titulo", ""))

        if not slug:
            raise forms.ValidationError(
                "Informe um título que permita gerar uma URL."
            )

        qs = Receita.objects.filter(slug=slug)

        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError(
                "Já existe uma receita com esta URL. Escolha outra."
            )

        return slug