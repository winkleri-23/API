import requests

# Funkce pro získání aktuálního počasí
def get_weather(city_name):
    # Base URL Open-Meteo API
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}"
    weather_url = "https://api.open-meteo.com/v1/forecast"
    
    # Získání souřadnic města
    geocoding_response = requests.get(geocoding_url)
    if geocoding_response.status_code != 200 or not geocoding_response.json().get("results"):
        return "Město nebylo nalezeno, zkontroluj zadání."
    
    city_data = geocoding_response.json()["results"][0]
    latitude, longitude = city_data["latitude"], city_data["longitude"]
    
    # Získání počasí
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }
    weather_response = requests.get(weather_url, params=params)
    
    if weather_response.status_code == 200:
        weather_data = weather_response.json()["current_weather"]
        temperature = weather_data["temperature"]
        wind_speed = weather_data["windspeed"]
        return f"Aktuální teplota v {city_name} je {temperature}°C a rychlost větru je {wind_speed} km/h."
    else:
        return "Nepodařilo se načíst počasí, zkus to znovu."

# Spuštění programu
if __name__ == "__main__":
    city = input("Zadej název města: ")
    print(get_weather(city))
