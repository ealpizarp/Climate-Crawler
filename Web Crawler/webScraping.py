# Costa Rica Institute of Technology

# A web scrapper that fetches information about the world climate from https://en.tutiempo.net/climate
# and store it in an local output csv file and in the Hadopp distributed file system

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


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

# Esta funcion se encarga de recibir todas las filas de una tabla y escribirlas en un archivo
# La actualización de dicho archivo no se realiza en esta funcion


def writeToFile(basicInfo, rows):

    lock.acquire()  # Se bloquean los threads para evitar que haya errores al escribir en el archivo

    stringToWrite = ""
    for row in rows:
        stringToWrite += basicInfo + ";" + ';'.join(row) + "\n"
    archivo.write(stringToWrite)

    lock.release()

# Esta funcion se encarga de buscar las tablas de continentes, países y estaciones, asi como retornar los links que contienen
# Se manejan en una sola funcion porque estas tablas comparten la misma clase de css


def getLinks(link, pos=-1):

    listaLinks = []
    completeLink = baseUrl + link

    # Esta verificación es porque en los continentes no se enviá una posición, entonces el valor por default es -1
    # La posición es para ir avanzando las paginas de las estaciones (pagina 1, pagina 2, ... , pagina n)
    if (pos != -1):
        completeLink = completeLink + "/"+str(pos)+"/"

    page = None
    amountOfTries = 0
    # Para evitar perder información se reintenta un maximo de 2 veces en caso de que falle el request
    while not page and amountOfTries < 2:
        amountOfTries += 1
        try:
            page = requests.get(completeLink)
        except:
            continue

    if not page:
        print('Error obteniendo tabla ', completeLink)
        return None

    soup = BeautifulSoup(page.content, 'html.parser')

    # Todas las tablas utilizan esta misma clase

    tablas = soup.find_all("div", {"class": "mlistados"})

    # Aca se buscan todos los links dentro de cada tabla

    for tabla in tablas:

        referencias = tabla.find_all("a")

        for ref in referencias:
            listaLinks += [[ref['href'], ref.string]]

    return listaLinks

# Esta funcion es para obtener la tabla de clima de una estación


def getTableInfo(basicInfo, link):
    tableRowsContent = []

    completeLink = baseUrl + link

    page = None
    amountOfTries = 0

    while not page and amountOfTries < 2:
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

    # Se obtiene la tabla, y de estas todas las filas
    table = soup.find("div", {"class": "mt5 minoverflow"})

    tableRows = table.find_all("tr")[1:]

    for row in tableRows:
        dataCells = row.find_all("td")  # Se toman las celdas

        firstColumn = True
        rowText = []

        # Una vez obtenidas todas las lineas se convierte a texto para ser impresas
        # La primera celda de cada fila es un caso especial dado que que se deba buscar una etiqueta "strong"
        for cell in dataCells:

            if (firstColumn == False):
                rowText += [cell.string]
            else:
                year = cell.find("strong")
                rowText += [year.string]
                firstColumn = False

        tableRowsContent += [rowText]

    writeToFile(basicInfo, tableRowsContent)


# Funcion para obtener las estaciones de un país, asi como obtener la tabla del clima de cada estación
def getStations(nombreContinente, linkPais):
    nombrePais = linkPais[1]

    currentPage = 1

    # Se itera las paginas de estaciones dado que algunos países cuentas con varias
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

        # Una vez escritas todas las estaciones de una pagina se limpia el buffer y se sincroniza el archivo con el sistema
        archivo.flush()
        os.fsync(archivo.fileno())

        archivoErrores.flush()
        os.fsync(archivoErrores.fileno())


# Esta funcion obtiene los países de un continente
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

    threadList = []
    for linkContinente in listaContinentes[:len(listaContinentes)-1]:
        threadList += [threading.Thread(target=getCountries,
                                        args=(linkContinente,),
                                        daemon=True)]

    threadList += [threading.Thread(target=getStations,
                                    args=("Antartica", listaContinentes[len(
                                        listaContinentes)-1], ),
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
    global archivo, archivoErrores
    archivo = open("climate" + ".csv", "w")
    archivoErrores = open("ERROR_LOG" + ".txt", "w")
    start = timer()

    getContinents()

    end = timer()
    print("Duracion", end - start)
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