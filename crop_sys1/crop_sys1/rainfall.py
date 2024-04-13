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
        temp_fd=sum_temp/76
        humid_fd=sum_humid/76
        result.append(round(sum_rain))
        result.append(round(temp_fd))
        result.append(round(humid_fd))
        return result
    else:
        return "Can't Access URL"
    
def rainfall(lat,lon,API_KEY):
    result1=[]
    result2=[]
    result3=[]
    result4=[]
    final_result=[]
    current_date = datetime.date.today()
    one_year_ago = current_date - datetime.timedelta(days=366)
    twonhalf_month_before = one_year_ago - datetime.timedelta(days=75)
    result1=calculate_data(lat,lon,twonhalf_month_before,one_year_ago,API_KEY)
    
    one_year_ago1 = current_date - datetime.timedelta(days=365)
    twonhalf_month_after = one_year_ago1 + datetime.timedelta(days=75)
    result2=calculate_data(lat,lon,one_year_ago1,twonhalf_month_after,API_KEY)

    two_year_ago = current_date - datetime.timedelta(days=731)
    twonhalf_month_before1 = two_year_ago - datetime.timedelta(days=75)
    result3=calculate_data(lat,lon,twonhalf_month_before1,two_year_ago,API_KEY)
   
    two_year_ago1 = current_date - datetime.timedelta(days=730)
    twonhalf_month_after1 = two_year_ago1 + datetime.timedelta(days=75)
    result4=calculate_data(lat,lon,two_year_ago1,twonhalf_month_after1,API_KEY)

    final_result.append(result1[0]+result2[0]+result3[0]+result4[0])
    final_result.append((result1[1]+result2[1]+result3[1]+result4[1])/4)
    final_result.append((result1[2]+result2[2]+result3[2]+result4[2])/4)
    return final_result

def rainfall_data(request):
    loc=locate(request)
    API_KEY="8U8YFGHHC3H2M5N777KF3URAS"
    value=rainfall(loc[0],loc[1],API_KEY)
    return value 