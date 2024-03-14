from django.db import models

class Almacen(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=100) 

    def __str__(self):
        return self.nombre

class MotivoAjuste(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

class Ajuste(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)
    motivo = models.ForeignKey(MotivoAjuste, on_delete=models.CASCADE)
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ajuste de {self.producto.nombre} el {self.fecha}"
    
class Movimiento(models.Model):

    TIPO_CHOICES = [
        ('Entrada', 'Entrada'),
        ('Salida', 'Salida'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)  # Tipo de movimiento: por ejemplo, "Entrada" o "Salida"
    fecha = models.DateTimeField(auto_now_add=True)
    origen = models.ForeignKey(Ubicacion, related_name='movimientos_origen', on_delete=models.CASCADE)
    destino = models.ForeignKey(Ubicacion, related_name='movimientos_destino', on_delete=models.CASCADE)

    """def save(self, *args, **kwargs):
        # Manejo de excepciones básicas
        if self.origen == self.destino:
            raise ValueError("El origen y el destino no pueden ser iguales")
        if self.tipo not in ['Entrada', 'Salida']:
            raise ValueError("El tipo de movimiento debe ser 'Entrada' o 'Salida'")
        if self.cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")
        super().save(*args, **kwargs) """

    def __str__(self):
        return f"Movimiento de {self.producto.nombre} el {self.fecha}"

