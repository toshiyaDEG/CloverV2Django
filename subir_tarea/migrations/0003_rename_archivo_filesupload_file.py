# Generated by Django 3.2.7 on 2021-10-12 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subir_tarea', '0002_auto_20211012_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filesupload',
            old_name='archivo',
            new_name='file',
        ),
    ]
