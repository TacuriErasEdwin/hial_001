from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctores(models.Model):
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    descripcion=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nombre

class Sintomas(models.Model):
    enfermedad=models.CharField(max_length=200)
    descripcion=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.enfermedad
    
class Cita(models.Model):
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctores, on_delete=models.CASCADE)
    sintomas = models.ManyToManyField(Sintomas)
    motivo=models.CharField(max_length=200)
    fecha_hora = models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.motivo
