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



# The virtual enviroment is activated for accesing dependencies

source .venv/bin/activate


# If there are previous output files they are removed 

rm -r climate.csv
rm -r ERROR_LOG.txt

# The data is extracted using the web crawler

python3 Web\ Crawler/webScraping.py



# Removes the existing directory in HDFS if the job was executed earlier

hadoop fs -rm -r /MAX_COUNTRY_VAR

hadoop fs -rm -r /MIN_COUNTRY_VAR

#Runs the map reduce job and stores the output in the HDFS

pydoop script --job-name max_country_var ./hadoop\ jobs/max_country_var.py /climate.csv /MAX_COUNTRY_VAR - t ';'

pydoop script --job-name min_country_var ./hadoop\ jobs/min_country_var.py /climate.csv /MIN_COUNTRY_VAR -t ';'


# Removes the existing directory in HDFS if the job was executed earlier

hadoop fs -rm -r /DECADE_CONTINENT_TEMPERTURE

#Runs the map reduce job and stores the output in the HDFS

pydoop script --job-name decade_avg_temp ./hadoop\ jobs/decade_avg_temp.py /climate.csv /DECADE_CONTINENT_TEMPERTURE - t ';'


# Removes the existing directory in HDFS if the job was executed earlier

hadoop fs -rm -r /MAX_AVG_COUNTRY_TEMPS

hadoop fs -rm -r /MIN_AVG_COUNTRY_TEMPS

#Runs the map reduce job and stores the output in the HDFS

pydoop script --job-name max_avg_country_temps ./hadoop\ jobs/max_avg_country_temp.py /climate.csv /MAX_AVG_COUNTRY_TEMPS -t ';'

pydoop script --job-name min_avg_country_temps ./hadoop\ jobs/min_avg_country_temp.py /climate.csv /MIN_AVG_COUNTRY_TEMPS -t ';'

# Removes the existing directory in HDFS if the job was executed earlier

hadoop fs -rm -r /MAX_YEAR_VAR

hadoop fs -rm -r /MIN_YEAR_VAR

#Runs the map reduce job and stores the output in the HDFS

pydoop script --job-name max_year_var ./hadoop\ jobs/max_year_var.py /climate.csv /MAX_YEAR_VAR -t ';'

pydoop script --job-name min_year_var ./hadoop\ jobs/min_year_var.py /climate.csv /MIN_YEAR_VAR -t ';'


hadoop fs -rm -r /STATION_MAX_VAR

hadoop fs -rm -r /STATION_MIN_VAR

#Runs the map reduce job and stores the output in the HDFS

pydoop script --job-name station_min_var ./hadoop\ jobs/station_min_var.py /climate.csv /STATION_MIN_VAR -t ';'

pydoop script --job-name station_max_var ./hadoop\ jobs/station_max_var.py /climate.csv /STATION_MAX_VAR -t ';'

#Runs all the exports 
#Job DECADE_AVG_TEMPERATURE
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table DECADE_AVG_TEMPERATURE --columns "continente, decada, temperatura" --export-dir /DECADE_AVG_TEMPERATURE --fields-terminated-by '\0073'

#Job MAX_AVG_COUNTRY_TEMPS
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table MAX_AVG_COUNTRY_TEMP --columns "country, temperature" --export-dir /MAX_AVG_COUNTRY_TEMPS  --fields-terminated-by '\0073'
#Job MIN_AVG_COUNTRY_TEMPS
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table MIN_AVG_COUNTRY_TEMP --columns "country, temperature" --export-dir /MIN_AVG_COUNTRY_TEMPS  --fields-terminated-by '\0073'

#Job MAX_COUNTRY_VAR
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table MAX_COUNTRY_VAR --columns "continent, T, TMax, Tmin, PP, V, RA, SN, TS, FG, TN, GR" --export-dir /MAX_COUNTRY_VAR  --fields-terminated-by '\0073'
#Job MIN_COUNTRY_VAR
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table MIN_COUNTRY_VAR --columns "continent, T, TMax, Tmin, PP, V, RA, SN, TS, FG, TN, GR" --export-dir /MIN_COUNTRY_VAR  --fields-terminated-by '\0073'

#Job MAX_YEAR_VAR
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table MAX_YEAR_VAR --columns "country, T, TMax, Tmin, PP, V, RA, SN, TS, FG, TN, GR" --export-dir /MAX_YEAR_VAR  --fields-terminated-by '\0073'
#Job MIN_YEAR_VAR
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table MIN_YEAR_VAR --columns "country, T, TMax, Tmin, PP, V, RA, SN, TS, FG, TN, GR" --export-dir /MIN_YEAR_VAR  --fields-terminated-by '\0073'

#Job STATION_MAX_VAR
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table STATION_MAX_VAR --columns "country, T, TMax, Tmin, PP, V, RA, SN, TS, FG, TN, GR" --export-dir /STATION_MAX_VAR  --fields-terminated-by '\0073'
#Job STATION_MIN_VAR
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table STATION_MIN_VAR --columns "country, T, TMax, Tmin, PP, V, RA, SN, TS, FG, TN, GR" --export-dir /STATION_MIN_VAR  --fields-terminated-by '\0073'