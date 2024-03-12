from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto, Almacen, Ubicacion
from .forms import ProductoForm, AlmacenForm, UbicacionForm





def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Mensaje de error si las credenciales son inválidas
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos.'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    return render(request, 'home.html')

class ListaAlmacenes(ListView):
    model = Almacen
    context_object_name = 'almacenes'
    template_name = 'lista_almacenes.html'

class DetalleAlmacen(DetailView):
    model = Almacen
    template_name = 'detalle_almacen.html'

class AgregarAlmacen(CreateView):
    model = Almacen
    form_class = AlmacenForm
    template_name = 'agregar_almacen.html'
    success_url = reverse_lazy('lista_almacenes')

class EditarAlmacen(UpdateView):
    model = Almacen
    form_class = AlmacenForm
    template_name = 'editar_almacen.html'
    success_url = reverse_lazy('lista_almacenes')

class EliminarAlmacen(DeleteView):
    model = Almacen
    template_name = 'eliminar_almacen.html'
    success_url = reverse_lazy('lista_almacenes')

class ListarUbicaciones(ListView):
    model = Ubicacion
    template_name = 'lista_ubicacion.html'

class DetalleUbicacion(DetailView):
    model = Ubicacion
    template_name = 'detalle_ubicacion.html'

class AgregarUbicacion(CreateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'agregar_almacen.html'
    success_url = reverse_lazy('lista_ubicacion')

class EditarUbicacion(UpdateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'editar_ubicacion.html'
    success_url = reverse_lazy('lista_ubicacion')

class EliminarUbicacion(DeleteView):
    model = Ubicacion
    template_name = 'eliminar_ubicacion.html'
    success_url = reverse_lazy('lista_ubicacion')


class AgregarProductoView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'agregar_producto.html'
    success_url = reverse_lazy('home')

