from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from sicv.settings import status_choices


class Usuario(AbstractUser):
    """Model that overrides authModel to allow has more information in the same table
    """

    identificacion = models.CharField(
        max_length = 30,
        blank = True,
        null = True,
        verbose_name = 'Identificación',
        )


    telefono = models.CharField(
        max_length = 30,
        blank = True,
        null = True,
        verbose_name = 'Teléfono',
        )

    codigo = models.CharField(
        max_length = 30,
        blank = True,
        null = True,
        verbose_name = 'Código',
        )
    
    edad = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = 'Edad',
        )

    resultado_examen = models.CharField(
        max_length = 30,
        blank = True,
        null = True,
        verbose_name = 'Resultado examen de admisión',
        )
    
    pais = models.ForeignKey(
        'Pais',
        blank = True,
        null = True,
        verbose_name = 'País',
        on_delete=models.CASCADE
        )

    ciudad = models.ForeignKey(
        'Ciudad',
        blank = True,
        null = True,
        verbose_name = 'Ciudad',
        on_delete=models.CASCADE
        )

    genero = models.ForeignKey(
        'Genero',
        blank = True,
        null = True,
        verbose_name = 'Genero',
        on_delete=models.CASCADE
        )

    tipo_identificacion = models.ForeignKey(
        'TipoIdentificacion',
        blank = True,
        null = True,
        verbose_name = 'Tipo de identificación',
        on_delete=models.CASCADE
        )


    pregrado_egreso = models.ForeignKey(
        'PregradosEgreso',
        blank = True,
        null = True,
        verbose_name = 'Pregrado de egreso',
        on_delete=models.CASCADE
        )
    
    colegio_egreso = models.ForeignKey(
        'ColegioEgreso',
        blank = True,
        null = True,
        verbose_name = 'Colegio de egreso',
        on_delete=models.CASCADE
        )

    nota_pregrado = models.CharField(
        max_length = 5,
        blank = True,
        null = True,
        verbose_name = 'Nota pregrado',
        )

        
        

    def __str__(self):
        if self.codigo:
            return self.codigo
        else:
            return self.username

    class Meta:
        verbose_name = u'Usuario'
        verbose_name_plural = u'Usuarios'


class ColegioEgreso(models.Model):
    """Models that contains all cities
    """


    nombre = models.CharField(
        max_length = 150,
        verbose_name = 'Nombre del colegio',
        )

    def __str__(self):
        return self.nombre


class PregradosEgreso(models.Model):
    """Models that contains all cities
    """


    nombre = models.CharField(
        max_length = 150,
        verbose_name = 'Nombre del programa',
        )
   


    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = u'Pregrado de egreso'
        verbose_name_plural = u'Pregrados de egreso'


class Pais(models.Model):
    """Models that contains all cities
    """


    nombre = models.CharField(
        max_length = 50,
        verbose_name = 'Nombre del país',
        )

    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'Descripción del país',
        )
    


    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = u'País'
        verbose_name_plural = u'Paises'


class Ciudad(models.Model):
    """Models that contains all cities
    """


    nombre = models.CharField(
        max_length = 50,
        verbose_name = 'Nombre de la ciudad',
        )

    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'Descripción de la ciudad',
        )
    

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = u'Ciudad'
        verbose_name_plural = u'Ciudades'


class Genero(models.Model):
    """Models to set the gender types allowed
    """
    nombre = models.CharField(
        max_length = 50,
        verbose_name = 'Nombre',
        )

    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'Descripción',
        )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = u'Género'
        verbose_name_plural = u'Géneros'


class TipoIdentificacion(models.Model):
    """Models to set the id types allowed
    """
    nombre = models.CharField(
        max_length = 50,
        verbose_name = 'Nombre',
        )

    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'Descripción',
        )


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = u'Tipo de indentificación'
        verbose_name_plural = u'Tipos de identificaciones'


