from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio,name =''),
    path('lista_productos',views.lista_productos,name='lista_productos'),
    path('agregar_productos.html', views.agregar_productos, name='agregar_productos'),
    path('iniciar_sesion.html', views.iniciar_sesion, name='iniciar_sesion'),

    path('borrarProducto/<str:pk>',views.eliminar_productos,name='productos_del'),
    path('buscarProducto/<str:pk>',views.buscar_productos,name='productos_findEdit'),
    path('actualizarProductos',views.actualizar_productos,name='actualizar_productos'),
    path('crud', views.crud, name='crud'),

    # path('listar_generos',views.mostrar_generos,name='crud_generos'),
]

