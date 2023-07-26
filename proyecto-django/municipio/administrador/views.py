from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# importar las clases de models.py
from administrador.models import *

# importar los formularios de forms.pyp
from administrador.forms import *

# Create your views here.
def index(request):
    locales_comida = LocalComida.objects.all()
    locales_repuestos = LocalComida.objects.all()
    diccionario = {'cant_locales_comida': len(locales_comida), 'cant_locales_repuestos': len(locales_repuestos)}
    return render(request, 'index.html', diccionario)

def ingreso(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.data.get("username")
            raw_password = form.data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect(index)
    else:
        form = AuthenticationForm()

    informacion_template = {'form': form}
    return render(request, 'registration/login.html', informacion_template)

def logout_view(request):
    logout(request)
    messages.info(request, "Has salido del sistema")
    return redirect(index)

# Locales de Comida
def listar_locales_comida(request):
    locales_comida = LocalComida .objects.all()
    diccionario = {'locales_comida': locales_comida, 'cant_locales_comida': len(locales_comida)}
    return render(request, 'listarLocalesComida.html', diccionario)

@login_required(login_url='/entrando/login/')   
@permission_required('administrador.change_localcomida', login_url="/entrando/login/")
def editar_local_comida(request, id):
    local_comida = LocalComida.objects.get(pk=id)
    propietario = Persona.objects.get(pk=local_comida.propietario.id)
    barrio = Barrio.objects.get(pk=local_comida.barrio.id)

    if request.method=='POST':
        formulario = LocalComidaForm(propietario, barrio, request.POST, instance=local_comida)
        print(formulario.errors)

        if formulario.is_valid():
            formulario.save()
            return redirect(listar_locales_comida)
    else:
        formulario = LocalComidaForm(propietario, barrio, instance=local_comida)
    
    diccionario = {'formulario': formulario}
    return render(request, 'editarLocalComida.html', diccionario)

@login_required(login_url='/entrando/login/')
@permission_required('administrador.delete_localcomida', login_url="/entrando/login/")
def eliminar_local_comida(request, id):
    local_comida = LocalComida.objects.get(pk=id)
    local_comida.delete()
    return redirect(listar_locales_comida)


# Locales de Repuestos
def listar_locales_repuestos(request):
    locales_repuestos = LocalRepuestos.objects.all()
    diccionario = {'locales_repuestos': locales_repuestos, 'cant_locales_repuestos': len(locales_repuestos)}
    return render(request, 'listarLocalesRepuestos.html', diccionario)

@login_required(login_url='/entrando/login/')
@permission_required('administrador.change_localrepuestos', login_url="/entrando/login/")
def editar_local_repuestos(request, id):
    local_repuestos = LocalRepuestos.objects.get(pk=id)
    propietario = Persona.objects.get(pk=local_repuestos.propietario.id)
    barrio = Barrio.objects.get(pk=local_repuestos.barrio.id)

    if request.method=='POST':
        formulario = LocalRepuestosForm(propietario, barrio, request.POST, instance=local_repuestos)
        print(formulario.errors)

        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = LocalRepuestosForm(propietario, barrio, instance=local_repuestos)
    
    diccionario = {'formulario': formulario}
    return render(request, 'editarLocalRepuestos.html', diccionario)

@login_required(login_url='/entrando/login/')
@permission_required('administrador.delete_localrepuestos', login_url="/entrando/login/")
def eliminar_local_repuestos(request, id):
    local_repuestos = LocalRepuestos.objects.get(pk=id)
    local_repuestos.delete()
    return redirect(listar_locales_repuestos)