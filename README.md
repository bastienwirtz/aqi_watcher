# aqi_watcher

Save air quality & weather data from various source info any influxdb database.
Nothing fancy here, just a basic script, written between two breaths of fresh PM2.5 particules from the ongoing wildfires.

## requirements
- python 3.6+
- influxdb 1.7+

## Get started
- `pip install -r requirements.txt` (idealy in a virtualenv or something)
- Open `settings.py` and configure your influxdb server & api keys. 
- Run it regularly (Example, cron every 10min: `*/10 * * * * /srv/aqi_watcher/env/bin/python /srv/aqi_watcher/aqi.py`)
- Do whatever you want with the data. My grafana dashboard is exported in `grafana-aqi-dashboard.json` 

Happy hacking :v: