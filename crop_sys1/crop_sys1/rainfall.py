import json
import requests
from datetime import datetime, timedelta

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
        return "Method Not Allowed"

def rainfall(lat,lon,API_KEY):
    current_date = datetime.now().date()
    six_months_ago = current_date - timedelta(days=6*30)
    url=f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat}%2C{lon}/{six_months_ago}/{current_date}?unitGroup=metric&include=days&key={API_KEY}&contentType=json'
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
        result.append(float(rain_fd))  
        result.append(float(temp_fd))  
        result.append(float(humid_fd))  
        return result
    else:
        return "Can't Access URL"

def rainfall_data(request):
    loc=locate(request)
    API_KEY="3RWR8TYRAAX5NGLJUZ3AZEZ25"
    value=rainfall(loc[0],loc[1],API_KEY)
    return value 