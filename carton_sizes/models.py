from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

"""Creates a module (table) with different fields: 
codename for each carton code- text field - max of 255 characters
length of the carton - integer - max 4 digits
width of the carton - integer - max 4 digits
height of the carton - integer - max 4 digits """

class Carton_sizes(models.Model):
  codename = models.CharField(max_length=255)
  length = models.IntegerField(null=False,validators=[MinValueValidator(0),
                                MaxValueValidator(150000)])
  width = models.IntegerField(null=False, validators=[MinValueValidator(0),
                                MaxValueValidator(150000)])
  height = models.IntegerField(null=False, validators=[MinValueValidator(0),
                                MaxValueValidator(150000)]) #set the min and max values for the carton sizes
  material = models.CharField(null=True, max_length=255)
  thickness = models.IntegerField(null=True,validators=[MinValueValidator(0),
                                MaxValueValidator(20)])
  folding_type = models.CharField(null=True,max_length=255)

  def __str__(self):
    return f"{self.codename} : {self.length} x {self.width} x {self.height}"