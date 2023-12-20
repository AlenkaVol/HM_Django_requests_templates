import csv
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


list_bus_stations = []
with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_bus_stations.append(row)


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    bus_stations = Paginator(list_bus_stations, 10)
    page = bus_stations.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
