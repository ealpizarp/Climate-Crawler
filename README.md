# Climate crawler

Climate crawler is project made for the databases II (IC4302) course in the Costa Rica Institute of Technology

## Web Crawler

The data fetched by the web crawler is retrieved from https://en.tutiempo.net/climate/

## Hadoop

Hadoop is used for processing and storing data of the web crawler output in the HDFS, map reduce jobs 
are made in a high level python api for hadoop called pydoop. The map reduce jobs are:

1. The 10 countries with the highest overall averages
2. The 10 countries with the lowest overall averages
3. For each country the year in which each of the variables was the maximum
4. For each country the year in which each of the variables was the minimum
5. Average temperature for each continent, in groups of 10 years
6. By Country the station that has the maximum values
7. By Country the station that has the minimum values
8. By Continent the countries with the maximum values
9. By Continent the countries with the minimum values


## Database

The database of choice is MySQL

## Web interface

The web interface is made in NodeJS and react