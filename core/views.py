from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

from .decorators import unauthenticated_user, allowed_users
from .models import *
from .forms import InsumosForm, UserRegisterForm


#Paginas
def index(request):
    return render(request, 'core/index.html')

def galeria(request):
    return render(request, 'core/galeria.html')
def mision(request):
    return render(request, 'core/mision.html')

def ubicacion(request):
    return render(request, 'core/ubicacion.html')

# Registro Insumos
@login_required(login_url='login')
@allowed_users(allowed_roles=['Dueño','trabajador'])
def registro_insumos(request):
    datos = {
        'form' : InsumosForm()      
    }
    if request.method == 'POST':
        formulario = InsumosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Insumo Guardado correctamente"
    return render(request, 'core/registro_insumos.html', datos)

# Sector gestion de insumos
@login_required(login_url='login')
@allowed_users(allowed_roles=['Dueño','trabajador'])
def lista_insumos(request):
    insumosAll = RegistroInsumos.objects.all()
    datos = {
        'listaInsumos' : insumosAll
    }

    return render(request, 'core/lista_insumos.html', datos)
#lista insumos cliente
@login_required(login_url='login')
def lista_insumos2(request):
    insumosAll = RegistroInsumos.objects.all()
    datos = {
        'listaInsumos' : insumosAll
    }

    return render(request, 'core/lista_insumos2.html', datos)

#modificar insumos
@login_required(login_url='login')
@allowed_users(allowed_roles=['Dueño','trabajador'])
def modificar_insumos(request, id):
    insumo = RegistroInsumos.objects.get(id=id)
    datos = {
        'form' : InsumosForm(instance=insumo)
    }
    if request.method == 'POST':
        formulario = InsumosForm(data=request.POST,instance=insumo)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Insumo Modificado correctamente"
            datos['form'] = formulario
    return render(request, 'core/modificar_insumos.html', datos)

#Eliminar insumos   
@login_required(login_url='login')
@allowed_users(allowed_roles=['Dueño'])
def eliminar_insumos(request, id):
    insumo = RegistroInsumos.objects.get(id=id)
    insumo.delete()

    return redirect(to="registro_insumos")

#Login Register
@unauthenticated_user
def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Se creo la cuenta de ' + user)
            return redirect('login')

    context = {'form' : form}
    return render(request, 'core/register.html', context)

#??????
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'El Nombre O la contraseña estan incorrectos')
    context = {}
    return render(request, 'core/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
