from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.core.exceptions import ValidationError
from decimal   import Decimal
from datetime import datetime
from django.utils import timezone


from computedfields.models import ComputedFieldsModel, computed
# Create your models here.

def only_int(value): 
    if value.isdigit()==False:
        raise ValidationError('ID contains characters')


class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    Razon_social = models.CharField(max_length=255)
    Nit = models.CharField(max_length=15,validators=[only_int])

    def __str__(self):
        return self.nombre


class item(models.Model):
    Descripcion_item = models.CharField(max_length=255)
    Valor_unidad = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(1000000)])

    def __str__(self):
        return self.Descripcion_item


#class Factura(models.Model):
class Factura(ComputedFieldsModel):
#Datos persona     
    Emisor = models.ForeignKey('Persona',on_delete=models.CASCADE, null=False, related_name='emisor_set')
    Receptor = models.ForeignKey('Persona', on_delete=models.CASCADE, null=False,related_name='receptor_set')

#Datos item
    ActItem = models.ForeignKey('item',on_delete=models.CASCADE)
    Cantidad_item = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(1000000)])
#detalles de la factura // datetime.now
    Fecha_E = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Emisor.nombre

    @computed(models.DecimalField(decimal_places=2, max_digits=10,  validators=[MinValueValidator(Decimal('0.01'))]),
    depends=[['self', ['Cantidad_item']],['ActItem', ['Valor_unidad']]])
    def Valor_neto_sin(self):
        return self.Cantidad_item * self.ActItem.Valor_unidad

    @computed(models.DecimalField(decimal_places=2, max_digits=10,  validators=[MinValueValidator(Decimal('0.01'))]),
    depends=[['self', ['Cantidad_item']],['ActItem', ['Valor_unidad']]])
    def Valor_iva(self):
        return (self.Cantidad_item * self.ActItem.Valor_unidad) * 0.16

    @computed(models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal('0.01'))]),
    depends=[['self', ['Cantidad_item']],['ActItem', ['Valor_unidad']]])
    def Valor_total(self):
        return (self.Cantidad_item * self.ActItem.Valor_unidad) * 1.16

    class Meta:
        unique_together = ('Emisor', 'Receptor',)

    #Valor_neto_sin = models.DecimalField((u'Price'), decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    #Valor_iva = models.DecimalField((u'Price'), decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    #Valor_total= models.DecimalField((u'Price'), decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])

    # def prueba(self):
    #       return self.Emisor.nombre + self.Emisor.Razon_social
    #full_name = property(prueba)

  



