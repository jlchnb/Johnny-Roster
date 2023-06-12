from django.shortcuts import render
from pedido.models import Producto, Pedido

# Create your views here.
def inicio(request):
    context = {}
    return render(request, 'pedido/index.html',context)

def lista_productos(request):
    lista_productos = Producto.objects.raw("SELECT * FROM venta_producto") #select * from Producto
    context={"producto":lista_productos}
    return render(request,'pedido/index.html',context)

def agregar_productos(request):
    if request.method != "POST":
        lista_productoss = Producto.objects.all()
        context={"producto":lista_productoss}
        return render(request,'venta/producto_add.html',context)
    else:
        #rescatamos en variables os valores del formulario (name)
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
        objAlumno = Producto.objects.create(  
            rut              = rut,
            nombre           = nombre,
            apellido_paterno = ape_Pat,
            apellido_materno = ape_Mat,
            fecha_nacimiento = fec_Nac,
            id_productos        = objGenero,
            telefono         = telefono,
            email            = email,
            direccion        = direccion,
            activo           = 1)
        
        objAlumno.save() #insert en la base de datos
        lista_productoss = Producto.objects.all()
        context = {"mensaje":"Se guardó producto","producto":lista_productoss}
        return render(request,'venta/producto_add.html',context)
        
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
        objAlumno = Producto()
        objAlumno.rut              = rut
        objAlumno.nombre           = nombre
        objAlumno.apellido_paterno = ape_Pat
        objAlumno.apellido_materno = ape_Mat
        objAlumno.fecha_nacimiento = fec_Nac
        objAlumno.id_productos        = objGenero
        objAlumno.telefono         = telefono
        objAlumno.email            = email
        objAlumno.direccion        = direccion
        objAlumno.activo           = 1
        
        objAlumno.save() #update en la base de datos
        lista_productoss = Producto.objects.all()
        context = {"mensaje":"Se actualizó producto","producto":lista_productoss}
        return render(request,'venta/producto_edit.html',context)
    else:
        lista_productos = Producto.objects.all()
        context = {"productos":lista_productos}
        return render(request,'venta/index.html',context)

def crud(request):
    pedidos = Pedido.objects.all()
    context = {'pedidos': pedidos}
    return render(request, 'pedidos/pedidos_list.html', context)

def mostrar_productoss(request):
    lista_producto = Pedido.objects.all()
    context = {"producto":lista_producto}
    return render(request, 'pedido/productos',context)