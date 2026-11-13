from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Contato",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100, verbose_name="Nome")),
                ("email", models.EmailField(max_length=254, verbose_name="E-mail")),
                ("mensagem", models.TextField(verbose_name="Mensagem")),
                ("data_envio", models.DateTimeField(auto_now_add=True, verbose_name="Data de envio")),
            ],
            options={"verbose_name": "Mensagem de contato", "verbose_name_plural": "Mensagens de contato", "ordering": ["-data_envio"]},
        ),
    ]
