from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto, Almacen, Ubicacion, MotivoAjuste, Movimiento, Ajuste
from .forms import ProductoForm, AlmacenForm, UbicacionForm, MotivoAjusteForm, MovimientoForm, AjusteForm





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
    success_url = reverse_lazy('lista_productos')


class DetalleProducto(DetailView):
    model = Producto
    template_name = 'producto/detalle_producto.html'
    context_object_name = 'producto'

class EditarProducto(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/editar_producto.html'
    success_url = reverse_lazy('lista_productos')

class EliminarProducto(DeleteView):
    model = Producto
    template_name = 'eliminar_producto.html'
    success_url = reverse_lazy('lista_productos')

class ListaMotivosAjuste(ListView):
    model = MotivoAjuste
    template_name = 'motivo_ajuste/lista_motivos_ajuste.html'
    context_object_name = 'motivos_ajuste'

class DetalleMotivoAjuste(DetailView):
    model = MotivoAjuste
    template_name = 'motivo_ajuste/detalle_motivo_ajuste.html'
    context_object_name = 'motivo_ajuste'

class AgregarMotivoAjuste(CreateView):
    model = MotivoAjuste
    form_class = MotivoAjusteForm
    template_name = 'motivo_ajuste/agregar_motivo_ajuste.html'
    success_url = reverse_lazy('lista_motivos_ajuste')

class EditarMotivoAjuste(UpdateView):
    model = MotivoAjuste
    form_class = MotivoAjusteForm
    template_name = 'motivo_ajuste/editar_motivo_ajuste.html'
    success_url = reverse_lazy('lista_motivos_ajuste')

class EliminarMotivoAjuste(DeleteView):
    model = MotivoAjuste
    template_name = 'motivo_ajuste/eliminar_motivo_ajuste.html'
    success_url = reverse_lazy('lista_motivos_ajuste')

class ListaMovimientos(ListView):
    model = Movimiento
    template_name = 'movimiento/lista_movimientos.html'
    context_object_name = 'movimientos'

class DetalleMovimiento(DetailView):
    model = Movimiento
    template_name = 'movimiento/detalle_movimiento.html'
    context_object_name = 'movimiento'

class AgregarMovimiento(CreateView):
    model = Movimiento
    form_class = MovimientoForm
    template_name = 'movimiento/agregar_movimiento.html'
    success_url = reverse_lazy('lista_movimientos')

class EditarMovimiento(UpdateView):
    model = Movimiento
    form_class = MovimientoForm
    template_name = 'movimiento/editar_movimiento.html'
    success_url = reverse_lazy('lista_movimientos')

class EliminarMovimiento(DeleteView):
    model = Movimiento
    template_name = 'movimiento/eliminar_movimiento.html'
    success_url = reverse_lazy('lista_movimientos')

class ListaAjustes(ListView):
    model = Ajuste
    template_name = 'ajuste/lista_ajustes.html'
    context_object_name = 'ajustes'

class DetalleAjuste(DetailView):
    model = Ajuste
    template_name = 'ajuste/detalle_ajuste.html'
    context_object_name = 'ajuste'

class AgregarAjuste(CreateView):
    model = Ajuste
    form_class = AjusteForm
    template_name = 'ajuste/agregar_ajuste.html'
    success_url = reverse_lazy('lista_ajustes')

class EditarAjuste(UpdateView):
    model = Ajuste
    form_class = AjusteForm
    template_name = 'ajuste/editar_ajuste.html'
    success_url = reverse_lazy('lista_ajustes')

class EliminarAjuste(DeleteView):
    model = Ajuste
    template_name = 'ajuste/eliminar_ajuste.html'
    success_url = reverse_lazy('lista_ajustes')


