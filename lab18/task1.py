import requests
import json

def get_weather_details(city, api_key):
    """
    Fetch weather details for a given city using OpenWeatherMap API
    
    Args:
        city (str): Name of the city
        api_key (str): OpenWeatherMap API key
    
    Returns:
        str: JSON formatted weather data
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Make API request
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # For temperature in Celsius
    }
    
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    
    # Return formatted JSON string
    return json.dumps(weather_data, indent=2)

if __name__ == "__main__":
    API_KEY = "a9175a5c01a2604472cea8e2911eb84f"  # Replace with your actual API key
    city_name = input("Enter city name: ")
    
    result = get_weather_details(city_name, API_KEY)
    print(result)