from django.contrib.auth import get_user_model
from django.db import models



class Producto(models.Model):
    nombre = models.CharField(primary_key=True,max_length=100)
    imagen = models.ImageField(upload_to='productos/')
    id_tipoComida = models.ForeignKey('TipoComida',on_delete=models.CASCADE, db_column='idTipoComida')
    precio = models.IntegerField()
    activo = models.IntegerField()

    def __str__(self):
        return self.nombre
  
class TipoComida(models.Model):
    id_tipoComida  = models.AutoField(db_column='idTipoComida', primary_key=True) 
    tipo_comida     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.tipo_comida)


