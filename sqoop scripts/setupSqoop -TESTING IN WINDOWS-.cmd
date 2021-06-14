hdfs.cmd dfs -mkdir /DECADE_AVG_TEMPERATURE
hdfs.cmd dfs -copyFromLocal D:\TEC\HadoopScripts\outputs\DECADE_AVG_TEMPERATURE.txt /DECADE_AVG_TEMPERATURE

hdfs.cmd dfs -mkdir /MAX_AVG_COUNTRY_TEMPS
hdfs.cmd dfs -copyFromLocal D:\TEC\HadoopScripts\outputs\MAX_AVG_COUNTRY_TEMPS.txt /MAX_AVG_COUNTRY_TEMPS

hdfs.cmd dfs -mkdir /MIN_AVG_COUNTRY_TEMPS
hdfs.cmd dfs -copyFromLocal D:\TEC\HadoopScripts\outputs\MIN_AVG_COUNTRY_TEMPS.txt /MIN_AVG_COUNTRY_TEMPS

hdfs.cmd dfs -mkdir /MAX_COUNTRY_VAR
hdfs.cmd dfs -copyFromLocal D:\TEC\HadoopScripts\outputs\MAX_COUNTRY_VAR.txt /MAX_COUNTRY_VAR

hdfs.cmd dfs -mkdir /MIN_COUNTRY_VAR
hdfs.cmd dfs -copyFromLocal D:\TEC\HadoopScripts\outputs\MIN_COUNTRY_VAR.txt /MIN_COUNTRY_VAR

hdfs.cmd dfs -mkdir /MAX_YEAR_VAR
hdfs.cmd dfs -copyFromLocal D:\TEC\HadoopScripts\outputs\MAX_YEAR_VAR.txt /MAX_YEAR_VAR

hdfs.cmd dfs -mkdir /MIN_YEAR_VAR
hdfs.cmd dfs -copyFromLocal D:\TEC\HadoopScripts\outputs\MIN_YEAR_VAR.txt /MIN_YEAR_VAR

hdfs.cmd dfs -mkdir /STATION_MAX_VAR
hdfs.cmd dfs -copyFromLocal D:\TEC\HadoopScripts\outputs\STATION_MAX_VAR.txt /STATION_MAX_VAR

hdfs.cmd dfs -mkdir /STATION_MIN_VAR
hdfs.cmd dfs -copyFromLocal D:\TEC\HadoopScripts\outputs\STATION_MIN_VAR.txt /STATION_MIN_VAR
