#!/bin/bash


# Costa Rica Institute of Technology

# A script for excecuting all the tasks needed for updating the latest data 
# into the database

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



# Se activa el ambiente virtual para obtener las dependencias

source .venv/bin/activate


# Ejecucion del extraccion de datos mediante el Web Crawler

python3 Web\ Crawler/webScraping.py



# Removes the existing directory in HDFS if the job was executed earlier

hadoop fs -rm -r /MAX_COUNTRY_VAR


#Runs the map reduce job and stores the output in the HDFS

pydoop script --job-name max_variables ./hadoop\ jobs/max_countries_var.py /climate.csv /MAX_COUNTRY_VAR


# Removes the existing directory in HDFS if the job was executed earlier

hadoop fs -rm -r /DECADE_CONTINENT_TEMPERTURE


#Runs the map reduce job and stores the output in the HDFS

pydoop script --job-name decade_avg_temp ./hadoop\ jobs/avg_tmp_cont_v2.py /climate.csv /DECADE_CONTINENT_TEMPERTURE


# Removes the existing directory in HDFS if the job was executed earlier

hadoop fs -rm -r /MAX_AVG_TEMPS


#Runs the map reduce job and stores the output in the HDFS

pydoop script --job-name max_avg_temps ./hadoop\ jobs/max_avg_temps.py /climate.csv /MAX_AVG_TEMPS

# Removes the existing directory in HDFS if the job was executed earlier

hadoop fs -rm -r /MAX_YEAR_VAR

#Runs the map reduce job and stores the output in the HDFS

pydoop script --job-name max_year_var ./hadoop\ jobs/max_year_var.py /climate.csv /MAX_YEAR_VAR