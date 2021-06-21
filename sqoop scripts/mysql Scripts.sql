--Creacion de la base
CREATE DATABASE `DB2_PR2`


--Creacion de tablas
CREATE TABLE `DECADE_AVG_TEMPERATURE` (
    `ID` INT NOT NULL AUTO_INCREMENT,
    `continente` VARCHAR(50) NULL DEFAULT NULL,
    `decada` YEAR NULL DEFAULT NULL,
    `temperatura` FLOAT NULL DEFAULT NULL,
    PRIMARY KEY (`ID`)
)
COLLATE='utf8mb4_0900_ai_ci'
;

CREATE TABLE `MAX_AVG_COUNTRY_TEMPS` (
    `ID` INT NOT NULL AUTO_INCREMENT,
    `country` VARCHAR(50) NOT NULL DEFAULT '0',
    `temperature` FLOAT NOT NULL DEFAULT 0,
    PRIMARY KEY (`ID`)
)
COLLATE='utf8mb4_0900_ai_ci'
;

CREATE TABLE `MIN_AVG_COUNTRY_TEMPS` (
    `ID` INT NOT NULL AUTO_INCREMENT,
    `country` VARCHAR(50) NOT NULL DEFAULT '0',
    `temperature` FLOAT NOT NULL DEFAULT 0,
    PRIMARY KEY (`ID`)
)
COLLATE='utf8mb4_0900_ai_ci'
;

CREATE TABLE `MAX_COUNTRY_VAR` (
    `ID` INT NOT NULL AUTO_INCREMENT,
    `continent` VARCHAR(50) NOT NULL DEFAULT '0',
    `T` VARCHAR(50) NOT NULL DEFAULT '0',
    `TMax` VARCHAR(50) NOT NULL DEFAULT '0',
    `Tmin` VARCHAR(50) NOT NULL DEFAULT '0',
    `PP` VARCHAR(50) NOT NULL DEFAULT '0',
    `V` VARCHAR(50) NOT NULL DEFAULT '0',
    `RA` VARCHAR(50) NOT NULL DEFAULT '0',
    `SN` VARCHAR(50) NOT NULL DEFAULT '0',
    `TS` VARCHAR(50) NOT NULL DEFAULT '0',
    `FG` VARCHAR(50) NOT NULL DEFAULT '0',
    `TN` VARCHAR(50) NOT NULL DEFAULT '0',
    `GR` VARCHAR(50) NOT NULL DEFAULT '0',
    PRIMARY KEY (`ID`)
)
COLLATE='utf8mb4_0900_ai_ci'
;

CREATE TABLE `MIN_COUNTRY_VAR` (
    `ID` INT NOT NULL AUTO_INCREMENT,
    `continent` VARCHAR(50) NOT NULL DEFAULT '0',
    `T` VARCHAR(50) NOT NULL DEFAULT '0',
    `TMax` VARCHAR(50) NOT NULL DEFAULT '0',
    `Tmin` VARCHAR(50) NOT NULL DEFAULT '0',
    `PP` VARCHAR(50) NOT NULL DEFAULT '0',
    `V` VARCHAR(50) NOT NULL DEFAULT '0',
    `RA` VARCHAR(50) NOT NULL DEFAULT '0',
    `SN` VARCHAR(50) NOT NULL DEFAULT '0',
    `TS` VARCHAR(50) NOT NULL DEFAULT '0',
    `FG` VARCHAR(50) NOT NULL DEFAULT '0',
    `TN` VARCHAR(50) NOT NULL DEFAULT '0',
    `GR` VARCHAR(50) NOT NULL DEFAULT '0',
    PRIMARY KEY (`ID`)
)
COLLATE='utf8mb4_0900_ai_ci'
;

