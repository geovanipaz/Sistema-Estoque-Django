# Generated by Django 4.0.6 on 2022-07-19 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque_gerencia', '0002_categoria_alter_estoque_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='estoque_gerencia.categoria'),
            preserve_default=False,
        ),
    ]