from django.db import models

# Create your models here.

class Clientes (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    DNI = models.IntegerField()
    email = models.EmailField()
    
def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.DNI} - {self.email}'

class Accesorios(models.Model):
    
    producto = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    precio = models.IntegerField()
    imagen = models.ImageField (upload_to= "accesorios", null= True)
    
    def __str__(self):
        return f'{self.producto} - {self.tipo} - ${self.precio}'
    
class Textiles (models.Model):
    
    producto = models.CharField(max_length=20)
    tipo =  models.CharField(max_length=20)
    precio = models.IntegerField()
    
    def __str__(self):
        return f'{self.producto} - {self.tipo} - ${self.precio}'
    
    
class ConsultaFormulario(models.Model):

    correo = models.EmailField()
    mensaje = models.TextField()
    
    