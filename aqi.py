#!/usr/bin/env python3

import settings

from influxdb import InfluxDBClient
from data_source import openweathermap, airnow, purpleair

purpleair_sensors = settings.PURPLEAIR_SENSORS.split(",")
points = []

# Get weather
try:
    points += openweathermap.get_points(settings.POSTCODE)
except Exception as error:
    print("fail to get weather data: %s", error)

# Get Air Quality Index
try:
    points += airnow.get_points(settings.POSTCODE)
except Exception as error:
    print("fail to get Air Quality data: %s", error)

# Get Air Quality Index from purple air
try:
    for sensor in purpleair_sensors:
        points += purpleair.get_points(sensor)
except Exception as error:
    print("fail to get Purple Air data: %s", error)

influx = InfluxDBClient(
    settings.INFLUXDB["URL"],
    settings.INFLUXDB["PORT"],
    settings.INFLUXDB["USER"],
    settings.INFLUXDB["PASSWORD"],
    settings.INFLUXDB["DB"],
    ssl=settings.INFLUXDB["SSL"],
    verify_ssl=settings.INFLUXDB["SSL"],
)

influx.write_points(points)
