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

Un cop hem definit els paràmetres de la nostra cerca s'ha d'executar el fitxer **main.py**, per fer-ho s'ha d'executar la següent línia des del terminal a la ruta on es trobi el fitxer:

```
python main.py
```
### Estrcutura del nom de cerca:
El programa és capaç de buscar el nom de qualsevol empresa dintre de la borsa de Madrid sense importar si està escrit en majúscules, minúscules o una combinació de les dues, a més encarar que el nom no sigui complet també és capaç de cercar-ho, per exemple el nom del Sabadell a la taula és BANCO DE SABADELL, S.A. però si busques simplement sabadell, el programa és capaç de trobar les dades en un període de temps, a més si busques una empresa que pertany al IBEX35 el programa també és capaç de fer una cerca pel ticker de l'empresa per exemple, si busquem SAB (tant si està en majúscules o en minúscules) que és el ticker de BANCO DE SABADELL, S.A. el programa és capaç de buscar l'empresa i retornar les dades en el període de temps indicat.

Podem trobar els tickers de les empreses a [Ticker IBEX35](https://es.wikipedia.org/wiki/IBEX_35)
