# Guía para Levantar un Proyecto de Django con Nginx

1. Instalar Gunicorn a nivel de sistema operativo y en python
2. Agregar algunas direcciones en settings.py del proyecto de Django en la variable *ALLOWED_HOSTS*
3. Agregar una variable para crear una copia de todos los recursos estaticos del proyecto de Django
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
4. Agregar la siguiente configuración en el archivo de urls.py del proyecto de Django para que se agregen los archivos necesarios y se pueda levantar con Ngix
```
# Importar
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Agregar la siguiente variable, debajo de las url creadas para el proyecto
urlpatterns += staticfiles_urlpatterns()
```
5. Recopilar los recusos estaticos del proyecto para que se vizualicen en el servidor de Nginx
```
python manage.py collectstatic
```