import requests

from bs4 import BeautifulSoup

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=34.05361000000005&lon=-118.24549999999999#.X5hsX4gzbIU')
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all('a'))
week = soup.find(id="seven-day-forecast-body")
# print(week)

items = week.find_all(class_='tombstone-container')
# print(items[0])

print(items[3].find(class_='period-name').get_text())
print(items[3].find(class_='short-desc').get_text())
print(items[3].find(class_='temp temp-high').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp temp-high').get_text() for item in items]

print(period_names)
print(short_descriptions)
#print(temperatures)

# 4:24
