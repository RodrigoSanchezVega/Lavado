from django.db import models

# Create your models here.
class TipoInsumo(models.Model):
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo

class RegistroInsumos(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoInsumo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre