from django.shortcuts import render
from cars.models import Car


# Create your views here.

def cars_view(request):
    cars = Car.objects.all()
    search = request.GET.get('search')
    if search:
        cars = Car.filter(model__contains=search)
    return render(request=request,
                  template_name='cars.html',
                  context={'cars': cars})
