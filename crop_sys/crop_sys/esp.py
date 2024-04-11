import urllib.request

def fetch_data_from_esp():
    # Replace 'your_esp_ip_address' with the actual IP address of your ESP8266
    esp_ip_address = 'your_esp_ip_address'
    url = 'http://' + esp_ip_address + '/data'  # Assuming your ESP8266 serves data at this endpoint

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')  # Assuming data is encoded in UTF-8
            return data
    except Exception as e:
        print("Error fetching data:", e)
        return None

    # Example usage:
    data_from_esp = fetch_data_from_esp()
    if data_from_esp:
        print("Data from ESP:", data_from_esp)
        return data_from_esp;
    else:
        print("Failed to fetch data from ESP.")
        return 0;

def esp_func():
    esp_data=fetch_data_from_esp()
    res=["N","P","K","PH"]
    return res