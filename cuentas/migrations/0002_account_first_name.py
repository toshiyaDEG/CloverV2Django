# Generated by Django 3.2.7 on 2021-10-15 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(default='nombre', max_length=30),
        ),
    ]