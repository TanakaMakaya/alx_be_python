import requests

def get_weather(city):
    # Using a free weather API
    url = f"http://wttr.in/{city}?format=j1"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        current = data['current_condition'][0]
        
        print(f"Weather in {city}:")
        print(f"Temperature: {current['temp_C']}°C")
        print(f"Condition: {current['weatherDesc'][0]['value']}")
    else:
        print("Could not fetch weather data")


city = input("Enter a city to get the weather: ")

get_weather(city)