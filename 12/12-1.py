import requests

try:
    apiRequest = requests.get("https://api.chucknorris.io/jokes/random")
    if apiRequest.status_code == 200:
        print(apiRequest.json()["value"])
except requests.exceptions.RequestException as e:
    print(f"Hakua ei voitu suorittaa\n{e}")
