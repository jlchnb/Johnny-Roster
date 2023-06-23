from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

class Producto(models.Model):
    TIPO_COMIDA_CHOICES = (
        ('broaster', 'Broaster'),
        ('carne', '100% carne'),
        ('vegetariana', 'Vegetariana'),
        ('acompanamiento', 'Acompañamiento'),
    )

    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='')
    tipo_comida = models.CharField(max_length=20, choices=TIPO_COMIDA_CHOICES)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre


class Usuario(AbstractUser):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)

    GENERO_CHOICES = (
        ('2', 'Mujer'),
        ('3', 'Hombre'),
        ('4', 'Otro'),
    )

    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    contraseña = models.CharField(max_length=128)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='usuarios'  # Agrega un related_name personalizado
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='usuarios'  # Agrega un related_name personalizado
    )

    def __str__(self):
        return self.nombre



class Orden(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    productos = models.ManyToManyField('pedido.Producto')
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"Orden #{self.pk} - {self.usuario.username}"