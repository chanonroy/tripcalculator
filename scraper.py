import json
import requests
from bs4 import BeautifulSoup

class GasPrice(object):
    "Tool for gathering gas price data for Canadian provinces"

    def __init__(self):
        self.provinces = ['AB', 'SK', 'MB', 'ON', 'PE', 'NB', 'NS', 'QC', 'BC', 'NT', 'NF']
        self.values = []
        self.prices = {}

    def scrape_gas(self):
        "Grabs html from gas site for parsing"

        raw = requests.get('http://www.gasbuddy.com/CAN')
        soup = BeautifulSoup(raw.content, 'html.parser')

        for prov in self.provinces:
            self.get_by_province(soup=soup, province=prov)

        self.prices = dict(zip(self.provinces, self.values))
        print(self.prices)

    def get_by_province(self, soup, province):
        "Looping and parsing through html 'soup' object"

        # Soup DOM traversal
        value = soup.find(id=province)('div')[2].string.strip()
        self.values.append(value)


gas = GasPrice()
gas.scrape_gas()
