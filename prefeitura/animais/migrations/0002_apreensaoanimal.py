# Generated by Django 5.0 on 2024-08-08 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animais", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ApreensaoAnimal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rua", models.CharField(max_length=200)),
                ("numero", models.IntegerField(default=0)),
                ("bairro", models.CharField(max_length=200)),
                ("estado", models.CharField(max_length=200)),
                ("cidade", models.CharField(max_length=200)),
                ("cep", models.CharField(max_length=200)),
                ("pontoRef", models.CharField(blank=True, max_length=200)),
                (
                    "animal_de_grande_porte",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Cavalo", "Cavalo"),
                            ("Boi", "Boi"),
                            ("Cabra", "Cabra"),
                            ("Porco", "Porco"),
                        ],
                        max_length=6,
                    ),
                ),
                ("observacoes", models.CharField(blank=True, max_length=200)),
                ("telefone", models.CharField(max_length=20)),
            ],
        ),
    ]