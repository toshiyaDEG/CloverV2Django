# Generated by Django 3.2.7 on 2021-10-18 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0002_alter_materia_materia'),
        ('subir_tarea', '0008_auto_20211013_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='materia_tarea',
            field=models.ForeignKey(default='LM', on_delete=django.db.models.deletion.CASCADE, related_name='materia_tarea', to='materias.materia'),
        ),
    ]
