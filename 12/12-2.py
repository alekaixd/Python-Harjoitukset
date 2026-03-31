import requests

# http://api.openweathermap.org/geo/1.0/direct?q=Kirkkonummi&limit=1&appid=c7b3b1df65d1fcb428804c44617b37f2
# eka tee api call jotta saat longitude ja latitude kaupungista
apiKey = "c7b3b1df65d1fcb428804c44617b37f2"


def Main():
    query = input("Anna paikkakunta/kaupunki: ")
    try:
        paikkakunta = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={query}&limit=1&appid={apiKey}")
        if paikkakunta.status_code == 200:
            lat = paikkakunta.json()[0]["lat"]
            lon = paikkakunta.json()[0]["lon"]

            weather = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}")
            output = weather.json()
            desc = output["weather"][0]["description"]
            tempMin = output["main"]["temp_min"] - 273.15
            tempMax = output["main"]["temp_max"] - 273.15
            feelsLike = output["main"]["feels_like"] - 273.15

            print(f"{desc}\nMax Temp: {tempMax:.1f}°C\nMin Temp: {
                  tempMin:.1f}°C\nFeels like: {feelsLike:.1f}°C")
    except requests.exceptions.RequestException as e:
        print(f"Api pyyntö epäonnistui\n{e}")
        return


# sitten katso sää data
Main()
