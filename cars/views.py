# from typing import Any
# from django.db.models.query import QuerySet
# from django.shortcuts import render, redirect
# from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cars.models import Car
from cars.forms import CarModelForm


# Create your views here.
# Order_by com - no inicio ordena decrecente (-model)


# Modelo Antigo de View o ideal é usar Class herdando de View
# def cars_view(request):
#     cars = Car.objects.all().order_by('-model')
#     search = request.GET.get('search')
#     if search:
#         cars = Car.objects.filter(model__icontains=search)
#     return render(request=request,
#                   template_name='cars.html',
#                   context={'cars': cars})

# def new_car_view(request):
#     if request.method == 'POST':
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#     else:
#         new_car_form = CarModelForm()
#     return render(request, 'new_car.html', {'new_car_form': new_car_form})


# class CarsView(View):

#     def get(self, request):
#         cars = Car.objects.all().order_by('-model')
#         search = request.GET.get('search')

#         if search:
#             cars = Car.objects.filter(model__icontains=search)

#         return render(
#                     request=request,
#                     template_name='cars.html',
#                     context={'cars': cars})


# class NewCarView(View):

#     def get(self, request):
#         new_car_form = CarModelForm()
#         return render(request, 'new_car.html', {'new_car_form': new_car_form})

#     def post(self, request):
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#         return render(request, 'new_car.html', {'new_car_form': new_car_form})


class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars


class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    # success_url = '/cars/'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'
