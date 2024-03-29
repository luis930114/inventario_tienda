# Generated by Django 5.0.3 on 2024-03-14 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_alter_movimiento_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ajuste',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='ajuste',
            name='movimiento',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.movimiento'),
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='tipo',
            field=models.CharField(choices=[('Entrada', 'Entrada'), ('Salida', 'Salida')], max_length=50),
        ),
    ]
