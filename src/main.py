# -*- coding: utf-8 -*f
import argparse
import sys
from bolsaScraper import BolsaScraper

scraper = BolsaScraper()


parser = argparse.ArgumentParser()

parser.add_argument("--companies", nargs='+')
parser.add_argument("--start")
parser.add_argument("--end")

known_args = parser.parse_known_args(sys.argv)

for key, value in parser.parse_args()._get_kwargs():
    if key == "companies":
        companies = value
    if key == "start":
        start_date = value
    if key == "end":
        end_date = value
print(companies, start_date, type(start_date), end_date)

if end_date == None:
    for companie in companies:
        # Obtained url
        url = scraper.trobarEmpresa(companie)
        # Scraping and saving informaiton about the companies
        scraper.dadesEmpresa(url, start_date)
else:
    for companie in companies:
        # Obtained url
        url = scraper.trobarEmpresa(companie)
        # Scraping and saving informaiton about the companies
        scraper.dadesEmpresa(url, start_date, end_date)
    

