from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus-stations'))

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        counter = 0
        lst = []
        for row in reader:
            counter += 1
            dic = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
            if counter <= 99000:
                lst.append(dic)
    CONTENT = lst
    page_number = int(request.GET.get("page",1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
