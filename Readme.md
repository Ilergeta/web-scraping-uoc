# Bolsa scraper

## Llibreries

Per executar el nostre codi és necesari tenir instalades les llibreries:

```
pip install pandas
pip install requests
pip install selenium
pip install beautifulsoup4
pip install psutil
```
*Nota:* Pel correcte funcionament del programa, possiblement sigui necessari tenir instal.lat `geckordriver` que es pot descarregar [aquí](https://github.com/mozilla/geckodriver/releases) i afegir la ruta de l'executable al path del sistema o en la línia d'execució del navegador (fitxer src/bolsaScraper.py).

En cas d'executar aquest programa des de MAC OS amb l'última actualització (*Catalina*) s'ha d'executar la següent comanda:
```
% xattr -r -d com.apple.quarantine geckodriver
```
a la carpeta */drivers/macos/*

## Estructura

El programa consta d'una llibreria **bolsaScraper.py** i un script d'execució **main.py** en el qual s'executen les diferents funcions desenvolupades a la llibreria.

Per a més informació consultar la [Wiki](https://github.com/alaverma/web-scraping-uoc/wiki/Pr%C3%A0ctica-1:-Web-Scraping)
