# Generated by Django 4.0.2 on 2022-02-11 19:55

from django.db import migrations
import vagas.models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='empresa_telefone_celular',
            field=vagas.models.TelefoneField(max_length=11),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='empresa_telefone_comercial',
            field=vagas.models.TelefoneField(max_length=10),
        ),
    ]
