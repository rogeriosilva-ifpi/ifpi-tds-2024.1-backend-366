# Generated by Django 5.0.2 on 2024-04-10 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_professor'),
        ('treinos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treinos', to='cadastro.aluno')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treinos', to='cadastro.professor')),
            ],
        ),
        migrations.CreateModel(
            name='ItemItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.PositiveIntegerField()),
                ('repeticoes', models.PositiveIntegerField()),
                ('exercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treinos.exercicio')),
                ('treino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='treinos.treino')),
            ],
        ),
    ]
