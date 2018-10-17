# Generated by Django 2.1.2 on 2018-10-16 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('dolar_dia', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True)),
            ],
            options={
                'verbose_name': 'nota',
                'verbose_name_plural': 'notas',
                'ordering': ('date', 'description'),
            },
        ),
        migrations.CreateModel(
            name='NotaItens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('valor_usd', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('maquina_pt', models.CharField(max_length=255)),
                ('maquina_en', models.CharField(blank=True, max_length=255, null=True)),
                ('maquina_ch', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_pt', models.CharField(max_length=255)),
                ('tipo_en', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_ch', models.CharField(blank=True, max_length=255, null=True)),
                ('modelo_pt', models.CharField(max_length=255)),
                ('modelo_en', models.CharField(blank=True, max_length=255, null=True)),
                ('modelo_ch', models.CharField(blank=True, max_length=255, null=True)),
                ('area_trabalho_pt', models.CharField(max_length=255)),
                ('area_trabalho_en', models.CharField(blank=True, max_length=255, null=True)),
                ('area_trabalho_ch', models.CharField(blank=True, max_length=255, null=True)),
                ('eixo_z_pt', models.CharField(max_length=255)),
                ('eixo_z_en', models.CharField(blank=True, max_length=255, null=True)),
                ('eixo_z_ch', models.CharField(blank=True, max_length=255, null=True)),
                ('cor_pt', models.CharField(max_length=255)),
                ('cor_en', models.CharField(blank=True, max_length=255, null=True)),
                ('cor_ch', models.CharField(blank=True, max_length=255, null=True)),
                ('faz_pt', models.TextField()),
                ('faz_en', models.TextField(blank=True, null=True)),
                ('faz_ch', models.TextField(blank=True, null=True)),
                ('voltagem_pt', models.CharField(max_length=10)),
                ('voltagem_en', models.CharField(blank=True, max_length=10, null=True)),
                ('voltagem_ch', models.CharField(blank=True, max_length=10, null=True)),
                ('ncm', models.CharField(max_length=20)),
                ('nome_classificacao', models.TextField(blank=True, null=True)),
                ('caixa_lateral_base', models.CharField(blank=True, max_length=255, null=True)),
                ('opcionais', models.TextField(blank=True, null=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='products/')),
            ],
            options={
                'verbose_name': 'máquina',
                'verbose_name_plural': 'máquinas',
                'ordering': ('maquina_pt',),
            },
        ),
        migrations.AddField(
            model_name='notaitens',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notas.Product'),
        ),
        migrations.AddField(
            model_name='notaitens',
            name='nota',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notas.Nota'),
        ),
    ]