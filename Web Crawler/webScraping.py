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

baseUrl = 'https://en.tutiempo.net/climate'


tableHeader = ["Year", "T", "TM", "Tm", "PP",
               "V", "RA", "SN", "TS", "FG", "TN", "GR"]

archivo = None

archivoErrores = None


def getLinks(link):
    listaLinks = []

    page = requests.get(baseUrl + link)

    if not page:

        print('Error obteniendo tabla')

    soup = BeautifulSoup(page.content, 'html.parser')

    # Todas las tablas utilizan esta misma clase

    tablas = soup.find_all("div", {"class": "mlistados"})

    # Aca se buscan todos los links dentro de cada tabla

    for tabla in tablas:

        referencias = tabla.find_all("a")

        for ref in referencias:
            listaLinks += [ref['href']]
            # print(continente['href'])

    return listaLinks






def writeToFile(basicInfo, rows):


    lock.acquire()
    #print("Escribiendo filas desde thread: ", threading.get_ident())

    stringToWrite = ""
    for row in rows:
        stringToWrite += basicInfo + ";" + ';'.join(row) + "\n"
    archivo.write(stringToWrite)

    lock.release()






def getTableInfo(basicInfo, link):
    tableRowsContent = []

    page = requests.get(baseUrl + link)

    if not page:
        print('Error obteniendo tabla del clima')

    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find("div", {"class": "mt5 minoverflow"})

    tableRows = table.find_all("tr")[1:]

    for row in tableRows:
        dataCells = row.find_all("td")
        #print(row, "\n")

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
        # print(tableRowsContent)

    # return tableRowsContent
    writeToFile(basicInfo, tableRowsContent)





def handle_none_val(value):
    return value if not None else 'None'






def getProvinces(nombreContinente, linkPais):
    nombrePais = linkPais.replace("/climate/", "").replace(".html", "")
    listaProvincias = getLinks(linkPais)
    for linkProvincia in listaProvincias:
        nombreProvincia = linkProvincia.replace(
            "/climate/", "").replace(".html", "")
        # print("Continente: " + nombreContinente + " Pais: " + nombrePais +
        #       " Provincia: " + nombreProvincia + " Link: " + baseUrl + linkProvincia + "\n")

        try:
            getTableInfo(nombreContinente + ";" +
                         nombrePais + ";" + nombreProvincia, linkProvincia)
            
        except AttributeError as e:
            archivoErrores.write( 'ERROR FETCHING TABLE '+ "Continente: " + handle_none_val(nombreContinente)  + " Pais: " + handle_none_val(nombrePais) +
                                 " Provincia: " + handle_none_val(nombreProvincia) + " Link: " + handle_none_val(baseUrl) + handle_none_val(linkProvincia) + "\n")
            # print(e, "Continente: " + nombreContinente + " Pais: " + nombrePais +
            #      " Provincia: " + nombreProvincia + " Link: " + baseUrl + linkProvincia + "\n")

            # print(
            #     "!!!!!!!!! Error no se encontró tabla dentro de provincia !!!!!!!!!")

        # print("\n #################### Fin de la tabla #################### \n")


    archivo.flush()
    os.fsync(archivo.fileno())

    archivoErrores.flush()
    os.fsync(archivoErrores.fileno())







def getCountries(linkContinente):
    nombreContinente = linkContinente.replace(
        "/climate/", "").replace(".html", "")
    listaPaises = getLinks(linkContinente)

    # Se crea un thread por país y luego se espera a que todos terminen
    threadList = []
    for linkPais in listaPaises:
        #getProvinces(nombreContinente, linkPais)
        threadList += [threading.Thread(target=getProvinces,
                                        args=(nombreContinente, linkPais, ))]
    for thread in threadList:
        thread.start()

    for thread in threadList:
        thread.join()








def getContinents():
    listaContinentes = getLinks('')
    # print(listaContinentes)
    # print("\n")

    threadList = []
    for linkContinente in listaContinentes:
        # getCountries(linkContinente)
        threadList += [threading.Thread(target=getCountries,
                                        args=(linkContinente,))]

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
    '''
    archivo.write("continente" + ";" + "provincia" + ";" + "pais" + ";" + ';'.join(
    ["Year", "T", "TM", "Tm", "PP", "V", "RA", "SN", "TS", "FG", "TN", "GR"]) + "\n")
    '''
    getContinents()
    archivo.close()
    archivoErrores.close()




def saveToHadoop():
    hdfs.rm('/climate.csv', True)
    hdfs.put('./climate.csv', '/')


saveFile()



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
