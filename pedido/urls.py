from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.static import serve


urlpatterns = [
    path('', views.inicio,name =''),
    path('productos_list/',views.lista_productos,name='productos_list'),
    path('agregar_productos/', views.agregar_productos, name='agregar_productos'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('borrarProducto/<str:pk>',views.eliminar_productos,name='productos_del'),
    path('buscarProducto/<str:pk>',views.buscar_productos,name='productos_findEdit'),
    path('actualizarProductos',views.actualizar_productos,name='actualizar_productos'),
    path('crud', views.crud, name='crud'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)