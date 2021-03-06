# Generated by Django 4.0.6 on 2022-07-21 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque_gerencia', '0005_estoque_criado'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricoEstoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('ultima_atualizacao', models.DateTimeField(null=True)),
                ('criado', models.DateTimeField(null=True)),
                ('categoria', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='estoque_gerencia.categoria')),
            ],
        ),
    ]
