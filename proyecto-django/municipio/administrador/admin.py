from django.contrib import admin
from administrador.models import *

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'cedula', 'correo')
    search_fields = ('nombres', 'apellidos', 'cedula')
admin.site.register(Persona, PersonaAdmin)

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'siglas')
    search_fields = ('nombre', 'siglas')
admin.site.register(Barrio, BarrioAdmin)

class LocalComidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_propietario', 'direccion', 'get_barrio', 'tipo_comida', 'ventas_mes', 'get_pago_permiso')
    search_fields = ('get_persona', 'get_barrio', 'tipo_comida')
    raw_id_fields = ('propietario', 'barrio')

    def get_propietario(self, obj):
        return obj.propietario.nombres + " " + obj.propietario.apellidos
    
    def get_barrio(self, obj):
        return obj.barrio.nombre
admin.site.register(LocalComida, LocalComidaAdmin)

class LocalRepuestosAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_propietario', 'direccion', 'get_barrio', 'total_mercaderia', 'get_pago_permiso')
    search_fields = ('get_persona', 'get_barrio')
    raw_id_fields = ('propietario', 'barrio')

    def get_propietario(self, obj):
        return obj.propietario.nombres + " " + obj.propietario.apellidos
    
    def get_barrio(self, obj):
        return obj.barrio.nombre
admin.site.register(LocalRepuestos, LocalRepuestosAdmin)