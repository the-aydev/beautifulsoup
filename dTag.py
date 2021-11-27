import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://weather.com/weather/today/l/fa24eb9f1a11df993ff36bc2958ee60169b8e4e3eb5f987649dc2807dc89b1b8')
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.title)

header = soup.find(class_='CurrentConditions--location--1Ayv3').get_text()
print(header)

temperature_value = soup.find(
    class_='CurrentConditions--tempValue--3KcTQ').get_text()
# print("Weather today >>>>> " + temperature_value)

temperature_desc = soup.find(
    class_='CurrentConditions--phraseValue--2xXSr').get_text()
# print(temperature_desc)
print('------------------------------------')

print("Weather today >>>>> " + temperature_value +
        " and is " + temperature_desc + " today!")
print('------------------------------------')

body = [soup.find(
    class_='WeatherTable--columns--3q5Nx WeatherTable--wide--YogM9').get_text() for body in soup]

print('\n'.join(body[0]))
