 # -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Modelo de datos
class Grupo(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)
    #agendas = models.ManyToManyField(Agenda)
    #user = models.ForeignKey(User)
    
    #Representación como cadena del objeto
    def __str__(self):
        return self.name
    
class Agenda(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField(choices=((1, 'Pública'), (2, 'Privada')), default=2)
    
    grupo = models.ForeignKey(Grupo, blank=True, null=True,on_delete=models.CASCADE)
    #Representación como cadena del objeto
    def __str__(self):
        return self.name
    

#class Miembro(models.Model):
#    grupo = models.ForeignKey(Grupo)
#    user = models.ForeignKey(User)
    
    #Representación como cadena del objeto
#    def __str__(self):
#        return str(self.id)
    
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=200)
    agenda = models.ForeignKey(Agenda,on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['first_name', 'last_name']
    
    #Representación como cadena del objeto
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class ContactNetwork(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=255)
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE)
    
class Localization(models.Model):
    name = models.CharField(max_length=200)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    email1 = models.EmailField(max_length=254)
    email2 = models.EmailField(max_length=254)
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE)

    #Representación como cadena del objeto
    def __str__(self):
        return self.name + ' - ' + self.phone1 + ' - ' + self.address1 + ' - ' + self.email1


class Colores(models.Model):
    name = models.CharField(max_length=50)
    estilo = models.CharField(max_length=300)
    users = models.ManyToManyField(User)

    #Representación como cadena del objeto
    def __str__(self):
        return self.name + ' - '

