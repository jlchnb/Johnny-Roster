from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio,name =''),
    path('lista_productos',views.lista_productos,name='lista_productos'),
    path('productoAdd',views.agregar_producto,name='productoAdd'),
    path('borrarProducto/<str:pk>',views.eliminar_productos,name='productos_del'),
    path('buscarProducto/<str:pk>',views.buscar_productos,name='productos_findEdit'),
    path('actualizarProductos',views.actualizar_productos,name='actualizar_productos'),
    path('crud', views.crud, name='crud'),

    path('listar_generos',views.mostrar_generos,name='crud_generos'),
]

