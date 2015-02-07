from django.db import models
from django.contrib.auth.models import User

# Modelo de datos
class Agenda(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User)
    
    #Representación como cadena del objeto
    def __str__(self):
        return self.name
    
class Grupo(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User)
    
    #Representación como cadena del objeto
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=200)
    agenda = models.ForeignKey(Agenda)
    
    class Meta:
        ordering = ['first_name', 'last_name']
    
    #Representación como cadena del objeto
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class ContactNetwork(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=255)
    contact = models.ForeignKey(Contact)
    
class Localization(models.Model):
    name = models.CharField(max_length=200)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    email1 = models.EmailField(max_length=254)
    email2 = models.EmailField(max_length=254)
    contact = models.ForeignKey(Contact)
    
    #Representación como cadena del objeto
    def __str__(self):
        return self.name + ' - ' + self.phone1 + ' - ' + self.address1 + ' - ' + self.email1