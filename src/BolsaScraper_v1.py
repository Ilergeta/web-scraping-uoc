# Imports needed libraries
import requests
import csv
from bs4 import BeautifulSoup

# Loads webpage

# TODO - cercar l'empresa desitjada
#      - poder seleccionar les dates desitjades

page = requests.get('http://www.bolsamadrid.es/esp/aspx/Empresas/InfHistorica.aspx?ISIN=ES0105200002')
soup = BeautifulSoup(page.content, 'html.parser')

# Reads data
taula = soup.find(id="ctl00_Contenido_tblDatos")

# Ticker
ticker = [soup.find(class_= 'FrmBusq').find_all('td')[10].string.strip()]

# Company name
company = [soup.find(class_= 'FrmBusq').find_all('td')[8].string.strip()]

# Heading row
first_row = [title.string for title in taula.find_all('th')]

# Other rows
content = [[element.string for element in row.find_all('td')] for row in taula.find_all('tr')[1:]]

# Writes output csv file in 'output' dir with ticker company as filename
with open('output/'+ticker[0]+'.csv', 'w', newline='') as csvfile:
    bolsa_writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    bolsa_writer.writerow(company)
    bolsa_writer.writerow(first_row)
    bolsa_writer.writerows(content)    
