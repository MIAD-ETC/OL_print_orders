from django.db import models
from django.conf import settings

#from django.core.files.storage import FileSystemStorage

# Create your models here.


class STL(models.Model):
    title = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    stl_file = models.FileField(upload_to="stl/")

class Gcode(models.Model):
    title = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    gcode_file = models.FileField(upload_to="gcode/")

class FilamentBrand(models.Model):
    name = models.CharField(max_length = 15)

    def __str__(self):
        return self.name

class FilamentMaterialType(models.Model):
    name = models.CharField(max_length=6)

    def __str__(self):
        return self.name

class Filament(models.Model):

    #color =models.CharField(max_length=50)
    #inventory = models.IntegerField()
    #weight = models.IntegerField()
    #rolls_used = models.IntegerField()
    cost =  models.DecimalField(max_digits=4, decimal_places=2)
    markup = models.DecimalField(max_digits=2, decimal_places=2)
    material = models.ForeignKey(FilamentMaterialType, default=1)
    brand =  models.ForeignKey(FilamentBrand, default=1)

    def __str__(self):
        return '%s %s' % (self.brand, self.material)
    # Vendor

# class Print(models.Model):
#     name =

class Order(models.Model):
    submit_datetime = models.DateTimeField(auto_now_add=True, null=True)
    stl = models.ForeignKey(STL, null=True)
    filament = models.ForeignKey(Filament, null=True)
    gcode = models.ForeignKey(Gcode, null=True)
    cost =  models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    grams = models.PositiveIntegerField(null=True)
    # payment status
    # date completed
    client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='client_orders', default=1)
    tech = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    # class
    # filament
    # collection date



#class Student(models.Model):

#class Faculty(models.Model):

#class OL_staff(models.Model):

#class Course(models.Model):
