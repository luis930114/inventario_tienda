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
from inventario.views import AgregarProductoView

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


    path('agregar_producto/', AgregarProductoView.as_view(), name='agregar_producto'),

]
