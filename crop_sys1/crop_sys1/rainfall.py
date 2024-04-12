import json
import requests
import datetime

def locate(request):
    result=[]
    if request.method == 'GET':
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        result.append(latitude)
        result.append(longitude)
        print(result)
        return result
    else:
        return "Method Not Allowed"

def calculate_data(lat,lon,date1,date2,API_KEY):
    url=f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat}%2C{lon}/{date1}/{date2}?unitGroup=metric&include=days&key={API_KEY}&contentType=json'
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
        temp_fd=sum_temp/60
        humid_fd=sum_humid/60
        result.append(round(sum_rain))
        result.append(round(temp_fd))
        result.append(round(humid_fd))
        return result
    else:
        return "Can't Access URL"
    
def rainfall(lat,lon,API_KEY):
    result1=[]
    result2=[]
    final_result=[]
    current_date = datetime.date.today()
    one_year_ago = current_date - datetime.timedelta(days=366)
    one_year_ago1 = current_date - datetime.timedelta(days=365)
    two_months_before = one_year_ago - datetime.timedelta(days=61)
    two_months_after = one_year_ago1 + datetime.timedelta(days=61)
    result1=calculate_data(lat,lon,two_months_before,one_year_ago,API_KEY)
    result2=calculate_data(lat,lon,one_year_ago1,two_months_after,API_KEY)
    final_result.append(result1[0]+result2[0])
    final_result.append((result1[1]+result2[1])/2)
    final_result.append((result1[2]+result2[2])/2)
    return final_result

def rainfall_data(request):
    loc=locate(request)
    API_KEY="HMLTELA7RSYR96MSKRJ5GF24K"
    value=rainfall(loc[0],loc[1],API_KEY)
    return value 