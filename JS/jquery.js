$(document).ready(function(){
    $(".error").hide();
    $(".error2").hide();
    $("#enviar").click(function(){
        var nombre="";
        var precio="";
        nombre = $("#nombre").val();
        if (nombre.length == 0){
            $(".error").show();
        }else{
            $(".error").hide();
        }
        precio = $("#precio").val();
        if (precio.length < 3){
            $(".error2").show();
        }else{
            $(".error2").hide();
        }
    });

});