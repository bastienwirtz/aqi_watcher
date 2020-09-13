"""
Purpleair data source
https://www2.purpleair.com/community/faq#!hc-access-the-json
"""

import requests


def get_points(sensor_id):
    purple_query = requests.get(f"https://www.purpleair.com/json?show={sensor_id}")
    purple_query.raise_for_status()
    purple = purple_query.json()

    points = []
    for sensor in purple["results"]:
        points.append(
            {
                "measurement": "purpleair",
                "tags": {"location": sensor["Label"], "sensor": sensor_id},
                "time": sensor["LastSeen"] * 1000000000,
                "fields": {
                    "pm2_5": float(sensor["pm2_5_atm"]),
                    "pm1_0": float(sensor["pm1_0_atm"]),
                    "pm10_0": float(sensor["pm10_0_atm"]),
                },
            }
        )
    return points
