# Generated by Django 2.1.5 on 2019-02-02 03:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponenteCurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nome', models.CharField(max_length=200)),
                ('ementa', models.CharField(max_length=200)),
                ('departamento', models.CharField(max_length=200)),
                ('carga_horaria', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EstruturaCurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizacaoCurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.IntegerField()),
                ('obrigatoria', models.BooleanField()),
                ('componente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.ComponenteCurricular')),
                ('estrutura', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.EstruturaCurricular')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
