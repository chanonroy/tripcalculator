"""
My own implementation of a Hackathon idea
Simple script to return cost and time breakdown for Uber, Driving, and Transit travel options

Developed by Chanon Roy. Shout-out to Team Omega (Budweiser Hackathon '16 - Toronto)
"""

import requests
import xml.etree.ElementTree as ET


def get_location():
    """  """


def get_id():
    """ Get vehicle ID for fueleconomy.gov XML API """

    # year = input("What year?\n").lower()
    # make = input("What is the make?\n").lower()
    # model = input("What is the model?\n").lower()

    year = 2006
    make = 'honda'
    model = 'accord'

    url = "http://fueleconomy.gov/ws/rest/vehicle/menu/options?year={}&make={}&model={}".format(year, make, model)
    r = requests.get(url)
    tree = ET.fromstring(r.content)
    print(tree)

    #TODO: Parse XML


def uber():
    """ Return Uber fare and time estimate """

    url = "https://api.uber.com/v1/estimates/price"

    parameters = {}

    response = requests.get(url, params=parameters)
    data = response.json()

    print(response)
    print(data)
