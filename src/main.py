# -*- coding: utf-8 -*f
from bolsaScraper import BolsaScraper

scraper = BolsaScraper()


# Write here companie or companies that you need do web scraping
companies = ["SAN", "SABADELL"]

# Start date is manadatory argument
start_date = "24/06/2019"
# End date is optional argument if not use the scraper use today as end date
end_date = "10/11/2019"

for companie in companies:
    # Obtained url
    url = scraper.trobarEmpresa(companie)
    # Scraping and saving informaiton about the companies
    scraper.dadesEmpresa(url, start_date)
    

# Aquí aniran totes les funcions amb l'estructura següent:
# scraper.funció(parametres)
