import requests
import time

API_KEY = "YOUR_API_KEY"
CITY = "Tel Aviv"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def get_weather():
    response = requests.get(URL)
    response.raise_for_status()
    return response.json()

def automation():
    data = get_weather()
    temp = data["main"]["temp"]
    condition = data["weather"][0]["description"]

    print(f"Temperature: {temp}°C, Condition: {condition}")

    if temp > 30:
        print("Hot outside!")
    elif temp < 15:
        print("Cold outside!")
    else:
        print("Cool weather!")

if __name__ == "__main__":
    while True:
        automation()
        time.sleep(3600)  # שעה
