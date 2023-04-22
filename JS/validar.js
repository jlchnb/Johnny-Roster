function validar(){
    var name,correo,pass,text;
    name = document.getElementById("nombre").value;
    correo = document.getElementById("correo").value;
    pass = document.getElementById("password").value;

    if (name.length != 3){
        text = "Favor de ingresar nombre minimo de 3 caracteres"
    }else{
        text = "";
    }
    document.getElementById("valida_nombre").innerHTML = text;

    if (correo.length == 0){
        text = "Correo no debe ir vacio !";   
    }else{
        text = "";
    }
    document.getElementById("valida_email").innerHTML = text;
    if (pass.length != 8){
        text = "Contraseña debe tener largo 8";
    }else{
        text = "";
    }
    document.getElementById("valida_password").innerHTML = text;
}