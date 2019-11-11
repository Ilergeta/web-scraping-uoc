# Bolsa scraper

## Llibreries

Per executar el nostre codi és necesari tenir instal·lades les llibreries:

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

Per definir l'empresa o les empreses de les quals es vulgui obtenir les dades i el període en el qual es vol obtenir la informació s'han d'afegir els parametres **--companies** i **--start** a l'execució. A la variable companies s'ha d'escriure el nom de l'empresa amb format "string: name" si es vol cercar més d'una empresa a l'hora s'han d'escriure els diferents noms separats per un espai (veure exemples).

També s'ha de definir la data inicial de la cerca amb format "dia/mes/any" la data final és opcional, és a dir, si no es defineix s'agafa per defecte el dia en que s'executa el programa, en cas de voler afegir-la s'ha d'afegir el parametre **--end** a l'execució.

Un cop s'han definit els paràmetres de la cerca s'ha d'executar el fitxer **main.py**, per fer-ho s'ha d'executar la següent línia des del terminal a la ruta on es trobi el fitxer:

```
python main.py --companies company1 [company2 ...] --start startdate [--end enddate]
```

Exemples:

La següent línia de comandes cerca les cotitzacions de l'empresa *BANCO DE SABADELL, S.A.* des del 24 de juny de 2019 fins al dia en que s'executa el programa:
```
python main.py --companies san SABADELL --start 24/06/2019     
```

Per cercar les cotitzacions de les empreses *BANCO DE SABADELL, S.A.* i *BANCO DE SANTANDER, S.A.* entre el 24 de juny i el 9 de novembre de 2019 es pot executar la següent línia de comandes:
```
python main.py --companies san SABADELL --start 24/06/2019 --end 9/10/2019
```

### Estructura del nom de cerca:
El programa és capaç de trobar les dades de qualsevol empresa que cotitzi a la borsa de Madrid sense importar si el seu nom està escrit en majúscules, minúscules o una combinació de les dues, a més encara que el nom no sigui complet també és capaç de cercar-ho, per exemple, l'empresa BANCO DE SABADELL, S.A. es pot cercar simplement com ```sabadell```. Igualment, el programa és capaç de trobar les dades en un període de temps. Finalment, si es cerca una empresa que pertany a l'IBEX35, la cerca també es pot fer pel ticker de l'empresa, així, si es volen les dades de l'empresa BANCO DE SABADELL, S.A. que està inclosa a l'índex IBEX35, es pot realitzar la cerca introduint el seu ticker que és ```SAB``` (tant si està en majúscules o en minúscules) i, d'aquesta manera, el programa és capaç de retornar les dades en el període de temps indicat.

Es poden consultar els tickers de les empreses a [tickers IBEX35](https://es.wikipedia.org/wiki/IBEX_35)
