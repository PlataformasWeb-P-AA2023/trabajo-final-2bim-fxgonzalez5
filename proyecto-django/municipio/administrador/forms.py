from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrador.models import LocalComida, LocalRepuestos

class LocalComidaForm(ModelForm):
    def __init__(self, propietario, barrio, *args, **kwargs):
        super(LocalComidaForm, self).__init__(*args, **kwargs)
        self.initial['propietario'] = propietario
        self.initial['barrio'] = barrio
        # self.initial['propietario'] = "%s %s" % (propietario.nombres, propietario.apellidos)
        # self.initial['barrio'] = barrio.nombre
        # self.fields["propietario"].widget = forms.TextInput(attrs={'readonly': 'readonly'})
        # self.fields["barrio"].widget = forms.TextInput(attrs={'readonly': 'readonly'})

    class Meta:
        model = LocalComida
        fields = ['propietario', 'direccion', 'barrio', 'tipo_comida', 'ventas_mes']
        labels = {
            'propietario': _('El propietario de este local es'),
            'direccion': _('Ingrese la dirección del local'),
            'barrio': _('El local se encuentra en el barrio'),
            'tipo_comida': _('Ingrese el tipo de comida que ofrece el local'),
            'ventas_mes': _('Ingrese el valor de las ventas proyectadas al mes del local'),
        }


class LocalRepuestosForm(ModelForm):
    def __init__(self, propietario, barrio, *args, **kwargs):
        super(LocalRepuestosForm, self).__init__(*args, **kwargs)
        self.initial['propietario'] = propietario
        self.initial['barrio'] = barrio
        # self.initial['propietario'] = "%s %s" % (propietario.nombres, propietario.apellidos)
        # self.initial['barrio'] = barrio.nombre
        # self.fields["propietario"].widget = forms.TextInput(attrs={'readonly': 'readonly'})
        # self.fields["barrio"].widget = forms.TextInput(attrs={'readonly': 'readonly'})

    class Meta:
        model = LocalRepuestos
        fields = ['propietario', 'direccion', 'barrio', 'total_mercaderia']
        labels = {
            'propietario': _('El propietario de este local es'),
            'direccion': _('Ingrese la dirección del local'),
            'barrio': _('El local se encuentra en el barrio'),
            'total_mercaderia': _('Ingrese el valor del total de la mercadería del local'),
        }
