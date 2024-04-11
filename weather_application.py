import random

def get_weather(city):
    # Simulate getting weather data (for demonstration purposes)
    temperatures = {
        'New York': random.randint(-10, 30),
        'London': random.randint(-5, 25),
        'Tokyo': random.randint(5, 35),
        'Sydney': random.randint(10, 40),
    }

    descriptions = {
        'New York': 'Cloudy',
        'London': 'Rainy',
        'Tokyo': 'Sunny',
        'Sydney': 'Partly cloudy',
    }

    if city in temperatures:
        return {'temperature': temperatures[city], 'description': descriptions[city]}
    else:
        return None

def main():
    city = input("Enter the city name: ")
    weather = get_weather(city)

    if weather:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
    else:
        print("City not found or weather data unavailable.")

if __name__ == "__main__":
    main()
