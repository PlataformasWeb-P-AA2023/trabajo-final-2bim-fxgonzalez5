"""
    Manejo de urls para la aplicación
    administrador
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    
    # Locales de Comida
    path('locales/comida', views.listar_locales_comida,
        name='listar_locales_comida'),
    path('editar/local/comida/<int:id>', views.editar_local_comida,
        name='editar_local_comida'),
    path('eliminar/local/comida/<int:id>', views.eliminar_local_comida,
        name='eliminar_local_comida'),

    # Locales de Repuestos
    path('locales/repuestos', views.listar_locales_repuestos,
        name='listar_locales_repuestos'),
    path('editar/local/repuestos/<int:id>', views.editar_local_repuestos,
        name='editar_local_repuestos'),
    path('eliminar/local/repuestos/<int:id>', views.eliminar_local_repuestos,
        name='eliminar_local_repuestos'),
    
    # Autenticación
    path('saliendo/logout/', views.logout_view, name="logout_view"),
    path('entrando/login/', views.ingreso, name="login"),
]
