from django.shortcuts import render
from .models import Laptop

def laptop(request):
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')  # Important: must use FILES for file inputs
        details = request.POST.get('details')
        generation = request.POST.get('generation')
        ram = request.POST.get('ram')
        ssd = request.POST.get('ssd')

        laptop_obj = Laptop(
            name=name,
            image=image,
            details=details,
            generation=generation,
            ram=ram,
            ssd=ssd,
        )
        laptop_obj.save()
        # Optionally pass a success message
        return render(request, 'laptop_form.html', {'message': 'Form submitted successfully!'})
    
    return render(request, 'laptop_form.html')


def laptop_list(request):
    laptops = Laptop.objects.all().order_by('-timeStamp')  # Latest first
    return render(request, 'laptops.html', {'laptops': laptops})