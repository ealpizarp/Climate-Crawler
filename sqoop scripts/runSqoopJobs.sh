#Job DECADE_AVG_TEMPERATURE
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table DECADE_AVG_TEMPERATURE --columns "continente, decada, temperatura" --export-dir /DECADE_AVG_TEMPERATURE --fields-terminated-by '\0073';

#Job MAX_AVG_COUNTRY_TEMPS
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table MAX_AVG_COUNTRY_TEMP --columns "country, temperature" --export-dir /MAX_AVG_COUNTRY_TEMPS  --fields-terminated-by '\0073';
#Job MIN_AVG_COUNTRY_TEMPS
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table MIN_AVG_COUNTRY_TEMP --columns "country, temperature" --export-dir /MIN_AVG_COUNTRY_TEMPS  --fields-terminated-by '\0073';

#Job MAX_COUNTRY_VAR
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table MAX_COUNTRY_VAR --columns "continent, T, TMax, Tmin, PP, V, RA, SN, TS, FG, TN, GR" --export-dir /MAX_COUNTRY_VAR  --fields-terminated-by '\0073';
#Job MIN_COUNTRY_VAR
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table MIN_COUNTRY_VAR --columns "continent, T, TMax, Tmin, PP, V, RA, SN, TS, FG, TN, GR" --export-dir /MIN_COUNTRY_VAR  --fields-terminated-by '\0073';

#Job MAX_YEAR_VAR
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table MAX_YEAR_VAR --columns "country, T, TMax, Tmin, PP, V, RA, SN, TS, FG, TN, GR" --export-dir /MAX_YEAR_VAR  --fields-terminated-by '\0073';
#Job MIN_YEAR_VAR
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table MIN_YEAR_VAR --columns "country, T, TMax, Tmin, PP, V, RA, SN, TS, FG, TN, GR" --export-dir /MIN_YEAR_VAR  --fields-terminated-by '\0073';

#Job STATION_MAX_VAR
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table STATION_MAX_VAR --columns "country, T, TMax, Tmin, PP, V, RA, SN, TS, FG, TN, GR" --export-dir /STATION_MAX_VAR  --fields-terminated-by '\0073';
#Job STATION_MIN_VAR
sqoop export --connect jdbc:mysql://34.66.197.163:3306/DB2_PR2 --username admin --password adminpass --table STATION_MIN_VAR --columns "country, T, TMax, Tmin, PP, V, RA, SN, TS, FG, TN, GR" --export-dir /STATION_MIN_VAR  --fields-terminated-by '\0073';