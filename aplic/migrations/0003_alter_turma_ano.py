# Generated by Django 4.2.6 on 2023-10-17 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0002_rename_serie_turma_ano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='ano',
            field=models.CharField(default='9º ano', verbose_name='Ano'),
        ),
    ]
