from django.db import models

#Modelo Abtracto
class PersonaAbs(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=150,verbose_name='Apellido')
    email = models.EmailField(max_length=150,null=True)
    dni = models.IntegerField(verbose_name="DNI")

    class Meta:
        abstract=True

class EstudianteAbs(PersonaAbs):
    matricula = models.CharField(max_length=10,verbose_name='Matricula')

class DocenteAbs(PersonaAbs):
    legajo = models.CharField(max_length=10,verbose_name='Legajo')

#HERENCIA
class PersonaM(models.Model):
    nombre_m = models.CharField(max_length=100,verbose_name='Nombre')
    apellido_m = models.CharField(max_length=150,verbose_name='Apellido')
    email_m = models.EmailField(max_length=150,null=True)
    dni_m = models.IntegerField(verbose_name="DNI")

class EstudianteM(PersonaM):
    matricula_m = models.CharField(max_length=10,verbose_name='Matricula')

class DocenteM(PersonaM):
    legajo_m = models.CharField(max_length=10,verbose_name='Legajo')

class Persona(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=150,verbose_name='Apellido')
    email = models.EmailField(max_length=150,null=True)
    dni = models.IntegerField(verbose_name="DNI")

# Create your models here.
class Estudiante(models.Model):
    persona = models.OneToOneField(Persona,on_delete=models.CASCADE,primary_key=True)
    matricula = models.CharField(max_length=10,verbose_name='Matricula')

class Categoria(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    baja = models.BooleanField(default=0)

    def __str__(self):
        return self.nombre

    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()
        
class Curso(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    descripcion = models.TextField(null=True,verbose_name='Descripcion')
    #fecha_inicio = models.DateField(verbose_name='Fecha de Inicio')
    #portada = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')
    #MANY-TO-ONE / ONE-TO-MANY
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    #estudiantes = models.ManyToManyField(Estudiante) # crearme una tabla intermedia automatica
    estudiantes = models.ManyToManyField(Estudiante,through='Inscripcion')

    def __str__(self):
        return self.nombre
        
class Inscripcion(models.Model):
    
    ESTADOS = [
        (1,'Inscripto'),
        (2,'Cursando'),
        (3,'Egresado'),
    ]
    fecha_creacion = models.DateField(verbose_name='Fecha de creacion')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    estado = models.IntegerField(choices=ESTADOS,default=1)

    def __str__(self):
        return self.id
