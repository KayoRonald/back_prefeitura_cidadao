# Generated by Django 5.0 on 2024-08-02 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Autorizacao_de_Estagio_Supervisionado",
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
                ("descricao", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Autorizacao_para_Pesquisa_CREI_Escola",
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
                ("descricao", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Furto_Extravio_ou_Perda_de_Equipamentos",
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
                ("descricao", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Solicitacao_de_Espaco_Fisico_Escola_CREI",
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
                ("descricao", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Solicitacao_Diversa",
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
                ("descricao", models.TextField()),
            ],
        ),
    ]
