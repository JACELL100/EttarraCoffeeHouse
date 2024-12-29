from django.db import models
# Create your models here.
from django.db import models
from django.utils import timezone
# Create your models here.
class Admin(models.Model):
    sno = models.AutoField(default=0, primary_key=True)
    email = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.email}'


class customer(models.Model):
    sno = models.AutoField(default=0, primary_key=True)
    name = models.CharField(default = 'Mark', max_length=50, null=False)
    email = models.CharField(default='helloworld', max_length=50, null=False)
    password = models.CharField(default='12345678', max_length=100, null=False)

    def __str__(self):
        return f'{self.name}'

class booking(models.Model):
    sno = models.AutoField(default=0, primary_key=True)
    id = models.IntegerField(null=False, unique=True)
    event = models.CharField(default='Music', null=False, max_length=100)
    price = models.IntegerField(default=500, null=False)
    purchased_by = models.CharField(null=False, max_length=50)
    numberoftickets = models.IntegerField(null=False, default=1)

    def __str__(self):
        return f'{self.purchased_by} -> {self.event}'

class Event(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)  
    gprice = models.DecimalField(max_digits=10, decimal_places=2, default=500)
    VIPrice = models.DecimalField(max_digits=10, decimal_places=2, default=500)
    theme = models.TextField(default='NA')
    venue = models.TextField(default='NA')
    chef = models.CharField(max_length=50, default='NA')
    date = models.DateField(default=None)  #Date field
    time = models.TimeField(default=None)  
    seats = models.PositiveIntegerField(default=0)  
    details = models.TextField(null=True, default='NA')  
    
    def __str__(self):
        return f'{self.name}, {self.venue}'
