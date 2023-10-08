from django.shortcuts import render
from cars.models import Car

# Create your views here.
# Order_by com - no inicio ordena decrecente (-model)


def cars_view(request):
    cars = Car.objects.all().order_by('-model')
    search = request.GET.get('search')
    print(search)
    if search:
        cars = Car.objects.filter(model__icontains=search)
    return render(request=request,
                  template_name='cars.html',
                  context={'cars': cars})
