# Generated by Django 2.2.7 on 2019-11-24 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_docente_turma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='siape',
            field=models.IntegerField(unique=True),
        ),
    ]
