"""
My own implementation of a Hackathon idea
Simple script to return cost and time breakdown for Uber, Driving, and Transit travel options

Developed by Chanon Roy. Shout-out to Team Omega (Budweiser Hackathon '16 - Toronto)
"""

import requests
import xml.etree.ElementTree as ET


def get_id():
    """ Get vehicle ID for fueleconomy.gov XML API """

    # Hardcoded for now
    year = 2006
    make = 'honda'
    model = 'accord'

    url = "http://fueleconomy.gov/ws/rest/vehicle/menu/options?year={}&make={}&model={}".format(year, make, model)
    r = requests.get(url)
    root = ET.fromstring(r.content)

    version = root[0][0].text       # 'Auto 5-spd, 4 cyl, 2.4 L'
    vehicle_id = root[0][1].text    # '21960'

    # Need to properly iterate through all car options, not just first (TODO)
    return vehicle_id


def get_gas():
    """ Get Gas info from fueleconomy.gov XML API """

    vehicle_id = 21960 # get_id()

    url = "http://www.fueleconomy.gov/ws/rest/ympg/shared/ympgVehicle/{}".format(vehicle_id)
    r = requests.get(url)
    root = ET.fromstring(r.content)

    avg_mpg = root[0].text         # 27.89997198
    city_percent = root[1].text    # 39
    highway_percent = root[2].text # 61
    max_mpg = root[3].text         # 38
    min_mpg = root[4].text         # 20

    print(avg_mpg)

get_gas()


def uber():
    """ Return Uber fare and time estimate """

    url = "https://api.uber.com/v1/estimates/price"

    parameters = {}

    response = requests.get(url, params=parameters)
    data = response.json()

    print(response)
    print(data)
