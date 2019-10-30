# Imports needed libraries
import requests
import csv
from bs4 import BeautifulSoup

class BolsaScraper():
    
    def __init__(self):
        # Definim l'url basica de la web
        self.path = 'http://www.bolsamadrid.es'
        
    # TODO - cercar l'empresa desitjada
#      - poder seleccionar les dates desitjades
    def trobarEmpresa(self, nomEmpresa):
        """
        Aquesta funció retorna el path final de l'empresa que busquem
        """
        url = self.path + "/esp/aspx/Empresas/Empresas.aspx"
        
        page = requests.get(url)
        
        soup = BeautifulSoup(page.content, 'html.parser')
        
        # Reads data
        taula = soup.find(id="ctl00_Contenido_tblEmisoras")
        
        print(taula)
        
    def dadesEmpresa(self):
        """
        Retorna les dades de l'empresa seleccionada
        """
        # Loads webpage -- Serà variable vindrà donada per la funció anterior
        
        url = self.path +'/esp/aspx/Empresas/InfHistorica.aspx?ISIN=ES0105200002'
        
        page = requests.get(url)
        
        soup = BeautifulSoup(page.content, 'html.parser')
        
        # Reads data
        taula = soup.find(id="ctl00_Contenido_tblDatos")
        
        # Ticker
        ticker = [soup.find(class_= 'FrmBusq').find_all('td')[10].string.strip()]
        
        # Company name
        self.company = [soup.find(class_= 'FrmBusq').find_all('td')[8].string.strip()]
        
        # Heading row
        self.first_row = [title.string for title in taula.find_all('th')]
        
        # Other rows
        self.content = [[element.string for element in row.find_all('td')] for row in taula.find_all('tr')[1:]]
        
        
        self.data2csv(ticker[0])
            
    def data2csv(self, filename):
        with open("../data/"+filename+'.csv', "w+", newline='') as csvfile:
            bolsa_writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            bolsa_writer.writerow(self.company)
            bolsa_writer.writerow(self.first_row)
            bolsa_writer.writerows(self.content)
        

def main():
    
    bolsa = BolsaScraper()
    
    bolsa.dadesEmpresa()
    
    bolsa.trobarEmpresa("ABENGOA, S.A.")
    
if __name__ == "__main__":
    main()
    
















