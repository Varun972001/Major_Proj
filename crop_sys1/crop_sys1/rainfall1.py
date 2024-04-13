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

def weather_fetcher(lat,lon,start_date,end_date):
    url=f'https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&hourly=temperature_2m,relative_humidity_2m,rain&timezone=auto'
    response=requests.get(url)
    result=[]
    flag=0
    weather_params=["rain","temperature_2m","relative_humidity_2m"]
    if(response.status_code==200):
        json_data=response.json()
        for item in weather_params:
            json_list=json_data["hourly"][item]
            sum1=0
            for item1 in json_list:
                if(item1=="null"):
                    sum1+=0
                else:
                    sum1+=item1
            if(flag==0):
                flag=1
                result.append(round(sum1))
            else:
                result.append(round(sum1/1800))
        return result
    else:
        print("Can't Access URL")

def store_fvalue(final_list,result):
    final_list[0]+=result[0]
    final_list[1]+=result[1]
    final_list[2]+=result[2]
    return final_list

def weather_readings(lat,lon):
    result=[]
    final_list=[0]*3
    current_date = datetime.date.today()

    one_year_ago = current_date - datetime.timedelta(days=366)
    twonhalf_month_before = one_year_ago - datetime.timedelta(days=75)
    result=weather_fetcher(lat,lon,twonhalf_month_before,one_year_ago)
    final_list=store_fvalue(final_list,result)
    print("One Year And Two And Half  Months - One Year Ago:"+str(result))
    # print(final_list)

    one_year_ago1 = current_date - datetime.timedelta(days=365)
    twonhalf_month_after = one_year_ago1 + datetime.timedelta(days=75)
    result=weather_fetcher(lat,lon,one_year_ago1,twonhalf_month_after)
    final_list=store_fvalue(final_list,result)
    print("One Year Ago - One Year Ago And Two And Half Months After:"+str(result))
    # print(result)
    # print(final_list)

    two_year_ago = current_date - datetime.timedelta(days=731)
    twonhalf_month_before1 = two_year_ago - datetime.timedelta(days=75)
    result=weather_fetcher(lat,lon,twonhalf_month_before1,two_year_ago)
    final_list=store_fvalue(final_list,result)
    print("Two Years And Two And Half Months - Two Years Ago:"+str(result))
    # print(result)
    # print(final_list)

    two_year_ago1 = current_date - datetime.timedelta(days=730)
    twonhalf_month_after1 = two_year_ago1 + datetime.timedelta(days=75)
    result=weather_fetcher(lat,lon,two_year_ago1,twonhalf_month_after1)
    final_list=store_fvalue(final_list,result)
    print("Two Years - Two Years And Two And Half Month After:"+str(result))
    # print(result)
    print(final_list)

    # three_year_ago = current_date - datetime.timedelta(days=1097)
    # one_month_before2 = three_year_ago - datetime.timedelta(days=75)
    # result=weather_fetcher(lat,lon,one_month_before2,three_year_ago)
    # final_list=store_fvalue(final_list,result)
    # print(result)
    # print(final_list)

    # three_year_ago1 = current_date - datetime.timedelta(days=1096)
    # one_month_after2 = three_year_ago1 + datetime.timedelta(days=75)
    # result=weather_fetcher(lat,lon,three_year_ago1,one_month_after2)
    # final_list=store_fvalue(final_list,result)
    # print(result)
    # print(final_list)

    final_list[1]=round(final_list[1]/4)
    final_list[2]=round(final_list[2]/4)
    print(final_list)
    return final_list

def weather_data(request):
    loc=locate(request)
    value=weather_readings(loc[0],loc[1])
    return value 