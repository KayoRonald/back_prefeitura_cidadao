# Generated by Django 5.1.1 on 2024-09-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("seguranca", "0005_denuncie_aqui_observacoes"),
    ]

    operations = [
        migrations.AddField(
            model_name="palestras_para_instituicoes_de_ensino",
            name="status",
            field=models.TextField(default="ABERTO", max_length=30),
        ),
    ]