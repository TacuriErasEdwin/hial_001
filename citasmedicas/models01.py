from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

class Personas(models.Model):
    
    opciont = [
        ('pa','Paciente'),
        ('me', 'Médico'),
        ('se','Secretaria'),
        ('au','Auxiliar'),
        ('ad','Administrador'),
    ]
    tipo_persona = models.CharField(max_length=20, choices=opciont, default='pa')
   
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
        return f"{self.nombres} {self.apellidos} - {self.tipo_persona}"

class Pacientes(Personas):
    tipo_persona = 'pa'
       
    def edades(self):
        today = date.today()
        edad = today.year - self.fecha_nacimiento.year - (
                    (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return edad

    def __str__(self) -> str:
        return f"Paciente {self.nombres} {self.apellidos}"

class Medicos(Personas):
    tipo_persona = 'me'
    
    def __str__(self) -> str:
        return f"Médico {self.nombres} {self.apellidos}"


class Especialidades(models.Model):
    nombre_espe = models.CharField(max_length=50)
    descripcion_espe = models.CharField(max_length=500)
    fecha_regis_datos = models.DateField()
    usuario_regis_datos = models.CharField(max_length=50)
    fecha_modif_regis = models.DateField()
    usuario_modif_regis = models.CharField(max_length=50)
    medico = models.ManyToManyField(Medicos)
    
    opcions = [
        ('ac','Activo'),
        ('des', 'Desactivo'),
    ]
    estatus_espe = models.CharField(max_length=13, choices=opcions, default='ac')
 
    def __str__(self) -> str:
        return self.nombre_espe +" "+ self.estatus_espe

class Citas(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)  
    paciente =  models.ManyToManyField(Pacientes)
    medico = models.ManyToManyField(Medicos)
    especialidad = models.ForeignKey(Especialidades,on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def _str_(self) -> str:
        return self.fecha_hora

class Consulta_medica(models.Model):
    cita = models.ForeignKey(Citas,on_delete=models.CASCADE) 
    
    opciona = [
        ('si','si'),
        ('no', 'no'),
    ]
    estatus_atencion = models.CharField(max_length=2, choices=opciona, default='si')
       
    motivo = models.CharField(max_length=100)

    def __str__(self):
        return self.estatus_atencion

class Historia_clinica(models.Model):
    consulta_med = models.ForeignKey(Consulta_medica,on_delete=models.CASCADE)
    triaje_peso = models.IntegerField()
    triaje_talla = models.IntegerField()
    triaje_tempe = models.IntegerField()
    triaje_presion = models.CharField(max_length=10)
    diagnostico = models.CharField(max_length=200)
    enfermedad = models.CharField(max_length=200)
    receta = models.CharField(max_length=200)
    pedido_examenes = models.CharField(max_length=200)
    proximo_control = models.DateField()
   
    def __str__(self):
        return (f'Diagnóstico: {self.diagnostico} Receta: {self.receta} Próximo control: {self.proximo_control}')

