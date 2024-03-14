"""
URL configuration for inventario_tienda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventario import views
from inventario.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),

    path('almacenes/', views.ListaAlmacenes.as_view(), name='lista_almacenes'),
    path('almacen/<int:pk>/', views.DetalleAlmacen.as_view(), name='detalle_almacen'),
    path('almacen/agregar/', views.AgregarAlmacen.as_view(), name='agregar_almacen'),
    path('almacen/editar/<int:pk>/', views.EditarAlmacen.as_view(), name='editar_almacen'),
    path('almacen/eliminar/<int:pk>/', views.EliminarAlmacen.as_view(), name='eliminar_almacen'),

    path('ubicaciones/', views.ListarUbicaciones.as_view(), name='lista_ubicaciones'),
    path('ubicacion/<int:pk>/', views.DetalleUbicacion.as_view(), name='detalle_ubicacion'),
    path('ubicacion/agregar/', views.AgregarUbicacion.as_view(), name='agregar_ubicacion'),
    path('ubicacion/editar/<int:pk>/', views.EditarUbicacion.as_view(), name='editar_ubicacion'),
    path('ubicacion/eliminar/<int:pk>/', views.EliminarUbicacion.as_view(), name='eliminar_ubicacion'),


    path('productos/', ListaProductos.as_view(), name='lista_productos'),
    path('producto/<int:pk>/', DetalleProducto.as_view(), name='detalle_producto'),
    path('producto/agregar/', AgregarProducto.as_view(), name='agregar_producto'),
    path('producto/editar/<int:pk>/', EditarProducto.as_view(), name='editar_producto'),
    path('producto/eliminar/<int:pk>/', EliminarProducto.as_view(), name='eliminar_producto'),

    path('motivos-ajuste/', ListaMotivosAjuste.as_view(), name='lista_motivos_ajuste'),
    path('motivo-ajuste/<int:pk>/', DetalleMotivoAjuste.as_view(), name='detalle_motivo_ajuste'),
    path('motivo-ajuste/agregar/', AgregarMotivoAjuste.as_view(), name='agregar_motivo_ajuste'),
    path('motivo-ajuste/editar/<int:pk>/', EditarMotivoAjuste.as_view(), name='editar_motivo_ajuste'),
    path('motivo-ajuste/eliminar/<int:pk>/', EliminarMotivoAjuste.as_view(), name='eliminar_motivo_ajuste'),

    path('movimientos/', ListaMovimientos.as_view(), name='lista_movimientos'),
    path('movimiento/<int:pk>/', DetalleMovimiento.as_view(), name='detalle_movimiento'),
    path('movimiento/agregar/', AgregarMovimiento.as_view(), name='agregar_movimiento'),
    path('movimiento/editar/<int:pk>/', EditarMovimiento.as_view(), name='editar_movimiento'),
    path('movimiento/eliminar/<int:pk>/', EliminarMovimiento.as_view(), name='eliminar_movimiento'),

    path('ajustes/', ListaAjustes.as_view(), name='lista_ajustes'),
    path('ajuste/<int:pk>/', DetalleAjuste.as_view(), name='detalle_ajuste'),
    path('ajuste/agregar/', AgregarAjuste.as_view(), name='agregar_ajuste'),
    path('ajuste/editar/<int:pk>/', EditarAjuste.as_view(), name='editar_ajuste'),
    path('ajuste/eliminar/<int:pk>/', EliminarAjuste.as_view(), name='eliminar_ajuste'),

    path('producto/buscar/', views.buscar_productos, name='buscar_productos'),
    path('producto/asignar-producto-nueva-ubicacion/<int:pk>/', views.asignar_producto, name='asignar_producto_ubicacion'),

]
