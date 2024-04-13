import requests

def esp_func():
    try:
        # Replace 'http://esp8266_ip_address/data_endpoint' with your ESP8266's IP address and data endpoint
        url = 'http://192.168.1.11'
        result=[]
    
        # Send HTTP GET request to ESP8266
        response = requests.get(url)
    
        # Check if request was successful
        if response.status_code == 200:
            # Store the data received from ESP8266 in a variable
            fetched_data = response.text
            print("Data fetched successfully:", fetched_data)
            reuslt = fetched_data.split(',')
            return ['N','P','K','PH']
        else:
            print("Failed to fetch data from ESP8266. Status code:", response.status_code)
            return ['N?','P?','K?','PH?']
    else:
        print("Error In URL") 
        return ["URL ERROR"]