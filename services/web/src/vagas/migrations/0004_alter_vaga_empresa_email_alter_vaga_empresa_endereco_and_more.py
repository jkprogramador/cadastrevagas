# Generated by Django 4.0.2 on 2022-02-24 23:13

import django.core.validators
from django.db import migrations, models
import vagas.models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0003_vaga_data_hora_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='empresa_email',
            field=models.EmailField(blank=True, error_messages={'invalid': 'O campo Email da empresa deve conter um email válido.'}, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='empresa_endereco',
            field=models.CharField(blank=True, error_messages={'max_length': 'O campo Endereço da empresa pode conter no máximo %(limit_value)s caracteres.'}, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='empresa_nome',
            field=models.CharField(error_messages={'blank': 'O campo Nome da empresa é obrigatório.', 'max_length': 'O campo Nome da empresa pode conter no máximo %(limit_value)s caracteres.'}, max_length=100),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='empresa_site',
            field=models.URLField(error_messages={'blank': 'O campo Site da empresa é obrigatório.', 'invalid': 'O campo Site da empresa deve conter um endereço web válido.'}),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='empresa_telefone_celular',
            field=vagas.models.TelefoneField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(code='invalid', message='O campo Telefone celular da empresa deve conter um número válido. Ex.: (DDD) 99999-9999', regex='^\\(\\d{2}\\) 9\\d{4}-\\d{4}$')]),
        ),
    ]
