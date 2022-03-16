# Generated by Django 4.0.2 on 2022-03-16 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0007_vaga_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='situacao',
            field=models.CharField(choices=[('W', 'Aguardando retorno'), ('S', 'Entrevista agendada'), ('R', 'Rejeitado')], default='W', max_length=1),
        ),
    ]
