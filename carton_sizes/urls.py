from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('carton_sizes/', views.carton_sizes, name='carton_sizes'), #DO NOT FORGET THE / IN THE END
    path('carton_sizes/details/<int:id>/', views.details, name='details'),
    path('testing/', views.testing, name='testing'), 
]


