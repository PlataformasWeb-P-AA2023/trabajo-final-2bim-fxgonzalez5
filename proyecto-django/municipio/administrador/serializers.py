from administrador.models import *

from rest_framework import serializers
class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    locales_comida = serializers.SerializerMethodField()
    locales_repuestos = serializers.SerializerMethodField()

    class Meta:
        model = Persona
        fields = '__all__'

    def get_locales_comida(self, obj):
        return obj.get_locales_comida()
    
    def get_locales_repuestos(self, obj):
        return obj.get_locales_repuestos()

class BarrioSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    locales_comida = serializers.SerializerMethodField()
    locales_repuestos = serializers.SerializerMethodField()

    class Meta:
        model = Barrio
        fields = '__all__'

    def get_locales_comida(self, obj):
        return obj.get_locales_comida()
    
    def get_locales_repuestos(self, obj):
        return obj.get_locales_repuestos()

class LocalComidaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    barrio_str = serializers.StringRelatedField(source="barrio.nombre", read_only=True)
    pago_permiso = serializers.SerializerMethodField()
    propietario_str = serializers.SerializerMethodField()

    class Meta:
        model = LocalComida
        fields = '__all__'

    def get_pago_permiso(self, obj):
        return obj.get_pago_permiso()
    
    def get_propietario_str(self, obj):
        return f"{obj.propietario.nombres} {obj.propietario.apellidos}"


class LocalRepuestosSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    barrio_str = serializers.StringRelatedField(source="barrio.nombre", read_only=True)
    pago_permiso = serializers.SerializerMethodField()
    propietario_str = serializers.SerializerMethodField()

    class Meta:
        model = LocalRepuestos
        fields = '__all__'
    
    def get_pago_permiso(self, obj):
        return obj.get_pago_permiso()
    
    def get_propietario_str(self, obj):
        return f"{obj.propietario.nombres} {obj.propietario.apellidos}"
