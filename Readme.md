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

Cal tenir instal·lat el Firefox pel correcte funcionament del codi, si no es té instal·lat, es pot descarregar [aquí](https://www.mozilla.org/es-ES/firefox/new/)

## Estructura

El programa consta d'una llibreria **bolsaScraper.py** i un script d'execució **main.py** en el qual s'executen les diferents funcions desenvolupades a la llibreria.

Per a més informació consultar la [Wiki](https://github.com/alaverma/web-scraping-uoc/wiki/Pr%C3%A0ctica-1:-Web-Scraping)

## Com executar el codi.

Per definir l'empresa o les empreses de les quals es vulgui obtenir les dades i el període del qual es vol obtenir la informació s'ha d'editar el fitxer **main.py**. A la variable companies s'ha d'escriure el nom de l'empresa amb format string: "name" si es vol cercar més d'una empresa a l'hora s'han d'escriure els diferents noms separats per coma (al **main.py** trobareu un exemple).

També s'ha de definir la data inicial de la cerca amb format "dia/mes/any" la data final és opcional, és a dir, si no s'especifica dintre de la funció *scraper.dadesEmpresa(url, start_date)* com és mostra en aquest exemple, s'agafa per defecte la data del dia de l'execució.

Un cop hem definit els parametres de la nostre busqueda s'ha d'executar el fitxer **main.py**, per fer-ho s'ha d'executar la següent linia des del terminal a la ruta on es trobi el fitxer:

```
python main.py

