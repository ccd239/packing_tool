from django.shortcuts import render
from django.views import View
from .forms import ProductSizesForm
from carton_sizes.models import Carton_sizes

# Create your views here.
class Index(View):
    def get(self, request):
        form = ProductSizesForm() #form is a variable we created
        return render(request, 'index.html',{'form': form})
    
    def post(self,request):
        form = ProductSizesForm(request.POST)

        if form.is_valid():
            length_product = form.cleaned_data['length']
            width_product = form.cleaned_data['width']
            height_product = form.cleaned_data['height']

            # Retrieve specific fields from Carton_sizes
            carton_sizes = Carton_sizes.objects.all()

            # Prepare data for template
            data = []
            for carton in carton_sizes:
                length_ratio = int(carton.length / length_product)
                width_ratio = int(carton.width / width_product)
                height_ratio = int(carton.height / height_product)
                data.append({
                    'length_ratio': length_ratio,
                    'width_ratio': width_ratio,
                    'height_ratio': height_ratio,
                })

            context = {
                'form': form,
                'data': data,
                'length_product' : length_product,
                'width_product' : width_product,
                'height_product': height_product,
            }
            return render(request, 'results.html', context)
        
      # If the form is not valid, render the form again with errors
        return render(request, 'index.html', {'form': form})