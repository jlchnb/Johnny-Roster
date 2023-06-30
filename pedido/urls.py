from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.inicio_y_lista_productos, name=''),
    path('navbar/', views.inicio,name='navbar'),
    path('productos_list/', views.lista_productos, name='productos_list'),
    path('agregar_productos/', views.agregar_productos, name='agregar_productos'),
    path('borrarProducto/<str:pk>/', views.productos_del, name='productos_del'),
    path('editarProducto/<str:pk>/', views.productos_edit, name='productos_edit'),
    path('ActualizacionProducto/', views.actualizar_productos, name='actualizar_productos'),
    path('crud/', views.crud, name='crud'),
    path('producto/<str:producto_nombre>/', views.detalle_producto, name='detalle_producto'),

    path('TipoComida_list/', views.TipoComida_list, name='TipoComida_list'),
    path('TipoComidaAdd/', views.TipoComidaAdd, name='TipoComidaAdd'),
    path('TipoComida_del/<str:pk>/', views.TipoComida_del, name='TipoComida_del'),
    path('TipoComida_edit/<str:pk>/', views.TipoComida_edit, name='TipoComida_edit'),
    
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
