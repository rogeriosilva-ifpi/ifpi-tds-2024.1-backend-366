<<<<<<< HEAD
# Generated by Django 5.0.6 on 2024-07-08 20:28
=======
# Generated by Django 5.0.2 on 2024-07-10 18:04
>>>>>>> 6be5c1bc3f4c4c87de31d30b744723fedcabb4a9

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('sigla', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('nome', models.CharField(max_length=200)),
=======
                ('nome', models.CharField(max_length=128)),
>>>>>>> 6be5c1bc3f4c4c87de31d30b744723fedcabb4a9
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cidades', to='core.estado')),
            ],
        ),
    ]
