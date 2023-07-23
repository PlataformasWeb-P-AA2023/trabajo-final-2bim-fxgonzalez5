# Trabajo Final - Segundo Bimestre

## Problemática
En el municipio de un cantón del Ecuador se necesita generar un sistema para el departamento de permisos de funcionamiento.

El objetivo es administrar: locales de comida y locales de ventas de repuestos. Las características de los locales de comida son: propietario (de tipo Persona), dirección, barrio  (de tipo Barrio), tipo de comida, ventas proyectadas al mes, pago de permiso (valor de ventas proyectadas al mes * 0.8). Las características de los locales de repuestos son: propietario (de tipo Persona), dirección, barrio (de tipo Barrio), valor de total de la mercadería, valor del pago del permiso (valor total de mercadería * 0.001). Un barrio tiene como atributos: nombre del barrio y siglas. Una persona tiene como características: nombres, apellidos, cédula, correo.

## Tecnologías a usar

- Python
- Flask
- Django
- Django-Rest-Framework
- Nginx
- Gunicorn
- Postgres

## Tareas

- Generar un proyecto en Django.
- Usar base de datos Postgres.
- Generar una aplicación en Django.
- Crear las clases en el modelo (en función de la problemática)
- En la aplicación levantar la parte del administrador. Un CRUD por cada entidad del modelo.
- Crear vistas (def, en views.py). Que permita: en una vista listar los locales de comida con sus características; en otra vista listar los locales de repuestos y sus características.
	- Solo los usuarios autenticados y con permisos de editar pueden editar y eliminar los locales de comida y de repuestos.
- Crear herencia de plantillas; se puede usar una theme en HTML5 y adaptarlo a la dinámica de Django.
- Crear un servicio web a través de django-rest-framework para las entidades: locales de comida, locales de repuestos, barrios, personas.
	- Desde una aplicación web en la librería Flask; listar locales del comida, locales de repuestos, barrios y personas.
- **[Consulta]** Usar una distribución de linux (Ubuntu) nueva ***(puede ser un VirtualBox)***. Instalar un servidor web Nginx y levantar el proyecto de Django desde el servidor Web. Es posible que deba usar: https://gunicorn.org/ como ayuda en el proceso.

## Formas de realizar el trabajo.

- Individual

## Presentación

- Subir los cambios al repositorio del proyecto Django en GitHub (usar la carpeta **proyecto-django**)
- Subir los cambios al repositorio del proyecto Flask en GitHub (usar la carpeta **proyecto-flask**)
- Una guía (simple) de los pasos realizados para levantar el proyecto de Django en Nginx (usar el archivo guia-publicacion.md de la carpeta **publicación**)
- El día de la defensa, se debe exponer desde la máquina que tiene instalado la instancia de Ubuntu.
