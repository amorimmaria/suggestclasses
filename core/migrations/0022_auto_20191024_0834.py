# Generated by Django 2.1.7 on 2019-10-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20191003_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacaocurricular',
            name='id_curriculo_componente',
            field=models.IntegerField(),
        ),
    ]
