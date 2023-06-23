from django.contrib import admin
from .models import Producto, Orden, Usuario

admin.site.register(Producto)
admin.site.register(Orden)
admin.site.register(Usuario)