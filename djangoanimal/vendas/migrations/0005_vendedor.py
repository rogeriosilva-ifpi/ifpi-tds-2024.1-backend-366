# Generated by Django 5.0.2 on 2024-02-26 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0004_alter_produto_habilitado_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
    ]
