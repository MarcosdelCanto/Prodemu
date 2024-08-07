from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria_producto(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    descrip_categoria = models.CharField(max_length= 30)
    def __str__(self):
        return self.descrip_categoria
    
class Producto (models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=50, verbose_name='Nombre')
    descri_producto = models.TextField(max_length= 150, verbose_name='Descripcion')
    precio_producto = models.IntegerField(verbose_name='Precio')
    estado_producto = models.BooleanField(default=True, verbose_name='Disponibilidad') 
    img_producto = models.ImageField(upload_to="productos", blank=True)
    id_categoria = models.ForeignKey(Categoria_producto, on_delete=models.CASCADE, verbose_name='Categoria')
    def __str__(self):
        return self.nombre_producto
    
class Carro_compra (models.Model):
    id_carro = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return 'Carrito de: '+ self.usuario.username
    
class Detalle_carro (models.Model):
    id_carro = models.ForeignKey(Carro_compra,on_delete=models.CASCADE)
    id_detalle_carro = models.AutoField(primary_key=True)
    cantidad_prod = models.IntegerField(default=1)
    id_producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Detalle_carro'
    def __str__(self):
        return f'{self.cantidad_prod} x {self.id_producto.nombre_producto}'
