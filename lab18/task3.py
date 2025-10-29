import requests
from requests.exceptions import RequestException

def display_weather(city, api_key):
    """
    Fetch and display specific weather details for a given city
    
    Args:
        city (str): Name of the city
        api_key (str): OpenWeatherMap API key
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    try:
        # Make API request
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'  # For temperature in Celsius
        }
        
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        
        # Parse response and extract specific fields
        weather_data = response.json()
        
        # Format and display the weather information in bullet points
        print(f"City: {weather_data['name']}")
        print(f"• Temperature: {weather_data['main']['temp']}°C")
        print(f"• Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather: {weather_data['weather'][0]['description'].title()}")
        
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")
    
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check your network connection.")
    
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("Error: Invalid API key. Please check your API key.")
        elif response.status_code == 404:
            print(f"Error: City '{city}' not found.")
        else:
            print(f"Error: HTTP error occurred: {http_err}")
    
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    API_KEY = "a9175a5c01a2604472cea8e2911eb84f"  # Replace with your actual API key
    city_name = input("Enter city name: ")
    
    display_weather(city_name, API_KEY)