class Facultad(models.Model):
    """Models to set the id types allowed
    """
    nombre = models.CharField(
        max_length = 50,
        verbose_name = 'Nombre de la facultad',
        )

    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'Descripción de la facultad',
        )


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = u'Facultad'
        verbose_name_plural = u'Facultades'


class Modalidad(models.Model):
    """Models to set the id types allowed
    """
    nombre = models.CharField(
        max_length = 50,
        verbose_name = 'Nombre de la modalidad',
        )

    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'Descripción de la modalidad',
        )


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = u'Modalidad'
        verbose_name_plural = u'Modalidades'


class Jornada(models.Model):
    """Models to set the id types allowed
    """
    nombre = models.CharField(
        max_length = 50,
        verbose_name = 'Nombre de la jornada',
        )

    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'Descripción de la jornada',
        )


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = u'Jornada'
        verbose_name_plural = u'Jornadas'


class Curso(models.Model):
    """Models to set the id types allowed
    """

    codigo = models.CharField(
        max_length = 30,
        verbose_name = 'Código',
        )



    nombre = models.CharField(
        max_length = 250,
        verbose_name = 'Nombre del curso',
        )

    descripcion = models.TextField(
        verbose_name=u'Descripción del curso',
        )

    profesor = models.ForeignKey(
        'Usuario',
        blank = True,
        null = True,
        verbose_name = 'Profesor',
        on_delete=models.CASCADE
        )

    semestre = models.IntegerField(
        verbose_name = u'Semestre',
    )


    contenido_pdf = models.FileField(
        upload_to='./contenidos',
        verbose_name=u'Contenido del curso PDF',
        )

    curso_pre = models.ForeignKey(
        'self',
        blank = True,
        null = True,
        verbose_name = 'Curso Pre-requisito',
        on_delete=models.CASCADE
        )

    num_estudiantes = models.IntegerField(
        verbose_name = u'Número de estudiantes inscritos',
    )

    

    
    


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = u'Curso'
        verbose_name_plural = u'Cursos'


class Programa(models.Model):
    """Models to set the id types allowed
    """

    codigo = models.CharField(
        max_length = 30,
        verbose_name = 'Código',
        )


    nombre = models.CharField(
        max_length = 250,
        verbose_name = 'Nombre del programa',
        )

    descripcion = models.TextField(
        verbose_name=u'Descripción del programa',
        )

    activo = models.BooleanField(
        default = True,
        verbose_name = u'Activo',
    )

    snies = models.CharField(
        max_length = 250,
        verbose_name = 'SNIES del programa',
        )


    direccion = models.CharField(
        max_length = 250,
        verbose_name = 'Dirección del programa',
        )

    email = models.CharField(
        max_length = 250,
        verbose_name = 'Email del programa',
        )

    imagen = models.ImageField(
        verbose_name=u'Imagen del programa',
        upload_to='imagenes_programas/',
        max_length=255,
        help_text='80x80',
        null = True,
    )

    telefono = models.CharField(
        max_length = 250,
        verbose_name = 'Teléfono del programa',
        )

    duracion = models.IntegerField(
        verbose_name = u'Duración',
    )

    cordinador = models.ForeignKey(
        'Usuario',
        verbose_name = 'Coordinador',
        on_delete=models.CASCADE
        )
    
    facultad = models.ForeignKey(
        'Facultad',
        blank = True,
        null = True,
        verbose_name = 'Facultad',
        on_delete=models.CASCADE
        )

    modalidad = models.ForeignKey(
        'Modalidad',
        blank = True,
        null = True,
        verbose_name = 'Modalidad',
        on_delete=models.CASCADE
        )

    jornada = models.ForeignKey(
        'Jornada',
        blank = True,
        null = True,
        verbose_name = 'Jornada',
        on_delete=models.CASCADE
        )

    

    plan_estudio = models.FileField(
        upload_to='./planes',
        verbose_name=u'Plan de estudio',
        )
    
    cursos = models.ManyToManyField(
        'Curso',
        verbose_name=u'Cursos del programa'
        )




    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = u'Programa'
        verbose_name_plural = u'Programas'


