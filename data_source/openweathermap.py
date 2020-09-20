"""
Open weather map data source
https://openweathermap.org/
"""

import requests
import settings


def get_points(postcode):
    weather_query = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?zip={postcode},us&appid={settings.OPENWEATHERMAP_KEY}&units=metric"
    )
    weather_query.raise_for_status()
    weather = weather_query.json()

    return [
        {
            "measurement": "weather",
            "tags": {"location": weather["name"], "postcode": postcode},
            "time": weather["dt"] * 1000000000,
            "fields": {
                "temp": float(weather["main"]["temp"]),
                "feels_like": float(weather["main"]["feels_like"]),
                "temp_min": float(weather["main"]["temp_min"]),
                "temp_max": float(weather["main"]["temp_max"]),
                "pressure": weather["main"]["pressure"],
                "humidity": float(weather["main"]["humidity"]),
            },
        }
    ]
