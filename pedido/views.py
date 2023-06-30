from django.shortcuts import render, redirect, get_object_or_404
from pedido.models import Producto, TipoComida
from .forms import TipoComidaForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os

@login_required
def inicio(request):
    request.session["usuario"]="julio"
    usuario = request.session.get("usuario", None)

    context = {'usuario':usuario}
    return render(request, 'pedido/navbar.html', context)

def inicio_y_lista_productos(request):
    lista_productos = Producto.objects.all()
    context={"lista_productos":lista_productos}
    return render(request, 'pedido/index.html', context)


def lista_productos(request):
    lista_productos = Producto.objects.all()
    context={"productos":lista_productos}
    return render(request, 'pedido/productos_list.html',context)

def agregar_productos(request):
    if request.method != "POST":
        print(request.POST)
        tipoComidas=TipoComida.objects.all()
        context={'tipoComidas':tipoComidas}
        return render(request, 'pedido/agregar_productos.html', context)


    else:
        print(request.POST)
        nombre = request.POST["nombre"]
        imagen = request.FILES["imagen"]
        tipo_comida = request.POST["tipo_comida"]
        precio = int(request.POST["precio"])
        activo="1"

        media_root = settings.MEDIA_ROOT
        nombre_imagen = imagen.name
        ruta_imagen = os.path.join(media_root, 'productos', nombre_imagen)
        with open(ruta_imagen, 'wb') as file:
            for chunk in imagen.chunks():
                file.write(chunk)

        objTipoComida=TipoComida.objects.get(id_tipoComida = tipo_comida)
        obj = Producto.objects.create(
            nombre=nombre,
            imagen=os.path.join(settings.MEDIA_URL, 'productos', nombre_imagen),
            id_tipoComida=objTipoComida,
            precio=precio,
            activo=1
        )
        print(request.POST)
        obj.save()
        context = {"mensaje": "Se agregó el producto"}
        return render(request, 'pedido/agregar_productos.html', context)


def iniciar_sesion(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            error_message = "Error en el inicio de sesión. Verifica tus credenciales."
    
    return render(request, 'pedido/iniciar_sesion.html', {'error_message': error_message})
    
def detalle_producto(request, producto_nombre):
    producto = get_object_or_404(Producto, nombre=producto_nombre)
    choices_tipo_comida = TipoComida.objects.all()  # Obtener todos los objetos de TipoComida

    context = {
        'producto': producto,
        'choices_tipo_comida': choices_tipo_comida,
    }
    return render(request, 'pedido/detalle_producto.html', context)

def productos_del(request,pk):
    context={}
    try:
        producto = Producto.objects.get(nombre=pk)

        producto.delete()
        mensaje = "Se eliminó el producto"
        lista_productos = Producto.objects.all()
        context={"lista_productos":lista_productos, "mensaje":mensaje}
        return render(request,'pedido/productos_list.html',context)
    except:
        mensaje = "Error: NO se eliminó producto"
        lista_productos = Producto.objects.all()
        context={"lista_productos":lista_productos, "mensaje":mensaje}
        return render(request,'pedido/productos_list.html',context)
    
def productos_edit(request,pk):

    if pk != "":
        producto    = Producto.objects.get(nombre=pk)
        tipoComidas = TipoComida.objects.all()

        context={"producto":producto, "tipoComidas":tipoComidas}
        if producto:
            return render(request,'pedido/productos_edit.html',context)
        else:
            context = {"mensaje":"El producto no existe"}
            return render(request,'pedido/productos_edit.html',context)
        
def actualizar_productos(request):

    if request.method == "POST":

        nombre = request.POST["nombre"]
        precio = request.POST["precio"]
        tipo_comida = request.POST["tipo_comida"]
        activo = "1"

        objTipoComida=TipoComida.objects.get(id_tipoComida = tipo_comida)

        producto = Producto()
        producto.nombre = nombre
        producto.precio = precio
        producto.id_tipoComida = objTipoComida
        producto.activo = 1

        if 'imagen' in request.FILES:
            producto.imagen = request.FILES['imagen']

        producto.save()

        tipoComidas= TipoComida.objects.all()
        context = {"mensaje": "Se actualizó el producto", "tipoComidas": tipoComidas, "producto" : producto}
        return render(request, 'pedido/productos_edit.html', context)
    else:
        lista_productos = Producto.objects.all()
        context = {"lista_productos": lista_productos}
        return render(request, 'pedido/productos_list.html', context)



def crud(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'pedido/productos_list.html', context)

def TipoComida_list(request):

    TipoComidas = TipoComida.objects.all()
    context ={'TipoComidas':TipoComidas}
    print("enviado datos Tipo comidas")
    return render(request, "pedido/TipoComida_list.html", context)


def TipoComidaAdd(request):
    print("estoy en controlador TipoComidaAdd...")
    context = {}

    if request.method == "POST":
        print("controlador es un post...")
        form = TipoComidaForm(request.POST)
        if form.is_valid():
            print("estoy en agregar, is_valid")
            form.save()
            context = {"mensaje": "Ok, datos grabados...", "form": TipoComidaForm()}
            return redirect('TipoComidaAdd')  # Redirigir a la página de agregar después de guardar el formulario
    else:
        form = TipoComidaForm()

    context = {"form": form}
    return render(request, 'pedido/TipoComidaAdd.html', context)

        
def TipoComida_del(request, pk):
    mensajes=[]
    errores=[]
    tipoComidas = TipoComida.objects.all()
    try:
        tipoComida=TipoComida.objects.get(id_tipoComida=pk)
        context={}
        if tipoComida:
            tipoComida.delete()
            mensajes.append("Tipo de comida eliminada")
            context = {'tipoComidas':tipoComidas, 'mensajes': mensajes, 'errores' : errores}
            return render(request, 'pedido/TipoComida_list.html', context)
    except:
        print("Error, id no existe")
        tipoComidas=TipoComida.object.all()
        mensaje="Error, id no existe"
        context={'mensaje': mensaje, 'tipoComidas':tipoComidas}

def TipoComida_edit(request,pk):
    try:
        tipoComida=TipoComida.get(id_tipoComidas=pk)
        context={}
        if tipoComida:
            print("Edit encontro el genero")
            if request.method == "POST":
                print("edit, es un POST")
                form = TipoComidaForm(request.POST,instance=tipoComida)
                form.save()
                mensaje="Datos actualizados"
                print(mensaje)
                context={'tipoComida' :tipoComida, 'form': form, 'mensaje':mensaje }
                return render(request, 'pedido/TipoComida_edit.html',context)
            else:
                form=TipoComidaForm(instance=tipoComida)
                mensaje=""
                context={'tipoComida' :tipoComida, 'form': form, 'mensaje':mensaje }
                return render(request, 'pedido/TipoComida_edit.html',context)
    except:
        print("Error")
        tipoComida=TipoComida.objects.all()
        mensaje="Error"
        context={'mensaje': mensaje,'tipoComida':tipoComida}
        return render(request, 'pedido/TipoComida_list.html',context)