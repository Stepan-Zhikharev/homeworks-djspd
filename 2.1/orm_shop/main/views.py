from django.http import Http404
from django.shortcuts import render, get_object_or_404

from main.models import Car, Sale, Client


def cars_list_view(request):
    # получите список авто
    cars = Car.objects.all()
    context = {'cars': cars}
    template_name = 'main/list.html'
    return render(request, template_name, context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    car = get_object_or_404(Car, id=car_id)
    try:
        context = {'car': car}
        template_name = 'main/details.html'
        return render(request, template_name, context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')


def sales_by_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)  # Получаем объект Car по его id
    try:
        sales = Sale.objects.filter(car=car)  # Получаем все продажи для данного автомобиля
        clients = []
        for sale in sales:
            clients.extend(sale.client.all())
        context = {
            'car': car,  # Передаем объект Car в контекст шаблона
            'sales': sales,  # Передаем список продаж в контекст шаблона
            'clients': clients,  # Передаем список клиентов в контекст шаблона
        }
        template_name = 'main/sales.html'
        return render(request, template_name, context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
