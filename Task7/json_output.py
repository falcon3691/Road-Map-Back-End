def output(json_data):
    try:
        print(f"Konum: {json_data['resolvedAddress']}")
        print(f"Açıklama: {json_data['description']}")

        for weather_data in json_data["days"]:
            
            # 📜 Açıklamaya Göre Emoji Seçimi
            description_emojis = [
                ("clear", "☀️"), 
                ("sunny", "☀️"),
                ("partly cloudy", "⛅"),
                ("cloudy", "☁️"),
                ("rain", "🌧️"),
                ("showers", "🌦️"),
                ("thunderstorm", "⛈️"),
                ("storm", "🌩️"),
                ("fog", "🌫️"),
                ("snow", "❄️"),
            ]

            # Açıklamaya uygun emoji bulma
            description_text = weather_data["description"].lower()
            matched_emoji = "🌍"  # Varsayılan emoji
            for keyword, emoji in description_emojis:
                if keyword in description_text:
                    matched_emoji = emoji
                    break  # İlk eşleşmede çık

            # 🌤️ Hava Durumu İçin Emoji Seçimi
            weather_icons = {
                "Clear": "☀️", 
                "Sunny": "☀️", 
                "Cloudy": "☁️", 
                "Partially cloudy": "⛅",
                "Rain": "🌧️", 
                "Light rain": "🌦️",
                "Thunderstorm": "⛈️", 
                "Storm": "🌩️",
                "Snow": "❄️", 
                "Fog": "🌫️"
            }
            weather_icon = weather_icons.get(weather_data["conditions"], "🌍")  # Varsayılan emoji 🌍

            if weather_data["tempmax"] >= 30:
                temp_status = "🔥 Çok sıcak bir gün!"
            elif weather_data["tempmax"] >= 20:
                temp_status = "😎 Ilık bir hava."
            elif weather_data["tempmax"] >= 10:
                temp_status = "🌤️ Serin bir gün."
            else:
                temp_status = "🥶 Soğuk hava."

            # 💨 Rüzgar Durumu
            if weather_data["windspeed"] >= 50:
                wind_status = "🌪️ Çok şiddetli rüzgar!"
            elif weather_data["windspeed"] >= 20:
                wind_status = "🌬️ Kuvvetli rüzgar."
            elif weather_data["windspeed"] >= 5:
                wind_status = "💨 Hafif esinti."
            else:
                wind_status = "🍃 Rüzgarsız sakin hava."

            # 💧 Nem Durumu
            if weather_data["humidity"] >= 80:
                humidity_status = "💦 Nem çok yüksek, bunaltıcı olabilir."
            elif weather_data["humidity"] >= 50:
                humidity_status = "🙂 Orta seviyede nem."
            else:
                humidity_status = "🏜️ Kuru hava, düşük nem."

            # 🌅 Gün Doğumu / Gün Batımı Emojileri
            sunrise_emoji = "🌅"
            sunset_emoji = "🌇"

            # 📜 Çıktıyı Yazdırma
            print(f"📅 Tarih: {weather_data['datetime']}")
            print(f"{matched_emoji} Hava Durumu: {weather_data['conditions']}")
            print(f"🌡️ Maksimum Sıcaklık: {weather_data['tempmax']}°C {temp_status}")
            print(f"🌡️ Minimum Sıcaklık: {weather_data['tempmin']}°C")
            print(f"💧 Nem: {weather_data['humidity']}% {humidity_status}")
            print(f"💨 Rüzgar Hızı: {weather_data['windspeed']} km/h {wind_status}")
            print(f"{sunrise_emoji} Gün Doğumu: {weather_data['sunrise']} {sunset_emoji} Gün Batımı: {weather_data['sunset']}")
            print(f"📜 Açıklama: {weather_icon} {weather_data['description']}")
            print("-"*75)
    except TypeError as e:
        print(f"❌ Couldn't get wheather data, check city name.\n"+
               f"Error: {e}")

