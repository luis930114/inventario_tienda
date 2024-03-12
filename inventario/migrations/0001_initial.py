# Generated by Django 5.0.3 on 2024-03-12 05:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MotivoAjuste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.CharField(max_length=100)),
                ('almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.almacen')),
            ],
        ),
        migrations.CreateModel(
            name='Ajuste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('motivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.motivoajuste')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.almacen')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='ubicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.ubicacion'),
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('tipo', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimientos_destino', to='inventario.ubicacion')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimientos_origen', to='inventario.ubicacion')),
            ],
        ),
    ]
