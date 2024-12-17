from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from datetime import date

# Create your models here.

class Persona(models.Model):
    
    menu = [
        ('pa','Paciente'),
        ('do', 'Doctor'),
        ('se','Secretaria'),
        ('au','Auxiliar'),
        ('ge','Gerente'),
    ]
    rol_persona = models.CharField(max_length=20, choices=menu, default='pa')

    cedula = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')]) #utilizar validador de expresiones regulares para garantizar que esté compuesto por dígitos
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    correo_electronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    ciudad_residencia = models.CharField(max_length=50)
    
    generos = (
        ('m', 'masculino'),
        ('f', 'femenino'),
    )
    genero = models.CharField(max_length=1, choices=generos, blank=True, default='m', help_text='Ingresar género')
    
    fecha_nacimiento = models.DateField()
    
    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.apellidos} {self.nombres} - {self.cedula}"
    
class Paciente(Persona):
    rol_persona = 'pa'
       
    def edad(self, obj):
        return obj.edad
    edad.short_description = 'edad'

    def __str__(self) -> str:
        return f"{self.apellidos} {self.nombres}"

class Doctor(Persona):
    rol_persona = 'do'
    
    def __str__(self) -> str:
        return f"{self.apellidos} {self.nombres}"
    
class Especialidad(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField()
    fecha_modificacion = models.DateTimeField()
    doctor = models.ManyToManyField(Doctor, through='DocEspe') 
       
    def __str__(self) -> str:
        return self.nombre 

class DocEspe(models.Model): #establece la relación entre doctores y especialidades
    id_doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    id_espe = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    quantity = models.IntegerField(default=1) #un doctor debería tener una especialidad
    
   # def _str_(self) -> str:
    #    return (f'La especialidad: {self.id_espe.nombre} se habilita al doctor: {self.id_doc.apellidos}   ').
 

class Cita(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE) #Un paciente puede tomar varias citas
    docespe = models.ForeignKey(DocEspe, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=200)
    fecha_hora = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Cita para: {self.paciente.nombres} {self.paciente.apellidos} Motivo: {self.motivo} Fecha y hora: {self.fecha_hora}"

class AtencionMedica(models.Model):
    cita = models.OneToOneField(Cita,on_delete=models.CASCADE,null=False,blank=False) #Cita genera una atención sin ella no abrá atención
    observaciones = models.CharField(max_length=200)
    acude = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.observaciones
    
class HistoriaMedica(models.Model):
    atencionMedica = models.OneToOneField(AtencionMedica,on_delete=models.CASCADE)
    fechadiagnostico = models.DateTimeField()
    temperatura = models.IntegerField()
    talla = models.IntegerField()
    peso = models.IntegerField()
    presion = models.IntegerField()
    diagnostico = models.CharField(max_length=200)
    indicaciones = models.CharField(max_length=200)
    receta = models.CharField(max_length=200)
    fechaproximocontrol = models.DateTimeField()

    def __str__(self) -> str:
        return self.diagnostico
    
class Farmacia(models.Model):
    historiaMed = models.OneToOneField(HistoriaMedica,on_delete=models.CASCADE)
    fechaentregaM = models.DateTimeField()
    medicamentos = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"Entregado el: {self.fechaentregaM} Medicamentos: {self.medicamentos}"
