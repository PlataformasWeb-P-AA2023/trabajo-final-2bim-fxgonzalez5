# Guía para Levantar un Proyecto de Django con Nginx

1. Instalar Gunicorn a nivel de sistema operativo y en python
```
sudo apt-get install gunicorn

# Si se esta trabajando con un entorno instalarlo ahí
pip install gunicorn
```
2. Agregar algunas direcciones en settings.py del proyecto de Django en la variable *ALLOWED_HOSTS*
```
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', '203.0.113.5' ,'localhost']
```
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
6. Levantar el proyecto con Gunicorn como prueba
```
gunicorn --bind 0.0.0.0:8000 raizProyecto.wsgi
```
**Nota:** Luego de probar que se levante el proyecto correctamente, bajarlo (ctrl + c).

7. Crear un archivo para establecer la configuración de Nginx
```
sudo nano etc/systemd/system/gunicorn.service

# Dentro del archivo agregar lo siguiente:

[Unit]
# Metadatos necesarios
Description=gunicorn daemon
After=network.target

[Service]
# Usuario del sistema operativo que ejecutará el proceso
User=usuario-sistema-operativo
# El grupo del sistema operativo que permite la comunicación a desde el servidor web-nginx con gunicorn. No se debe cambiar el valor
Group=www-data

# A través de la variable WorkingDirectory se indica la dirección absoluta del proyecto de Django
# Tener muy en cuenta que el proyecto no puede estar muy adentro del sistema operativo, sino a nivel del home
WorkingDirectory=/home/usuario-sistema/carpeta/proyectos/nombre-proyecto

# En Environment se indica el path de python
# Ejemplo 1: /usr/bin/python3.9
# Ejemplo 2: (Opcional, con el uso de entornos virtuales) /home/usuario/entornos/entorno01/bin
Environment="PATH=agregar-path-python"

# Detallar el comando para iniciar el servicio
ExecStart=path-python/bin/gunicorn --workers 3 --bind unix:application.sock -m 007 proyectoDjango.wsgi:application

# Donde: aplicacion.sock es el nombre del archivo que se debe crear en el directorio del proyecto; proyectoDjango el nombre del proyecto que se intenta vincular con nginx.
# La expresión /bin/gunicorn no se debe modificar.

[Install]
# Esta sección será usada para indicar que el servicio puede empezar cuando se inicie el sistema operativo. Se sugiere no cambiar el valor dado.
WantedBy=multi-user.target
```
8. Iniciar, habilitar y validar el servicio de Gunicorn este funcionando correctamente
```
sudo systemctl start gunicorn.service
sudo systemctl enable gunicorn.service
sudo systemctl status gunicorn.service
```
9. Verificar en la carpeta raíz del proyecto de Django se haya creado un archivo *application.sock*

**Nota:** Si todo esta correcto hasta aquí, proceder a seguir con los siguientes pasos; caso contrario revisar cualquier error y rectificar para continuar.

10. Crear un archivo en la ruta de Nginx para levantar el servicio.
```
sudo nano /etc/nginx/sites-available/nombre_proyecto_django

# Dentro del archivo agregar lo siguiente:

server {
    listen 81;
    server_name localhost;
    
    location / {
        include proxy_params;
        proxy_pass http://unix:/ruta/al/archivo/sock/application.sock;
    }

    
    location /static/ {
        root /ruta/a/la/carpeta/staticos/del/raiz-del-proyecto;
    }

}
```
11. Crear un enlace al archivo anteriormente creado para habilitar el sitio que debe levantar Nginx
```
sudo ln -s /etc/nginx/sites-available/nombre_proyecto_django /etc/nginx/sites-enabled
```
12. Iniciar el servicio de Nginx, si el sitio no carga reiniciar el servicio. Comandos para gestionar el servicio:
```
- sudo service nginx start
- sudo service nginx stop
- sudo service nginx resstart
- sudo service nginx status
```
13. Si todo se realizo correctamente, abrir cualquiera de las siguientes direcciones y verificar que todo este funcionando.
* http://localhost:81
* http://0.0.0.0:81
* http://127.0.0.0:81

__*Opcional*__

Si el proyecto no se levanta y arroja un error de _"502 Bad Gateway"_, en el archivo de configuracion de Nginx verificar que el usuario sea **www-data** con el siguiente comando:
```
sudo nano /etc/nginx/nginx.conf

# Si el usuario esta correcto, reiniciar el servicio de Nginx
```
