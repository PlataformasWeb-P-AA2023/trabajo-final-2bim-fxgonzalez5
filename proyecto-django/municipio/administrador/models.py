from django.db import models
from decimal import Decimal, ROUND_HALF_UP

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cedula = models.CharField(max_length=30, unique=True)
    correo = models.EmailField()

    def __str__(self):
        return "Persona: %s - %s - %s - %s" % (self.nombres,
                self.apellidos,
                self.cedula,
                self.correo)
    
    def get_locales_comida(self):
        cantidad = [c for c in self.locales_comida_persona.all()]
        return len(cantidad)
    
    def get_locales_repuestos(self):
        cantidad = [c for c in self.locales_repuestos_persona.all()]
        return len(cantidad)
    

class Barrio(models.Model):
    nombre = models.CharField(max_length=75)
    siglas = models.CharField(max_length=10)

    def __str__(self):
        return "Barrio: %s - %s" % (self.nombre, self.siglas)
    
    def get_locales_comida(self):
        cantidad = [c for c in self.locales_comida_barrio.all()]
        return len(cantidad)
    
    def get_locales_repuestos(self):
        cantidad = [c for c in self.locales_repuestos_barrio.all()]
        return len(cantidad)

class LocalComida(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE,
        related_name="locales_comida_persona")
    direccion = models.CharField(max_length=75)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE,
        related_name="locales_comida_barrio")
    tipo_comida = models.CharField(max_length=50)
    ventas_mes = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return "Local Comida: %s %s - %s - %s - %s - %f" % (self.propietario.nombres, self.propietario.apellidos,
                self.direccion,
                self.barrio.nombre,
                self.tipo_comida,
                self.ventas_mes)
    
    def get_pago_permiso(self):
        costo = self.ventas_mes * Decimal(0.8)
        return costo.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    

class LocalRepuestos(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE,
        related_name="locales_repuestos_persona")
    direccion = models.CharField(max_length=75)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE,
        related_name="locales_repuestos_barrio")
    total_mercaderia = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return "Local Comida: %s %s - %s - %s - %f" % (self.propietario.nombres, self.propietario.apellidos,
                self.direccion,
                self.barrio.nombre,
                self.total_mercaderia)
    
    def get_pago_permiso(self):
        costo = self.total_mercaderia * Decimal(0.001)
        return costo.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)