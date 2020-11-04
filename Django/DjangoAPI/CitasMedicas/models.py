from django.db import models

# Create your models here.
class Persona(models.Model):
    cod_per = models.AutoField(primary_key=True) # cedula
    nom_per = models.CharField(max_length=100) # Nombre completo
    fna_per = models.CharField(max_length=100) # Fecha de nacimiento
    dir_per = models.CharField(max_length=100) # Direccion de residencia
    ema_per = models.CharField(max_length=100) # Email 
    usu_per = models.CharField(max_length=100) # Nickname
    pas_per = models.CharField(max_length=100) # Password

class Consultorio(models.Model):
    cod_con = models.AutoField(primary_key=True) # Codigo
    des_con = models.CharField(max_length=100) # Descripcion

class Estado(models.Model):
    cod_est = models.AutoField(primary_key=True) # Codigo
    des_est = models.CharField(max_length=100) # Descripcion