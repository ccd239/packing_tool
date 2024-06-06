from django.contrib import admin
from .models import Carton_sizes

# Register your models here.
class CartonSizesAdmin(admin.ModelAdmin):
  list_display = ("codename", "length", "width","height",)
  
admin.site.register(Carton_sizes, CartonSizesAdmin)