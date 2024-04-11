from django.shortcuts import render
from .esp import esp_func
from .ml import ml_func
# from .rainfall import rainfall_data
from .test import rainfall_data

def start(request):
    return render(request, 'index.html')

final_list=[]
def calculate(request):
    list=esp_func();
    for item in list:
        final_list.append(item)
    raindata=rainfall_data(request);
    for item in raindata:
        final_list.append(item)
    string=ml_func(final_list);
    return string

def result(request):
    string=calculate(request)
    return render(request,'result.html',{'data':string})