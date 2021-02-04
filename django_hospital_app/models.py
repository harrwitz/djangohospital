from django.db import models
class appointments(models.Model):
     name = models.CharField(max_length=30,blank=False)
     age = models.IntegerField(blank=False)
     sex = models.CharField(max_length=1,blank=False)
     doctor = models.CharField(max_length=30,blank=False)
     appointment_date = models.DateField(blank=False)
     appointment_time = models.TimeField(blank=False)
     class Meta:
          unique_together = ('doctor', 'appointment_date','appointment_time')









# Create your models here.
