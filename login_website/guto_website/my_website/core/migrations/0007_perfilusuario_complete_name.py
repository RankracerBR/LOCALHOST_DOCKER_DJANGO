# Generated by Django 4.1.5 on 2023-10-04 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_perfilusuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuario',
            name='complete_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='perfil_usuario', to='core.cadastrousuario'),
        ),
    ]
