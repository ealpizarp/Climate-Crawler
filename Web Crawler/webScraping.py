# Costa Rica Institute of Technology

# A web scrapper that fetches information about the world climate from https://en.tutiempo.net/climate
# and store it in an local output csv file and in the Hadopp distributed file system

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import requests
from bs4 import BeautifulSoup
import os
from timeit import default_timer as timer
import threading
import pydoop.hdfs as hdfs




lock = threading.Lock()

baseUrl = 'https://en.tutiempo.net'

tableHeader = ["Year", "T", "TM", "Tm", "PP",
               "V", "RA", "SN", "TS", "FG", "TN", "GR"]

archivo = None

archivoErrores = None

linksVisitados = set()







def getLinks(link, pos=-1):


    listaLinks = []
    completeLink = baseUrl + link

    if (pos != -1):
        completeLink = completeLink + "/"+str(pos)+"/"


    page = None
    amountOfTries = 0


    while not page and amountOfTries < 3:
        amountOfTries += 1
        try:
            page = requests.get(completeLink)
        except:
            continue


    if not page:
        print('Error obteniendo tabla ', completeLink)
        return None

    if (pos > 100):
        print("Mas de 100 ", completeLink)


    soup = BeautifulSoup(page.content, 'html.parser')

    # Todas las tablas utilizan esta misma clase

    tablas = soup.find_all("div", {"class": "mlistados"})

    # Aca se buscan todos los links dentro de cada tabla

    for tabla in tablas:

        referencias = tabla.find_all("a")

        for ref in referencias:
            listaLinks += [[ref['href'], ref.string]]
            # print(continente['href'])


    return listaLinks







def writeToFile(basicInfo, rows):
    lock.acquire()

    stringToWrite = ""
    for row in rows:
        stringToWrite += basicInfo + ";" + ';'.join(row) + "\n"
    archivo.write(stringToWrite)

    lock.release()






def getTableInfo(basicInfo, link):
    tableRowsContent = []

    completeLink = baseUrl + link

    page = None
    amountOfTries = 0

    while not page and amountOfTries < 3:
        amountOfTries += 1
        try:
            page = requests.get(completeLink)
        except Exception as e:
            print(e, completeLink)
            continue

    if not page:
        print('Error obteniendo tabla con datos del clima ', completeLink)
        return None

    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find("div", {"class": "mt5 minoverflow"})

    tableRows = table.find_all("tr")[1:]


    for row in tableRows:
        dataCells = row.find_all("td")

        firstColumn = True
        rowText = []


        # Una vez obtenidas todas las lineas se convierte a texto para ser impresas

        for cell in dataCells:


            if (firstColumn == False):
                rowText += [cell.string]
            else:
                year = cell.find("strong")
                rowText += [year.string]
                firstColumn = False

        tableRowsContent += [rowText]

    writeToFile(basicInfo, tableRowsContent)






def getStations(nombreContinente, linkPais):


    nombrePais = linkPais[1]

    currentPage = 1

    while True:
        listaEstaciones = getLinks(linkPais[0], currentPage)

        if not listaEstaciones:
            break

        currentPage += 1

        for linkEstacion in listaEstaciones:
            nombreEstacion = linkEstacion[1]

            try:
                getTableInfo(nombreContinente + ";" +
                             nombrePais + ";" + nombreEstacion, linkEstacion[0])

            except AttributeError as e:
                archivoErrores.write(str(e) + "Continente: " + nombreContinente + " Pais: " + nombrePais +
                                     " Provincia: " + nombreEstacion + " Link: " + baseUrl + linkEstacion[0] + "\n")

        archivo.flush()
        os.fsync(archivo.fileno())

        archivoErrores.flush()
        os.fsync(archivoErrores.fileno())








def handle_none_val(value):
    return value if not None else 'None'






def getCountries(linkContinente):
    nombreContinente = linkContinente[1]
    listaPaises = getLinks(linkContinente[0])

    # Se crea un thread por país y luego se espera a que todos terminen
    threadList = []
    for linkPais in listaPaises:

        threadList += [threading.Thread(target=getStations,
                                        args=(nombreContinente, linkPais, ),
                                        daemon=True)]
    for thread in threadList:
        thread.start()

    for thread in threadList:
        thread.join()







def getContinents():
    listaContinentes = getLinks("/climate/")
    listaContinentes.pop()


    threadList = []
    for linkContinente in listaContinentes:

        threadList += [threading.Thread(target=getCountries,
                                        args=(linkContinente,),
                                        daemon=True)]

    for thread in threadList:
        thread.start()

    for thread in threadList:
        thread.join()






def pruebas():
    global archivo, archivoErrores
    cantidadDePruebas = 10
    for i in range(cantidadDePruebas):
        archivo = open("out" + str(i+1) + ".txt", "w")
        archivo.write("continente" + ";" + "provincia" + ";" + "pais" + ";" + ';'.join(
            ["Year", "T", "TM", "Tm", "PP", "V", "RA", "SN", "TS", "FG", "TN", "GR"]) + "\n")
        archivoErrores = open("errores" + str(i+1) + ".txt", "w")

        start = timer()
        getContinents()
        end = timer()
        print("Duracion", end - start)

        archivo.close()
        archivoErrores.close()
        archivoErrores.close()







def saveFile():
    global archivo,archivoErrores
    archivo = open("climate" + ".csv", "w")
    archivoErrores = open("ERROR_LOG" + ".txt", "w")
    getContinents()
    archivo.close()
    archivoErrores.close()
    archivoErrores.close()





def saveToHadoop():
    if hdfs.path.exists('/climate.csv'):
        hdfs.rm('/climate.csv', True)

    hdfs.put('./climate.csv', '/')


# Se invoca funcion que se encarga de ejecutar todos los procesos recursivamente 

saveFile()

# Se guarda el archivo resultante en el HDFS de Hadoop

saveToHadoop()




"""

    Antártica no tiene países

    Hacer el parser recursivamente
        Cada tabla utiliza la misma clase
        Se busca dicha tabla
        Si no se encuentra se asume que ya se llego al final
            Se busca la tabla del clima

            163208  En ciertos casos no llega a este numero porque el request de la tabla falla
            2587
"""
