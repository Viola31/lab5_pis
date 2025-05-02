import requests

API_KEY = "65550319c4bb65e2e0de54b60adfb86a"

def get_weather_by_city_name(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_weather_for_multiple_cities(cities):
    results = []
    for city in cities:
        data = get_weather_by_city_name(city)
        if data:
            results.append((city, data))
    return results

def print_weather_info(city, data):
    print(f"Погода в місті {city}: {data['weather'][0]['description']}")
    print(f"Температура: {data['main']['temp']}°C")
    print(f"Швидкість вітру: {data['wind']['speed']} м/с")
    print("-" * 40)

if __name__ == "__main__":
    print("Оберіть спосіб доступу:")
    print("1 - Для кількох міст")
    choice = input("Ваш вибір (1): ")

    if choice == "1":
        cities = input("Введіть міста через кому: ").split(",")
        results = get_weather_for_multiple_cities([c.strip() for c in cities])
        if results:
            for city, data in results:
                print_weather_info(city, data)
        else:
            print("Не вдалося отримати дані для деяких міст.")
    else:
        print("Невірний вибір.")

