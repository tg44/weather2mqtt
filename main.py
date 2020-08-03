import os, json, crython, requests, traceback
from paho.mqtt import publish

print("started")
topic = os.environ.get('MQTT_TOPIC')
host = os.environ.get('MQTT_HOST')
port = int(os.getenv('MQTT_PORT', '1883'))

cityId = os.environ.get('CITY_ID')
appId = os.environ.get('APP_ID')
units = os.getenv('UNITS', 'metric') #standard, metric, imperial
lang = os.getenv('API_LANG', 'en')

schedule = os.getenv('SCHEDULE')

unitsQuery = '' if units == 'standard' else f'units={units}&'
url = f'http://api.openweathermap.org/data/2.5/weather?id={cityId}&{unitsQuery}lang={lang}&appid={appId}'
print(url)

@crython.job(expr=schedule)
def process():
    try:
        r = requests.get(url)
        data = r.json()
        jsonString = json.dumps(data)
        if not 'dt' in data or not 'main' in data or not 'temp' in data['main']:
            print("OpenWeatherMap error: " + jsonString)
        else:
            print(jsonString)
            publish.single(topic, jsonString, hostname=host, port=port)
    except requests.exceptions.RequestException as e:
        print("OpenWeatherMap not available: " + str(e))
    except Exception as e:
        print("Unknown error:" + str(e))
        traceback.print_exc()

if __name__ == "__main__":
    if schedule is None:
        process()
    else:
        crython.start()
        crython.join()
