[![Docker Build Status](https://img.shields.io/docker/cloud/build/tg44/weather2mqtt?style=flat-square)](https://hub.docker.com/r/tg44/weather2mqtt)

# Weather2MQTT

Gets weather data from [openweathermap](https://openweathermap.org/) and publishes to MQTT.

### Docker
```
docker run \
-it \
-e MQTT_HOST=example.com \
-e MQTT_PORT=1883 \
-e MQTT_TOPIC=weather/stats \
-e CITY_ID=2643743 \
-e APP_ID=appid \
tg44/weather2mqtt
```

You need to register to [openweathermap](https://openweathermap.org/) for an api key.

Also you need to search your city in the site, and copy-paste the cityid from the url.

For other language than english you can set an `API_LANG` env var, the options are at the bottom of [this page](https://openweathermap.org/current)

The default `UNITS` is `metric`, the other two options are `imperial` or `standard` (this will return temp data in Kelvin).

`SCHEDULE` is an optional setting to schedule with [crython](https://github.com/ahawker/crython) expression (default is 10 minutes).
