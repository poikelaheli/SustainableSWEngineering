import os
import requests
import json
import ssl
import time
import datetime

intencityUrl = 'https://api.carbonintensity.org.uk/intensity'
weatherUrl = 'http://api.weatherapi.com/v1/current.json'

dataset = []
error = []

apiKey = '$API_KEY'
queryParam = 'London'

intensityData = {}
weatherData = {}

print(f'Date: {datetime.datetime.now()} \n')

try: 
  headers = {
    'Accept': 'text/json'
  }
  res = requests.get(intencityUrl, params={}, headers=headers)

  p = res.text.find('\r\n')
  if p >= 0:
    textData = '{' + res.text[p:]
    intensityData = json.loads(textData) 
    data = intensityData['data'][0]
    intensity = data['intensity']
    actual = intensity['actual']
    index = intensity['index']
    print('Carbon intensity:')
    print(f'value: {str(actual)}, index: {index} \n')

except requests.HTTPError as err:
  if err.code == 404:
    print(err)
except Exception as err:
  print(f'Error: {err}')

try: 
  headers = {
    'Accept': 'text/json'
  }
  params = {
    'key' : apiKey,
    'q' : queryParam
  }
  res = requests.get(weatherUrl, params=params, headers=headers)

  p = res.text.find('\r\n')
  textData = res.text
  if p >= 0:
    textData = res.text[p:]
  weatherData = json.loads(textData)
  location = weatherData['location']
  name = location['name']
  country = location['country']
  current = weatherData['current']
  tempC = current['temp_c']
  tempF = current['temp_f']
  humidity = current['humidity']
  windDir = current['wind_dir']
  windKph = current['wind_kph']
  windMph = current['wind_mph']
  cloud = current['cloud']

  print('Weather:')
  print(f'location: {name}, {country}')
  print('Weather conditions:')
  print(f'temperature: {tempC} C / {tempF} F')
  print(f'humidity: {humidity} %')
  print(f'wind direction and speed: {windDir}, {windKph} kph / {windMph} mph')
  print(f'clouds: {cloud} %')



except requests.HTTPError as err:
  if err.code == 404:
    print(err)
except Exception as err:
  print(f'Error: {err}')

