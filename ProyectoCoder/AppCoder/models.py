from django.db import models
from django.contrib.auth.models import User

#Clase de equipos de futbol y sus características.
class Futbol(models.Model):

    nombre_equipo=models.CharField(max_length=40)
    entrenador=models.CharField(max_length=40)
    fundacion=models.DateField()
    apodo=models.CharField(max_length=40)
    ubicacion=models.CharField(max_length=40)
    def __str__(self):
        return f"Nombre_equipo:{self.nombre_equipo} - Entrenador: {self.entrenador} - Fundación: {self.fundacion} - Apodo: {self.apodo} - Ubicacion: {self.ubicacion}"

#Clase de equipos de basket y sus características.
class Basket(models.Model):

    nombre_equipo=models.CharField(max_length=40)
    entrenador=models.CharField(max_length=40)
    fundacion=models.DateField()
    apodo=models.CharField(max_length=40)
    ubicacion=models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre_equipo:{self.nombre_equipo} - Entrenador: {self.entrenador} - Fundación: {self.fundacion} - Apodo: {self.apodo} - Ubicacion: {self.ubicacion}"

#Clase de jugadores de tenis y sus características.
class Tenis(models.Model):

    nombre_equipo=models.CharField(max_length=40)
    altura=models.CharField(max_length=40)
    nacimiento=models.DateField()
    apodo=models.CharField(max_length=40)
    pais=models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre_equipo:{self.nombre_equipo} - Altura: {self.altura} - Nacimiento: {self.nacimiento} - Apodo: {self.apodo} - Pais: {self.pais}"


class Avatar(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares',null=True,blank=True)