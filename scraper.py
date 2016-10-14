import json
import requests
from bs4 import BeautifulSoup

class GasPrice(object):
    "Tool for gathering gas price data for Canadian provinces"

    def __init__(self):
        self.prices = {
            'AB': None,
            'SK': None,
            'MB': None,
            'ON': None,
            'PE': None,
            'NB': None,
            'NS': None,
            'QC': None,
            'BC': None,
            'NT': None,
            'NF': None,
        }

    def scrape_gas(self):
        "Grabs html from gas site for parsing"

        raw = requests.get('http://www.gasbuddy.com/CAN')
        soup = BeautifulSoup(raw.content, 'html.parser')

        # self.final = {province: self.get_by_province(soup, province for province in self.provinces)}

        for key in self.prices.items():
            self.get_by_province(soup, key)

    def get_by_province(self, soup, province):
        "Looping and parsing through html 'soup' object"

        # Soup DOM traversal
        value = soup.find(id=province)('div')[2].string.strip()
        self.prices[province] = value
