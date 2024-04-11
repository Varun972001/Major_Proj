from django.http import HttpResponse
import requests
from datetime import datetime, timedelta, date
import json

def locate(request):
    result=[]
    if request.method == 'GET':
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        print(latitude)
        print(longitude)
        result.append(latitude)
        result.append(longitude)
        print(result)
        return result
    else:
        return "Method not allowed"

def rainfall(lat,lon,API_KEY):
    url=f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat}%2C{lon}/2023-10-01/2024-04-10?unitGroup=metric&include=days&key={API_KEY}&contentType=json'
    response=requests.get(url)
    result=[]
    sum_rain=0
    sum_temp=0
    sum_humid=0
    if(response.status_code==200):
        json_data=response.json()
        for day in json_data["days"]:
            print(day["datetime"])
            rain1=day["precip"]
            sum_rain+=rain1
            temp1=day["temp"]
            sum_temp+=temp1
            humid1=day["humidity"]
            sum_humid+=humid1
        rain_fd=sum_rain/180
        temp_fd=sum_temp/180
        humid_fd=sum_humid/180
        result.append(rain_fd)  
        result.append(temp_fd)  
        result.append(humid_fd)  
        return result
    else:
        return "Can't Access URL"

def rainfall_data(request):
    loc=locate(request)
    API_KEY="SA6X93TJCU3S5CAE44ABSNJS5"
    value=rainfall(loc[0],loc[1],API_KEY)
    return value    