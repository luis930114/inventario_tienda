from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto, Almacen, Ubicacion, MotivoAjuste, Movimiento, Ajuste
from .forms import ProductoForm, AlmacenForm, UbicacionForm, MotivoAjusteForm, MovimientoForm, AjusteForm, AsignarProductoForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos.'})
    else:
        return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
   return render(request, 'home.html')

@method_decorator(login_required, name='dispatch')
class ListaAlmacenes(ListView):
    model = Almacen
    context_object_name = 'almacenes'
    template_name = 'almacen/lista_almacenes.html'

@method_decorator(login_required, name='dispatch')
class DetalleAlmacen(DetailView):
    model = Almacen
    template_name = 'almacen/detalle_almacen.html'

@method_decorator(login_required, name='dispatch')
class AgregarAlmacen(CreateView):
    model = Almacen
    form_class = AlmacenForm
    template_name = 'almacen/agregar_almacen.html'
    success_url = reverse_lazy('lista_almacenes')

@method_decorator(login_required, name='dispatch')
class EditarAlmacen(UpdateView):
    model = Almacen
    form_class = AlmacenForm
    template_name = 'almacen/editar_almacen.html'
    success_url = reverse_lazy('lista_almacenes')

@method_decorator(login_required, name='dispatch')
class EliminarAlmacen(DeleteView):
    model = Almacen
    template_name = 'almacen/eliminar_almacen.html'
    success_url = reverse_lazy('lista_almacenes')

@method_decorator(login_required, name='dispatch')
class ListarUbicaciones(ListView):
    model = Ubicacion
    context_object_name = 'ubicaciones'
    template_name = 'ubicacion/lista_ubicacion.html'

@method_decorator(login_required, name='dispatch')
class DetalleUbicacion(DetailView):
    model = Ubicacion
    template_name = 'ubicacion/detalle_ubicacion.html'

@method_decorator(login_required, name='dispatch')
class AgregarUbicacion(CreateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'ubicacion/agregar_ubicacion.html'
    success_url = reverse_lazy('lista_ubicaciones')

@method_decorator(login_required, name='dispatch')
class EditarUbicacion(UpdateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'ubicacion/editar_ubicacion.html'
    success_url = reverse_lazy('lista_ubicaciones')

@method_decorator(login_required, name='dispatch')
class EliminarUbicacion(DeleteView):
    model = Ubicacion
    template_name = 'ubicacion/eliminar_ubicacion.html'
    success_url = reverse_lazy('lista_ubicaciones')

@method_decorator(login_required, name='dispatch')
class ListaProductos(ListView):
    model = Producto
    template_name = 'producto/lista_productos.html'
    context_object_name = 'productos'

@method_decorator(login_required, name='dispatch')
class AgregarProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/agregar_producto.html'
    success_url = reverse_lazy('lista_productos')

@method_decorator(login_required, name='dispatch')
class DetalleProducto(DetailView):
    model = Producto
    template_name = 'producto/detalle_producto.html'
    context_object_name = 'producto'

@method_decorator(login_required, name='dispatch')
class EditarProducto(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/editar_producto.html'
    success_url = reverse_lazy('lista_productos')

@method_decorator(login_required, name='dispatch')
class EliminarProducto(DeleteView):
    model = Producto
    template_name = 'eliminar_producto.html'
    success_url = reverse_lazy('lista_productos')

@method_decorator(login_required, name='dispatch')
class ListaMotivosAjuste(ListView):
    model = MotivoAjuste
    template_name = 'motivo_ajuste/lista_motivos_ajuste.html'
    context_object_name = 'motivos_ajuste'

@method_decorator(login_required, name='dispatch')
class DetalleMotivoAjuste(DetailView):
    model = MotivoAjuste
    template_name = 'motivo_ajuste/detalle_motivo_ajuste.html'
    context_object_name = 'motivo_ajuste'

@method_decorator(login_required, name='dispatch')
class AgregarMotivoAjuste(CreateView):
    model = MotivoAjuste
    form_class = MotivoAjusteForm
    template_name = 'motivo_ajuste/agregar_motivo_ajuste.html'
    success_url = reverse_lazy('lista_motivos_ajuste')

@method_decorator(login_required, name='dispatch')
class EditarMotivoAjuste(UpdateView):
    model = MotivoAjuste
    form_class = MotivoAjusteForm
    template_name = 'motivo_ajuste/editar_motivo_ajuste.html'
    success_url = reverse_lazy('lista_motivos_ajuste')

@method_decorator(login_required, name='dispatch')
class EliminarMotivoAjuste(DeleteView):
    model = MotivoAjuste
    template_name = 'motivo_ajuste/eliminar_motivo_ajuste.html'
    success_url = reverse_lazy('lista_motivos_ajuste')

@method_decorator(login_required, name='dispatch')
class ListaMovimientos(ListView):
    model = Movimiento
    template_name = 'movimiento/lista_movimientos.html'
    context_object_name = 'movimientos'

@method_decorator(login_required, name='dispatch')
class DetalleMovimiento(DetailView):
    model = Movimiento
    template_name = 'movimiento/detalle_movimiento.html'
    context_object_name = 'movimiento'

@method_decorator(login_required, name='dispatch')
class AgregarMovimiento(CreateView):
    model = Movimiento
    form_class = MovimientoForm
    template_name = 'movimiento/agregar_movimiento.html'
    success_url = reverse_lazy('lista_movimientos')

@method_decorator(login_required, name='dispatch')
class EditarMovimiento(UpdateView):
    model = Movimiento
    form_class = MovimientoForm
    template_name = 'movimiento/editar_movimiento.html'
    success_url = reverse_lazy('lista_movimientos')

@method_decorator(login_required, name='dispatch')
class EliminarMovimiento(DeleteView):
    model = Movimiento
    template_name = 'movimiento/eliminar_movimiento.html'
    success_url = reverse_lazy('lista_movimientos')

@method_decorator(login_required, name='dispatch')
class ListaAjustes(ListView):
    model = Ajuste
    template_name = 'ajuste/lista_ajustes.html'
    context_object_name = 'ajustes'
@method_decorator(login_required, name='dispatch')
class DetalleAjuste(DetailView):
    model = Ajuste
    template_name = 'ajuste/detalle_ajuste.html'
    context_object_name = 'ajuste'

@method_decorator(login_required, name='dispatch')
class AgregarAjuste(CreateView):
    model = Ajuste
    form_class = AjusteForm
    template_name = 'ajuste/agregar_ajuste.html'
    success_url = reverse_lazy('lista_ajustes')

@method_decorator(login_required, name='dispatch')
class EditarAjuste(UpdateView):
    model = Ajuste
    form_class = AjusteForm
    template_name = 'ajuste/editar_ajuste.html'
    success_url = reverse_lazy('lista_ajustes')

@method_decorator(login_required, name='dispatch')
class EliminarAjuste(DeleteView):
    model = Ajuste
    template_name = 'ajuste/eliminar_ajuste.html'
    success_url = reverse_lazy('lista_ajustes')

@login_required
def buscar_productos(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            productos = Producto.objects.filter(nombre__icontains=query)
            return render(request, 'busqueda_productos.html', {'productos': productos})
        else:
            return render(request, 'busqueda_productos.html', {'productos': []})
    else:
        return render(request, 'busqueda_productos.html', {'productos': []})
    

def asignar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        form = AsignarProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')  
    else:
        form = AsignarProductoForm(instance=producto)
    return render(request, 'asignar_producto_ubicacion.html', {'form': form})

