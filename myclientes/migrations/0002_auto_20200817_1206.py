# Generated by Django 2.1.5 on 2020-08-17 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myclientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
