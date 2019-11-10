# -*- coding: utf-8 -*f
import requests
import csv
import psutil
import platform
import os
from selenium import webdriver
from bs4 import BeautifulSoup

class BolsaScraper():
    
    def __init__(self):
        # Definim l'url basica de la web
        self.path = 'http://www.bolsamadrid.es'
        self.dir_path = os.path.dirname(os.path.abspath(__file__))
        

    def trobarEmpresa(self, nomEmpresa):
        """
        Aquesta funció retorna el path final de l'empresa que busquem
        """
        url = self.path + "/esp/aspx/Empresas/Empresas.aspx"
        
        headers = {
                'Accept': 'text/html,application/xhtml+xml, \
                application/xml;q=0.9,*/*;q=0.8',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'http://www.bolsamadrid.es',
                'Accept-Encoding': 'gzip, deflate',
                'Upgrade-Insecure-Requests': '1',
                'Host': 'www.bolsamadrid.es',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) \
                AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 \
                Safari/605.1.15',
                'Accept-Language': 'es-es',
                'Connection': 'keep-alive'
                }
        
        page = 0
        
        linkEmp = ''
        
        # This loop run the all pages in a table until find the page that 
        # contain the name of entity 
        while not linkEmp:
            # This data is use to do a post requests and contain the table page
           data = {
                '__EVENTTARGET': '',
                '__EVENTARGUMENT': '',
                '__VIEWSTATE': 'ELOG9j+dXlB0neVne96qoQt5YBD99TrZEhhPUlG2uUo1xqC3cym00LyqoRQoi8x0RzaWp7RCOsxDjW3KsByfdG9p8VkpQGQaFjJGdNLbKjGy3H8jqKwTRvW/hDQPsv3aDesfZAxZHi3QO89pBa1Kr9diSmSxfx7PBYisYbL74FTK3gWFDcwXe/pkaTj34dUzsoLi7g==',
                '__VIEWSTATEGENERATOR': '65A1DED9',
                '__EVENTVALIDATION': '74YPg3B3Klx410ErZzrI+oUgqOATLDvnA/jY9wSgYwwIVARtwCmEEfVHIgrrd/7qdwqFGaen89VfmYLafxEGEwc5TeJDIkKP9Il8ZpD002wYxJgmruY/YdpYGmiey3RQFegiFLG0vgY/dZH9ObURK+wLPzhz7nTNRuQOdaaC9TgQX8oH51Layu04bs4EvFmtZF4gzDIRcYEba88DVy8pzykMaxB5cT353XUYf47IPnNFdXHC',
                'ctl00$Contenido$GoPag': str(page)
                }
           # Post request to a url using header and data defined before
           response = requests.post(url, headers=headers, data=data)
           # Create soup with the html response from page
           soup = BeautifulSoup(response.content, 'html.parser')
           # Find links in the page
           links = soup.find_all('a')
           # This loop find link that contain the name of company and return the
           # page that contain information about this
           for link in links:
               # Find link of all companies
               if nomEmpresa.upper() in link.text:
                   linkEmp = link.attrs['href']
           # This if control that the while are not infinite in case that not
           # find any match with the name (Only read the all page of the table)
           if page > 7:
               print("No se encuentra la empresa")
               break
           page = page + 1
           
           
        # Define dict to change part of url to goes directly to page that
        # contain data 
        urlchange = {
                "FichaValor": "InfHistorica"
                }
        for word, info in urlchange.items():
            linkEmp = linkEmp.replace(word, info)
                
        return linkEmp
        
    def dadesEmpresa(self, lastUrl):
        """
        Retorna les dades de l'empresa seleccionada
        """
        # Select drivers in function of OS
        if psutil.MACOS == True:
            driverpath = self.dir_path + "/drivers/macos/geckodriver"
            
        if psutil.WINDOWS == True:
            if str(platform.architecture()[0]) == "64bit":
                driverpath = self.dir_path + "/drivers/win64/geckodriver.exe"
            else:
                driverpath = self.dir_path + "/drivers/win32/geckodriver.exe"
        
        if psutil.LINUX == True:
            if str(platform.architecture()[0]) == "64bit":
                driverpath = self.dir_path + "/drivers/linux64/geckodriver"
            else:
                driverpath = self.dir_path + "/drivers/linux32/geckodriver"
            
        
        # Set vars with fixed values to future improve from data user in command line
        start_day = '2'
        start_month = '4'
        start_year = '2019'
        finish_day = '2'
        finish_month = '8'
        finish_year = '2019'       

        driver = webdriver.Firefox(executable_path = driverpath)

        # Builds url needed        
        url = self.path + lastUrl


        # Opens url
        driver.get(url)

        # Clears and sets starting day
        input_start_day = driver.find_element_by_id('ctl00_Contenido_Desde_Dia')
        input_start_day.clear()
        input_start_day.send_keys(start_day)

        # Clears and sets starting month
        input_start_month = driver.find_element_by_id('ctl00_Contenido_Desde_Mes')
        input_start_month.clear()
        input_start_month.send_keys(start_month)

        # Clears and sets starting year
        input_start_day = driver.find_element_by_id('ctl00_Contenido_Desde_Año')
        input_start_day.clear()
        input_start_day.send_keys(start_year)

        # Clears and sets finishing day
        input_start_day = driver.find_element_by_id('ctl00_Contenido_Hasta_Dia')
        input_start_day.clear()
        input_start_day.send_keys(finish_day)

        # Clears and sets finishing month
        input_start_month = driver.find_element_by_id('ctl00_Contenido_Hasta_Mes')
        input_start_month.clear()
        input_start_month.send_keys(finish_month)

        # Clears and sets finishing year
        input_start_day = driver.find_element_by_id('ctl00_Contenido_Hasta_Año')
        input_start_day.clear()
        input_start_day.send_keys(finish_year)

        # Submits data range
        driver.find_element_by_id('ctl00_Contenido_Buscar').click()
        
        # Ticker and company name
        data_form = driver.find_element_by_class_name('FrmBusq').find_elements_by_tag_name('td')

        self.company = [data_form[8].text]
        ticker = [data_form[10].text]

        # Reads table data
        taula = driver.find_element_by_id('ctl00_Contenido_tblDatos')

        # Heading rows
        self.first_row = [title.text for title in taula.find_elements_by_tag_name('th')]

        # Other rows
        # Reads first page
        self.content = [[element.text for element in row.find_elements_by_tag_name('td')] 
            for row in taula.find_elements_by_tag_name('tr')[1:]]
        
        # Reads other pages
        try:
            while driver.find_element_by_id('ctl00_Contenido_SiguientesArr'):
                driver.find_element_by_id('ctl00_Contenido_SiguientesArr').click()

                taula = driver.find_element_by_id('ctl00_Contenido_tblDatos')

                for row in taula.find_elements_by_tag_name('tr')[1:]:
                    self.content.append([element.text for element in row.find_elements_by_tag_name('td')])
    
        except:
            pass
    
        # Closes window explorer
        driver.quit()
        
        # Save image and opteined url
        imageurl = self.findIimage(url, ticker[0])
        
        # Calls CSV writer method
        self.data2csv(ticker[0], imageurl)
        
        
            
    def data2csv(self, filename, imageurl):
        with open("../data/"+filename+'.csv', "w+", newline='') as csvfile:
            bolsa_writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            bolsa_writer.writerow(self.company)
            bolsa_writer.writerow(["Image url: %s"%(imageurl)])
            bolsa_writer.writerow(["Image folder: %s"%(filename+".gif")])
            bolsa_writer.writerow(self.first_row)
            bolsa_writer.writerows(self.content)
            
            
    def findIimage(self, url, filename):
        # Post request to a url using header and data defined before
        response = requests.post(url)
        # Create soup with the html response from page
        soup = BeautifulSoup(response.content, 'html.parser')
        imgs = soup.find_all('img')
        
        # Find image url
        imgEmp = ''
        for img in imgs:
            if 'logosEmisoras' in img["src"]:
                imgEmp = img.attrs['src']
        
        # Get image from a company
        imgResponse = requests.get(self.path+imgEmp)
        
        # Write image in a folder
        with open("../images/"+filename+'.gif', "wb") as giffile:
            giffile.write(imgResponse.content)
            giffile.close()
            
        return self.path+imgEmp
        
        
        
        

def main():
    
    # Aquest codi és el que anira finalment al main
    bolsa = BolsaScraper()
    
    # Find url with the name of the company
    url = bolsa.trobarEmpresa("sabadell")
    
    # Find and save data from a company defined before
    bolsa.dadesEmpresa(url)
    
    
if __name__ == "__main__":
    main()
    
















