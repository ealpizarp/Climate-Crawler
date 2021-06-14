# Job decade_avg_temp
sqoop export --connect jdbc:mysql://localhost:3306/weatherdata --username root --password root --table decade_avg_temp --export-dir /DECADE_AVG_TEMP --fields-terminated-by "	" --columns "decade,temperature";
# Job max_avg_country_temp
sqoop export --connect jdbc:mysql://localhost:3306/weatherdata --username root --password root --table max_avg_country_temp --export-dir /MAX_AVG_COUNTRY_TEMP --fields-terminated-by "	" --columns "country,temperature";
# Job max_var_country
sqoop export --connect jdbc:mysql://localhost:3306/weatherdata --username root --password root --table max_var_country --export-dir /MAX_VAR_COUNTRY --fields-terminated-by "	" --columns "continent,country";
# Job min_country_var
sqoop export --connect jdbc:mysql://localhost:3306/weatherdata --username root --password root --table min_country_var --export-dir /MIN_COUNTRY_VAR --fields-terminated-by "	" --columns "continent,country";
# Job min_avg_country_temp
sqoop export --connect jdbc:mysql://localhost:3306/weatherdata --username root --password root --table min_avg_country_temp --export-dir /MIN_AVG_COUNTRY_TEMP --fields-terminated-by "	" --columns "country,temperature";
# Job max_year_var
sqoop export --connect jdbc:mysql://localhost:3306/weatherdata --username root --password root --table max_year_var --export-dir /MAX_YEAR_VAR --fields-terminated-by "	" --columns "year,T,TM,Tm,PP,V,RA,SN,TS,FG,TN,GR";
# Job min_year_var
sqoop export --connect jdbc:mysql://localhost:3306/weatherdata --username root --password root --table min_year_var --export-dir /MIN_YEAR_VAR --fields-terminated-by "	" --columns "year,T,TM,Tm,PP,V,RA,SN,TS,FG,TN,GR";
# Job station_max_var
sqoop export --connect jdbc:mysql://localhost:3306/weatherdata --username root --password root --table station_max_var --export-dir /STATION_MAX_VAR --fields-terminated-by "	" --columns "station,T,TM,Tm,PP,V,RA,SN,TS,FG,TN,GR";
# Job station_min_var
sqoop export --connect jdbc:mysql://localhost:3306/weatherdata --username root --password root --table station_min_var --export-dir /STATION_MIN_VAR --fields-terminated-by "	" --columns "station,T,TM,Tm,PP,V,RA,SN,TS,FG,TN,GR";
