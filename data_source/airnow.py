"""
Airnow data source
https://www.airnow.gov/
"""

import pytz
import requests
import settings
from datetime import datetime


def get_points(postcode):
    aqi_query = requests.get(
        f"https://airnowapi.org/aq/observation/zipCode/current?zipCode={postcode}&format=json&api_key={settings.AIRNOW_KEY}"
    )
    aqi_query.raise_for_status()
    aqi = aqi_query.json()

    points = []
    for entry in aqi:
        report_date = pytz.timezone("US/Pacific").localize(
            datetime.strptime(entry["DateObserved"].strip(), "%Y-%m-%d").replace(
                hour=entry["HourObserved"]
            )
        )
        report_date = int(report_date.astimezone(pytz.utc).timestamp()) * 1000000000

        points.append(
            {
                "measurement": entry["ParameterName"],
                "tags": {"location": entry["ReportingArea"], "postcode": postcode},
                "time": report_date,
                "fields": {
                    "aqi": entry["AQI"],
                    "zone": entry["Category"]["Number"],
                    "libelle": entry["Category"]["Name"],
                },
            }
        )

    return points
