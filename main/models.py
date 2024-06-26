from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cli = models.AutoField(primary_key=True)
    nombre_cli = models.CharField(max_length=70)
    email_cli = models.EmailField(max_length=80)
    pass_cli = models.CharField(max_length=30)
    direccion_cli = models.CharField(max_length=200)
    telefono_cli = models.CharField(max_length=13)
    
class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    monto_pago = models.IntegerField()
    fecha_pago = models.DateField()
    referencia_trans_pago = models.CharField(max_length=20)
    estado_pago = models.CharField(max_length = 10)
    
class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    fecha_orden = models.DateField()
    total_orden = models.IntegerField()
    estado_orden = models.CharField(max_length=10)
    id_cli = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_pago = models.ForeignKey(Pago, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'
    
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
    
class Detalle_carro (models.Model):
    id_detalle_carro = models.AutoField(primary_key=True)
    cantidad_prod = models.IntegerField()
    precio_prod = models.IntegerField()
    id_producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Detalle_carro'
    
class Carro_compra (models.Model):
    id_carro = models.AutoField(primary_key=True)
    fecha_crea_carro = models.DateField()
    total_monto_carro = models.IntegerField()
    id_cli = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_detalle_carro = models.ForeignKey(Detalle_carro, on_delete=models.CASCADE)