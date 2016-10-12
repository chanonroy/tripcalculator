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

    version = root[0][0].text       # Auto 5-spd, 4 cyl, 2.4 L
    vehicle_id = root[0][1].text    # 21960

    # Need to properly iterate through all car options, not just first (TODO)
    return vehicle_id, version

print(get_id())


def get_gas():
    """ Get Gas info from fueleconomy.gov XML API """


def uber():
    """ Return Uber fare and time estimate """

    url = "https://api.uber.com/v1/estimates/price"

    parameters = {}

    response = requests.get(url, params=parameters)
    data = response.json()

    print(response)
    print(data)
