import json
import requests
def getData(apiUrl):
    try:
        response = requests.get(apiUrl)
        if response.status_code == 200:
            json_data = response.json()
            return json_data
    except Exception as e:
        print(f"❌ Couldn't get wheather data, check internet connection.\n"+
               f"Error: {e}")
        return None
    
def writeData(apiUrl):
    response = requests.get(apiUrl)
    if response.status_code == 200:
        json_data = response.json()
    with open("veri.json","w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=4, ensure_ascii= False)
    
