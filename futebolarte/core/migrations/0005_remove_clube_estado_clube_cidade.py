# Generated by Django 5.0.2 on 2024-03-04 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comum', '0001_initial'),
        ('core', '0004_clube_cores_alter_clube_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clube',
            name='estado',
        ),
        migrations.AddField(
            model_name='clube',
            name='cidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clubes', to='comum.cidade'),
        ),
    ]