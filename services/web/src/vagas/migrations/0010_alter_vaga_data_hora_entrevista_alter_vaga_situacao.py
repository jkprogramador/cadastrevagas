# Generated by Django 4.0.2 on 2022-03-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0009_vaga_data_hora_atualizacao_alter_vaga_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='data_hora_entrevista',
            field=models.DateTimeField(blank=True, error_messages={'invalid': 'O campo Data e horário da entrevista deve conter uma data e horário válidos. Ex.: dia/mês/ano horas:minutos', 'invalid_datetime': 'O campo Data e horário da entrevista deve conter uma data e horário válidos. Ex.: dia/mês/ano horas:minutos'}, null=True),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='situacao',
            field=models.CharField(choices=[(None, 'Todas'), ('W', 'Aguardando retorno'), ('S', 'Entrevista agendada'), ('R', 'Rejeitado')], default='W', error_messages={'blank': 'O campo Situação é obrigatório.', 'invalid_choice': 'O campo Situação contém um valor inválido.'}, max_length=1),
        ),
    ]
