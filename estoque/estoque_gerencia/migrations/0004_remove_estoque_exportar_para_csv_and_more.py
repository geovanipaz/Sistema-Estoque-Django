# Generated by Django 4.0.6 on 2022-07-19 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque_gerencia', '0003_alter_estoque_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estoque',
            name='exportar_para_CSV',
        ),
        migrations.AlterField(
            model_name='estoque',
            name='categoria',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='estoque_gerencia.categoria'),
        ),
    ]
