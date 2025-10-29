import requests
import json
from requests.exceptions import RequestException
from json.decoder import JSONDecodeError

def get_weather_details(city, api_key):
    """
    Fetch weather details for a given city using OpenWeatherMap API
    
    Args:
        city (str): Name of the city
        api_key (str): OpenWeatherMap API key
    
    Returns:
        str: JSON formatted weather data or error message
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
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Parse JSON response
        weather_data = response.json()
        
        # Format and return the weather data
        return json.dumps(weather_data, indent=2)
        
    except requests.exceptions.Timeout:
        return "Error: Request timed out. Please try again."
    
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to API. Check your network connection."
    
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            return "Error: Invalid API key. Please check your API key."
        elif response.status_code == 404:
            return f"Error: City '{city}' not found."
        else:
            return f"Error: HTTP error occurred: {http_err}"
    
    except JSONDecodeError:
        return "Error: Could not parse the API response."
    
    except Exception as e:
        return f"Error: An unexpected error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    API_KEY = "a9175a5c01a2604472cea8e2911eb84f"  # Replace with your actual API key
    city_name = input("Enter city name: ")
    
    result = get_weather_details(city_name, API_KEY)
    print(result)