# -*- coding: utf-8 -*f
from bolsaScraper import BolsaScraper

scraper = BolsaScraper()


# Write here companie or companies that you need do web scraping
companies = ["aena", "SABADELL"]

for companie in companies:
    # Obtained url
    url = scraper.trobarEmpresa(companie)
    # Scraping and saving informaiton about the companies
    scraper.dadesEmpresa(url)
    

# Aquí aniran totes les funcions amb l'estructura següent:
# scraper.funció(parametres)