CREATE TABLE `MAX_YEAR_VAR` (
    `ID` INT NOT NULL AUTO_INCREMENT,
    `country` VARCHAR(50) NOT NULL DEFAULT '0',
    `T` YEAR NULL DEFAULT NULL,
    `TMax` YEAR NULL DEFAULT NULL,
    `Tmin` YEAR NULL DEFAULT NULL,
    `PP` YEAR NULL DEFAULT NULL,
    `V` YEAR NULL DEFAULT NULL,
    `RA` YEAR NULL DEFAULT NULL,
    `SN` YEAR NULL DEFAULT NULL,
    `TS` YEAR NULL DEFAULT NULL,
    `FG` YEAR NULL DEFAULT NULL,
    `TN` YEAR NULL DEFAULT NULL,
    `GR` YEAR NULL DEFAULT NULL,
    PRIMARY KEY (`ID`)
)
COLLATE='utf8mb4_0900_ai_ci'
;

CREATE TABLE `MIN_YEAR_VAR` (
    `ID` INT NOT NULL AUTO_INCREMENT,
    `country` VARCHAR(50) NOT NULL DEFAULT '0',
    `T` YEAR NULL DEFAULT NULL,
    `TMax` YEAR NULL DEFAULT NULL,
    `Tmin` YEAR NULL DEFAULT NULL,
    `PP` YEAR NULL DEFAULT NULL,
    `V` YEAR NULL DEFAULT NULL,
    `RA` YEAR NULL DEFAULT NULL,
    `SN` YEAR NULL DEFAULT NULL,
    `TS` YEAR NULL DEFAULT NULL,
    `FG` YEAR NULL DEFAULT NULL,
    `TN` YEAR NULL DEFAULT NULL,
    `GR` YEAR NULL DEFAULT NULL,
    PRIMARY KEY (`ID`)
)
COLLATE='utf8mb4_0900_ai_ci'
;

CREATE TABLE `STATION_MAX_VAR` (
    `ID` INT NOT NULL AUTO_INCREMENT,
    `country` VARCHAR(50) NOT NULL DEFAULT '0',
    `T` VARCHAR(50) NOT NULL DEFAULT '0',
    `TMax` VARCHAR(50) NOT NULL DEFAULT '0',
    `Tmin` VARCHAR(50) NOT NULL DEFAULT '0',
    `PP` VARCHAR(50) NOT NULL DEFAULT '0',
    `V` VARCHAR(50) NOT NULL DEFAULT '0',
    `RA` VARCHAR(50) NOT NULL DEFAULT '0',
    `SN` VARCHAR(50) NOT NULL DEFAULT '0',
    `TS` VARCHAR(50) NOT NULL DEFAULT '0',
    `FG` VARCHAR(50) NOT NULL DEFAULT '0',
    `TN` VARCHAR(50) NOT NULL DEFAULT '0',
    `GR` VARCHAR(50) NOT NULL DEFAULT '0',
    PRIMARY KEY (`ID`)
)
COLLATE='utf8mb4_0900_ai_ci'
;

CREATE TABLE `STATION_MIN_VAR` (
    `ID` INT NOT NULL AUTO_INCREMENT,
    `country` VARCHAR(50) NOT NULL DEFAULT '0',
    `T` VARCHAR(50) NOT NULL DEFAULT '0',
    `TMax` VARCHAR(50) NOT NULL DEFAULT '0',
    `Tmin` VARCHAR(50) NOT NULL DEFAULT '0',
    `PP` VARCHAR(50) NOT NULL DEFAULT '0',
    `V` VARCHAR(50) NOT NULL DEFAULT '0',
    `RA` VARCHAR(50) NOT NULL DEFAULT '0',
    `SN` VARCHAR(50) NOT NULL DEFAULT '0',
    `TS` VARCHAR(50) NOT NULL DEFAULT '0',
    `FG` VARCHAR(50) NOT NULL DEFAULT '0',
    `TN` VARCHAR(50) NOT NULL DEFAULT '0',
    `GR` VARCHAR(50) NOT NULL DEFAULT '0',
    PRIMARY KEY (`ID`)
)
COLLATE='utf8mb4_0900_ai_ci'
;

--test:

SELECT a.country, a.temperature, b.temperature FROM MAX_AVG_COUNTRY_TEMP AS a, MIN_AVG_COUNTRY_TEMP AS b WHERE a.country = b.country;