from django.db import migrations


def criar_categorias(apps, schema_editor):
    Categoria = apps.get_model("receitas", "Categoria")
    categorias = [
        ("Café da manhã", "cafe-da-manha", 1),
        ("Almoço ou jantar", "almoco-ou-jantar", 2),
        ("Lanches", "lanches", 3),
        ("Sobremesas", "sobremesas", 4),
    ]
    for nome, slug, ordem in categorias:
        Categoria.objects.using(schema_editor.connection.alias).get_or_create(
            slug=slug, defaults={"nome": nome, "ordem": ordem}
        )


def remover_categorias(apps, schema_editor):
    Categoria = apps.get_model("receitas", "Categoria")
    Categoria.objects.using(schema_editor.connection.alias).filter(
        slug__in=["cafe-da-manha", "almoco-ou-jantar", "lanches", "sobremesas"]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [("receitas", "0001_initial")]
    operations = [migrations.RunPython(criar_categorias, migrations.RunPython.noop)]
