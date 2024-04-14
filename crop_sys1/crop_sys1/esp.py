import requests
import time


def esp_func():
    # time.sleep(5)
    # url = 'http://192.168.4.1'
    # response = requests.get(url)
    # if response.status_code == 200:
        # fetched_data = response.text
        # print("Data fetched successfully:", fetched_data)
    string="Data:4,12,17,3.5"
    result=[]
    result1=[]
    result2=[]
    sum1=0
    ph=0
    result=string.split(":")
    result1=result[1].split(",")
    sum1=int(result1[0])+int(result1[1])+int(result1[2])
    for i in range(0,3):
        result2.append(round(int(result1[i])/sum1,2))
    result2.append(round(float(result1[3]),2))
    print(result2)
    return result2
