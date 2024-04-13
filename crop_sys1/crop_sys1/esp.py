import requests

def esp_func():

    # Replace 'http://esp8266_ip_address/data_endpoint' with your ESP8266's IP address and data endpoint
    url = 'http://192.168.1.11'

    try:
        # Send HTTP GET request to ESP8266
        response = requests.get(url)
    
        # Check if request was successful
        if response.status_code == 200:
            # Store the data received from ESP8266 in a variable
            fetched_data = response.text
            print("Data fetched successfully:", fetched_data)
        else:
            print("Failed to fetch data from ESP8266. Status code:", response.status_code)

    except Exception as e:
        print("An error occurred:", e)

    return ['N','P','K','PH']