class ProgramaUsuario(models.Model):
    """Models to set the id types allowed
    """

    activo = models.BooleanField(
        default = True,
        verbose_name = u'Activo',
    )

    fecha_inscripcion = models.DateField(
        verbose_name = u'Fecha de inscripción',
    )

    status = models.CharField(
       max_length=32,
       choices=status_choices,
       default='pendiente',
       verbose_name = 'Estado',
    )
    

    usuario = models.ForeignKey(
        'Usuario',
        blank = True,
        null = True,
        verbose_name = 'Estudiante',
        on_delete=models.CASCADE
        )
    
    programa = models.ForeignKey(
        'Programa',
        blank = True,
        null = True,
        verbose_name = 'Programa',
        on_delete=models.CASCADE
        )

    semestre = models.IntegerField(
        verbose_name = u'Semestre',
        default = 1
    )


    def __str__(self):
        return (self.usuario.codigo) + ' - ' + (self.programa.nombre)

    class Meta:
        verbose_name = u'Programa de estudiante'
        verbose_name_plural = u'Programas de estudiantes'


class CursoUsuario(models.Model):
    """Models to set the id types allowed
    """

    estado = models.BooleanField(
        default = True,
        verbose_name = u'Activo',
    )

    fecha_inscripcion = models.DateField(
        verbose_name = u'Fecha de inscripción',
    )


    usuario = models.ForeignKey(
        'Usuario',
        blank = True,
        null = True,
        verbose_name = 'Estudiante',
        on_delete=models.CASCADE
        )
    
    curso = models.ForeignKey(
        'Curso',
        blank = True,
        null = True,
        verbose_name = 'Curso',
        on_delete=models.CASCADE
        )

    programa = models.ForeignKey(
        'Programa',
        blank = True,
        null = True,
        verbose_name = 'Programa',
        on_delete=models.CASCADE
        )

    status = models.CharField(
       max_length=32,
       choices=status_choices,
       default='pendiente',
       verbose_name = 'Estado',
    )

    semestre = models.IntegerField(
        verbose_name = u'Semestre',
        default = 1
    )
    


    def __str__(self):
        return (self.usuario.codigo) + ' - ' + (self.programa.nombre) + ' - ' + (self.curso.nombre)

    class Meta:
        verbose_name = u'Curso de estudiante'
        verbose_name_plural = u'Cursos de estudiantes'


class CursoSemestre(models.Model):
    """Models to set the id types allowed
    """


    programa = models.ForeignKey(
        'Programa',
        blank = True,
        null = True,
        verbose_name = 'Programa',
        on_delete=models.CASCADE
        )

    semestre = models.IntegerField(
        verbose_name = u'Semestre',
        default = 1
    )

    max_curso = models.IntegerField(
        verbose_name = u'Maxímo de cursos por semestre',
        default = 1
    )
    


    def __str__(self):
        return (self.programa.nombre) + ' - ' + str(self.semestre) + ' - ' + str(self.max_curso) 

    class Meta:
        verbose_name = u'Máximo curso por semestre'
        verbose_name_plural = u'Maxímos cursos por semestres'


class Contacto(models.Model):
    """Models to set the id types allowed
    """
    nombre = models.CharField(
        max_length = 250,
        verbose_name = 'Nombre',
        )
    
    email = models.CharField(
        max_length = 255,
        verbose_name = 'Email',
        )

    telefono = models.CharField(
        max_length = 50,
        verbose_name = 'Teléfono',
        )

    comentarios = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'Comentarios',
        )

    programa = models.ForeignKey(
        'Programa',
        blank = True,
        null = True,
        verbose_name = 'Programa',
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = u'Contacto'
        verbose_name_plural = u'Contactos'
