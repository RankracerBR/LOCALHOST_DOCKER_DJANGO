# Generated by Django 4.1.5 on 2023-09-17 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete_name', models.CharField(default=None, max_length=80)),
                ('complete_email', models.EmailField(max_length=254)),
                ('complete_password', models.CharField(default=None, max_length=20)),
            ],
        ),
    ]
