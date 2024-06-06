from django.http import HttpResponse
from django.template import loader
from .models import Carton_sizes

# Create your views here.
def carton_sizes(request):
   mycartons = Carton_sizes.objects.all().values()
   template = loader.get_template('all_carton_sizes.html')
   context = {
     'mycartons': mycartons,
   }
   return HttpResponse(template.render(context, request))

def details(request, id):
  mycarton = Carton_sizes.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mycarton': mycarton,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))