from django.contrib import admin
from .models import Persona,item, Factura
# Register your models here.

@admin.register(Persona)
class AdminPersona(admin.ModelAdmin):
    list_display = ('nombre','Razon_social','Nit')
    list_filter = ('nombre',)


@admin.register(item)
class AdminItem(admin.ModelAdmin):
    list_display = ('Descripcion_item','Valor_unidad')
    list_filter = ('Descripcion_item',)


@admin.register(Factura)
class AdminFactura(admin.ModelAdmin):
    list_display = ('Emisor', 'Receptor', 'Valor_total', 'Valor_iva','Valor_neto_sin')
    list_filter = ('Emisor',)