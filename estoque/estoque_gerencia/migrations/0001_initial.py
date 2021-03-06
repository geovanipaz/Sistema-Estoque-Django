# Generated by Django 4.0.6 on 2022-07-15 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(blank=True, max_length=50, null=True)),
                ('item_nome', models.CharField(blank=True, max_length=50, null=True)),
                ('quantidade', models.IntegerField(blank=True, default='0', null=True)),
                ('quantidade_recebida', models.IntegerField(blank=True, default='0', null=True)),
                ('recebida_por', models.CharField(blank=True, max_length=50, null=True)),
                ('quantidade_emitida', models.IntegerField(blank=True, default='0', null=True)),
                ('emitida_por', models.CharField(blank=True, max_length=50, null=True)),
                ('emitida_para', models.CharField(blank=True, max_length=50, null=True)),
                ('telefone', models.CharField(blank=True, max_length=50, null=True)),
                ('criada_por', models.CharField(blank=True, max_length=50, null=True)),
                ('nivel_reabastecimento', models.IntegerField(blank=True, default='0', null=True)),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
                ('exportar_para_CSV', models.BooleanField(default=False)),
            ],
        ),
    ]
