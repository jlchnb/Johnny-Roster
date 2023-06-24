from django.shortcuts import render, redirect
from pedido.models import Producto, Orden, Usuario
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

# Create your views here.
def inicio(request):
    context = {}
    return render(request, 'pedido/index.html',context)

def lista_productos(request):
    print("1")
    lista_productos = Producto.objects.all()
    print(lista_productos)
    context={"productos":lista_productos}
    return render(request, 'pedido/productos_list.html',context)

def agregar_productos(request):
    if request.method != "POST":
        lista_productos = Producto.objects.all()
        context = {"productos": lista_productos}
        return render(request, 'pedido/agregar_productos.html', context)
    else:
        nombre = request.POST["nombre"]
        imagen = request.FILES["imagen"]
        tipo_comida = request.POST["tipo_comida"]
        precio = int(request.POST["precio"])


        # Guardar la imagen en la carpeta de media
        media_root = settings.MEDIA_ROOT
        nombre_imagen = imagen.name
        ruta_imagen = os.path.join(media_root, 'productos', nombre_imagen)
        with open(ruta_imagen, 'wb') as file:
            for chunk in imagen.chunks():
                file.write(chunk)

        # Crear objeto Producto
        producto = Producto.objects.create(
            nombre=nombre,
            imagen=os.path.join(settings.MEDIA_URL, 'productos', nombre_imagen),
            tipo_comida=tipo_comida,
            precio=precio
        )

        producto.save()  # Insertar en la base de datos
        lista_productos = Producto.objects.all()
        context = {"mensaje": "Se agregó el producto", "producto": lista_productos}
        return render(request, 'pedido/agregar_productos.html', context)


def iniciar_sesion(request):
    error_message = None  # Asignar un valor predeterminado a error_message

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('inicio')  # Reemplaza 'inicio' con la URL a la que deseas redirigir después del inicio de sesión exitoso
        else:
            error_message = "Error en el inicio de sesión. Verifica tus credenciales."
    
    return render(request, 'pedido/iniciar_sesion.html', {'error_message': error_message})
    








def eliminar_productos(request,pk):
    
    try:
        producto = Producto.objects.get(rut=pk)

        producto.delete() #delete en la BD
        mensaje = "Se eliminó producto"
        lista_productos = Producto.objects.all()
        context={"productos":lista_productos, "mensaje":mensaje}
        return render(request,'venta/index.html',context)
    except:
        mensaje = "NO se eliminó producto"
        lista_productos = Producto.objects.all()
        context={"productos":lista_productos, "mensaje":mensaje}
        return render(request,'venta/index.html',context)
    
def buscar_productos(request,pk):
    if pk != "":
        producto = Producto.objects.get(rut=pk)
        lista_productoss = Producto.objects.all()
        context={"producto":producto, "producto":lista_productoss}
        if producto:
            return render(request,'venta/producto_edit.html',context)
        else:
            context = {"mensaje":"El producto no existe"}
            return render(request,'venta/index.html',context)
        
def actualizar_productos(request):
    if request.method == "POST":
        #rescatamos en variables los valores del formulario (name)
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        ape_Pat = request.POST["apePat"]
        ape_Mat = request.POST["apeMat"]
        fec_Nac = request.POST["fecNac"]
        productos = request.POST["productos"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]

        objGenero = Producto.objects.get(id_productos = productos)
        #crea producto (izp:nombre del campo de la BD, derecho:variable local)
        objProducto = Producto()
        objProducto.rut              = rut
        objProducto.nombre           = nombre
        objProducto.apellido_paterno = ape_Pat
        objProducto.apellido_materno = ape_Mat
        objProducto.fecha_nacimiento = fec_Nac
        objProducto.id_productos        = objGenero
        objProducto.telefono         = telefono
        objProducto.email            = email
        objProducto.direccion        = direccion
        objProducto.activo           = 1
        
        objProducto.save() #update en la base de datos
        lista_productoss = Producto.objects.all()
        context = {"mensaje":"Se actualizó producto","producto":lista_productoss}
        return render(request,'venta/producto_edit.html',context)
    else:
        lista_productos = Producto.objects.all()
        context = {"productos":lista_productos}
        return render(request,'venta/index.html',context)

def crud(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'pedidos/productos_list.html', context)

def mostrar_productoss(request):
    lista_producto = Orden.objects.all()
    context = {"producto":lista_producto}
    return render(request, 'pedido/productos',context)