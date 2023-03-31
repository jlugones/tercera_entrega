from django.db import models

class Estudiante(models.Model):
    apellido = models.CharField(max_length=50, null=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido} Email: {self.email}"


class Profesor(models.Model):
    profesion = models.CharField(max_length=20)
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido} - Profesion: {self.profesion} - Email: {self.email}"

class Curso(models.Model):
    name = models.CharField(max_length=50)
    idc = models.IntegerField()
    def __str__(self):
        return f"Curso: {self.name}, Camada: {self.idc}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    entregado = models.BooleanField
