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
    template_name = 'almacen/lista_almacenes.html'

class DetalleAlmacen(DetailView):
    model = Almacen
    template_name = 'almacen/detalle_almacen.html'

class AgregarAlmacen(CreateView):
    model = Almacen
    form_class = AlmacenForm
    template_name = 'almacen/agregar_almacen.html'
    success_url = reverse_lazy('lista_almacenes')

class EditarAlmacen(UpdateView):
    model = Almacen
    form_class = AlmacenForm
    template_name = 'almacen/editar_almacen.html'
    success_url = reverse_lazy('lista_almacenes')

class EliminarAlmacen(DeleteView):
    model = Almacen
    template_name = 'almacen/eliminar_almacen.html'
    success_url = reverse_lazy('lista_almacenes')

class ListarUbicaciones(ListView):
    model = Ubicacion
    context_object_name = 'ubicaciones'
    template_name = 'ubicacion/lista_ubicacion.html'

class DetalleUbicacion(DetailView):
    model = Ubicacion
    template_name = 'ubicacion/detalle_ubicacion.html'

class AgregarUbicacion(CreateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'ubicacion/agregar_ubicacion.html'
    success_url = reverse_lazy('lista_ubicaciones')

class EditarUbicacion(UpdateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'ubicacion/editar_ubicacion.html'
    success_url = reverse_lazy('lista_ubicaciones')

class EliminarUbicacion(DeleteView):
    model = Ubicacion
    template_name = 'ubicacion/eliminar_ubicacion.html'
    success_url = reverse_lazy('lista_ubicaciones')

class ListaProductos(ListView):
    model = Producto
    template_name = 'producto/lista_productos.html'
    context_object_name = 'productos'

class AgregarProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/agregar_producto.html'
    success_url = reverse_lazy('home')

class ListaProductos(ListView):
    model = Producto
    template_name = 'producto/lista_productos.html'
    context_object_name = 'productos'

class DetalleProducto(DetailView):
    model = Producto
    template_name = 'detalle_producto.html'
    context_object_name = 'producto'

class EditarProducto(UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'cantidad', 'precio', 'almacen', 'ubicacion', 'categoria']
    template_name = 'editar_producto.html'
    success_url = reverse_lazy('lista_productos')

class EliminarProducto(DeleteView):
    model = Producto
    template_name = 'eliminar_producto.html'
    success_url = reverse_lazy('lista_productos')

