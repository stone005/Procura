# Generated by Django 2.0.5 on 2018-07-13 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratiche', '0002_auto_20180712_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='AG_matricola',
            field=models.PositiveIntegerField(),
        ),
    ]
