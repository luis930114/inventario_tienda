from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Ajuste

@receiver(pre_save, sender=Ajuste)
def validar_ajuste(sender, instance, **kwargs):
    if instance.movimiento:
        movimiento = instance.movimiento
        if movimiento.tipo == 'Salida':
            if movimiento.cantidad > instance.producto.cantidad:
                raise ValueError("No hay suficientes productos en el inventario para esta salida")
            instance.producto.cantidad -= movimiento.cantidad  # Decrementar la cantidad de productos
        elif movimiento.tipo == 'Entrada':
            instance.producto.cantidad += movimiento.cantidad  # Incrementar la cantidad de productos
        instance.producto.save()  # Guardar el cambio en la cantidad de productos
