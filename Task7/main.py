from redis_cache import test, getCachedData, setCacheData
from json_output import output
from api_client import getData, writeData

def getWeather(city):
    key = f"weather:{city}"

    cachedData = getCachedData(key)
    if cachedData:
        print("📌 Veriler Redis'ten alındı!")
        return cachedData
    
    apiUrl = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}%2C%20Turkey?unitGroup=metric&key=K46E7NXMPKXGVB9P66U9ZYF7Z&contentType=json"
    print("🌍 API'den veri alınıyor...")
    weatherData = getData(apiUrl)
    if weatherData:
        setCacheData(key, weatherData)

    return weatherData

city = input("Please enter the city name: ")
output(getWeather(city))

# If you want to write the wheather data to a JSON file, run the code below.
#writeData(getWeather(city), city + ".json")

#Tüm Türkiye illerini Redis içerisine kayıt etmek için aşağıdaki kodu çalışıtır.
"""
turkey_cities = [
    "Adana", "Adiyaman", "Afyonkarahisar", "Agri", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin",
    "Aydin", "Balikesir", "Bartin", "Batman", "Bayburt", "Bilecik", "Bingol", "Bitlis", "Bolu", "Burdur",
    "Bursa", "Canakkale", "Cankiri", "Corum", "Denizli", "Diyarbakir", "Duzce", "Edirne", "Elazig", "Erzincan",
    "Erzurum", "Eskisehir", "Gaziantep", "Giresun", "Gumushane", "Hakkari", "Hatay", "Igdir", "Isparta", "Istanbul",
    "Izmir", "Kahramanmaras", "Karabuk", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kilis", "Kirikkale", "Kirklareli",
    "Kirsehir", "Kocaeli", "Konya", "Kutahya", "Malatya", "Manisa", "Mardin", "Mersin", "Mugla", "Mus",
    "Nevsehir", "Nigde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Sanliurfa", "Siirt", "Sinop",
    "Sirnak", "Sivas", "Tekirdag", "Tokat", "Trabzon", "Tunceli", "Usak", "Van", "Yalova", "Yozgat", "Zonguldak"
]
for city in turkey_cities:
    output(getWeather(city))"""