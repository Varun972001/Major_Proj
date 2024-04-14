import threading
from django.shortcuts import render
from .esp import esp_func
from .ml import ml_func
# from .rainfall import rainfall_data
from .rainfall1 import weather_data

def start(request):
    return render(request, 'index.html')

final_list=[]
def calculate(request):
    list=esp_func();
    for item in list:
        final_list.append(item)
    # raindata=rainfall_data(request);
    raindata=weather_data(request);
    for item in raindata:
        final_list.append(item)
    string=ml_func(final_list);
    return string

def result(request):
    # def calculate_async(request):
    #     print("This is loader page")
    #     loading_page = render(request, 'loader.html')
    #     return loading_page
        
    # calculation_thread = threading.Thread(target=calculate_async, args=(request,))
    # calculation_thread.start()
    # string=calculate(request)
    # print(string)
    # return render(request, 'result.html', {'data': string})
    
    string=calculate(request)
    print(string)
    return render(request, 'result.html', {'data': string})