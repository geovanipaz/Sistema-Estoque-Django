# Generated by Django 4.0.6 on 2022-07-19 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque_gerencia', '0004_remove_estoque_exportar_para_csv_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque',
            name='criado',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
