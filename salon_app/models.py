from django.db import models
from django.urls import reverse 

# Create your models here.
class HairSalon(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('s_detail', args=[str(self.id)])

class HairDresser(models.Model):
    name = models.CharField(max_length=100)
    years_experience = models.PositiveIntegerField()  # Years of experience
    salon = models.ForeignKey(HairSalon, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('hd_detail', args=[str(self.id)])

class Client(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    salon = models.ForeignKey(HairSalon, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('c_detail', args=[str(self.id)])


