
# To run this script from terminal, cd to "/". Then, type "/Scripts/my_env/bin/python3.6 /Scripts/location.py"

import firebase_admin
import pyrebase
import requests
from bs4 import BeautifulSoup
from firebase_admin import credentials

# SETUP CONNECTION TO FIREBASE

config = {
    "apiKey": "concealed",
    "authDomain": "concealed",
    "databaseURL": "concealed",
    "storageBucket": "concealed",
    "serviceAccount": "concealed"
}

firebase = pyrebase.initialize_app(config)

# LOCATION CLASS USED TO POPULATE LOCATIONS ARRAY WITH tip VALUES

class Location():
    def __init__(self, name, tips):
        self.name = name
        self.tips = tips

locations_arr = []

# SCRAPE NORTHERN LOCATIONS

page = requests.get("https://wildlife.utah.gov/hotspots/reports_nr.php")
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

locations_1 = soup.find_all('div', class_='report1')
locations_2 = soup.find_all('div', class_='report2')

for location in locations_1:
    location_head = location.find('h4')
    location_ref = location_head.find('a')
    location_name = location_ref.get_text()
    tip_ref = location.find('p', class_=None)
    tip = tip_ref.get_text()
    # print(tip)
    new_location = Location(location_name, tip)
    locations_arr.append(new_location)

for location in locations_2:
    location_head = location.find('h4')
    location_ref = location_head.find('a')
    location_name = location_ref.get_text()
    tip_ref = location.find('p', class_=None)
    tip = tip_ref.get_text()
    # print(tip)
    new_location = Location(location_name, tip)
    locations_arr.append(new_location)

# SCRAPE CENTRAL LOCATIONS

page = requests.get("https://wildlife.utah.gov/hotspots/reports_cr.php")
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

locations_1 = soup.find_all('div', class_='report1')
locations_2 = soup.find_all('div', class_='report2')

for location in locations_1:
    location_head = location.find('h4')
    location_ref = location_head.find('a')
    location_name = location_ref.get_text()
    tip_ref = location.find('p', class_=None)
    tip = tip_ref.get_text()
    # print(tip)
    new_location = Location(location_name, tip)
    locations_arr.append(new_location)

for location in locations_2:
    location_head = location.find('h4')
    location_ref = location_head.find('a')
    location_name = location_ref.get_text()
    tip_ref = location.find('p', class_=None)
    tip = tip_ref.get_text()
    # print(tip)
    new_location = Location(location_name, tip)
    locations_arr.append(new_location)


# SCRAPE SOUTHEASTERN LOCATIONS

page = requests.get("https://wildlife.utah.gov/hotspots/reports_se.php")
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

locations_1 = soup.find_all('div', class_='report1')
locations_2 = soup.find_all('div', class_='report2')

for location in locations_1:
    location_head = location.find('h4')
    location_ref = location_head.find('a')
    location_name = location_ref.get_text()
    tip_ref = location.find('p', class_=None)
    tip = tip_ref.get_text()
    # print(tip)
    new_location = Location(location_name, tip)
    locations_arr.append(new_location)

for location in locations_2:
    location_head = location.find('h4')
    location_ref = location_head.find('a')
    location_name = location_ref.get_text()
    tip_ref = location.find('p', class_=None)
    tip = tip_ref.get_text()
    # print(tip)
    new_location = Location(location_name, tip)
    locations_arr.append(new_location)


# SCRAPE SOUTHERN LOCATIONS

page = requests.get("https://wildlife.utah.gov/hotspots/reports_sr.php")
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

locations_1 = soup.find_all('div', class_='report1')
locations_2 = soup.find_all('div', class_='report2')

for location in locations_1:
    location_head = location.find('h4')
    location_ref = location_head.find('a')
    location_name = location_ref.get_text()
    tip_ref = location.find('p', class_=None)
    tip = tip_ref.get_text()
    # print(tip)
    new_location = Location(location_name, tip)
    locations_arr.append(new_location)

for location in locations_2:
    location_head = location.find('h4')
    location_ref = location_head.find('a')
    location_name = location_ref.get_text()
    tip_ref = location.find('p', class_=None)
    tip = tip_ref.get_text()
    # print(tip)
    new_location = Location(location_name, tip)
    locations_arr.append(new_location)


# SCRAPE NORTHEASTERN LOCATIONS

page = requests.get("https://wildlife.utah.gov/hotspots/reports_ne.php")
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

locations_1 = soup.find_all('div', class_='report1')
locations_2 = soup.find_all('div', class_='report2')

for location in locations_1:
    location_head = location.find('h4')
    location_ref = location_head.find('a')
    location_name = location_ref.get_text()
    tip_ref = location.find('p', class_=None)
    tip = tip_ref.get_text()
    # print(tip)
    new_location = Location(location_name, tip)
    locations_arr.append(new_location)

for location in locations_2:
    location_head = location.find('h4')
    location_ref = location_head.find('a')
    location_name = location_ref.get_text()
    tip_ref = location.find('p', class_=None)
    tip = tip_ref.get_text()
    # print(tip)
    new_location = Location(location_name, tip)
    locations_arr.append(new_location)

for loc in locations_arr:
    source = "\nSource: https://wildlife.utah.gov/hotspots/"
    loc.tips += source
    print(f'{loc.name}, {loc.tips}')


# RETRIEVE LIST OF LOCATION NAMES TO COMPARE AGAINST WEB LIST

db = firebase.database()
locations_ref = db.child("locationsMasterSheet")
all_firebase_locations = locations_ref.get()

for firebase_location in all_firebase_locations.each():

    for location in locations_arr:

        if firebase_location.val()['locationName'] in location.name:
            #print(firebase_location.val())
            locations_ref.child("locationsMasterSheet").child(firebase_location.key()).update({'tips':location.tips})
