import requests
from datetime import datetime

api_key = 'ea91d929f1086763d258cdb835285fc3'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-------------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  :", weather_desc)
print("Current Humidity      :", hmdt, '%')
print("Current wind speed    :", wind_spd, 'kmph')

file = open("weather.txt", "w")
file.write("weather details for :" + location)
file.write("\n")
file.write("temperature :" + str(temp_city))
file.write("\n")
file.write('description :' + weather_desc)
file.write("\n")
file.write("humidity :" + str(hmdt))
file.write("\n")
file.write("wind speed(KmpH) :" +str(wind_spd))
file.close()
