# latest/ 

This folder contains files with data that focus on the most recent period of the outbreak. It includes daily 7-day cumulative percent positivity for the molecular test by modified ZIP Code Tabulation Areas (MODZCTA), daily 28-day counts and rates of hospitalizations and deaths by MODZCTA, and trend data that cover the most recent 90 days.

## Files 

### hosp_death_last28days-by-modzcta.csv

This file contains counts and rates of hospitalizations and confirmed deaths, by MODZCTA. Please see the technical notes for a description of MODZCTA ([Geography: Zip codes and ZCTAs](https://github.com/nychealth/coronavirus-data#geography-zip-codes-and-zctas)). 

Indicators, which are calculated for the most recent 28-days at a 14-day lag, include:

| Variable Name | Definition | Timeframe  | 
|-------------------------|------------------------------------------------------------------------------------|----------------------------------------------------| 
| MODZCTA | MODZCTA | |          
| MODZCTA_NAME | Neighborhood name of the MODZCTA | | 
| LABEL | List of the ZIP Code Tabulation Areas (ZCTAs) that are bundled into the MODZCTA | |   
| LAT | Latitude of the central point within the MODZCTA | | 
| LONG | Longitude of the central point within the MODZCTA | |
| HOSPITALIZATION_COUNT_28DAY | Number of hospitalized cases by MODZCTA | Cumulative across current day and 27 previous days |
| HOSPITALIZATION_RATE_28DAY | Rate of hospitalized cases per 100,000 people by MODZCTA | Cumulative across current day and 27 previous days |
| DEATH_COUNT_28DAY | Number of confirmed deaths by MODZCTA | Cumulative across current day and 27 previous days |
| DEATH_RATE_28DAY | Rate of confirmed deaths per 100,000 people by MODZCTA | Cumulative across current day and 27 previous days |
| DATERANGE | Range of dates included in the most recent 28 days | | 

The rate of hospitalized cases per 100,000 people (HOSPITALIZATION_RATE_28DAY) is suppressed for a specific MODZCTA when the HOSPITALIZATION_COUNT_28DAY is between 1 and 5 due to imprecise and unreliable estimates. Both the rate of confirmed deaths per 100,000 people (DEATH_RATE_28DAY) and count (DEATH_COUNT_28DAY) are suppressed for a specific MODZCTA when DEATH_COUNT_28DAY is between 1 and 5 due to imprecise and unreliable estimates and also to protect patient confidentiality. 

Neighborhood names represent the [Neighborhood Organizing Census Committee](https://www1.nyc.gov/site/census/index.page) boundaries, which were recently developed by the U.S. Census Bureau with input from community groups.

Note that sum of counts in this file may not match values in citywide tables because of:
* Records with missing geographic information
* Cells that are suppressed due to imprecise and unreliable estimates or for the protection of patient confidentiality

### last7days-by-modzcta.csv

This file contains person-level information on molecular testing: the number of people who received a test, the number of people with positive results, the percentage of people tested who tested positive, and the median rate of testing per 100,000 people, stratified by MODZCTA. Please see the technical notes for a description of MODZCTA ([Geography: Zip codes and ZCTAs](https://github.com/nychealth/coronavirus-data#geography-zip-codes-and-zctas)), the different [types of COVID-19 laboratory tests](https://github.com/nychealth/coronavirus-data#laboratory-testing), and details on the [calculation of percent positivity](https://github.com/nychealth/coronavirus-data#calculation-of-percent-positivity). The dates shown in this table reflect the date of specimen collection (i.e., when someone went to a healthcare provider for a test). Please note that the number of people with positive results does not include people who previously tested positive.

Indicators, which are calculated for the most recent 7-days, include:

| Variable Name | Definition | Timeframe  | 
|-------------------------|------------------------------------------------------------------------------------|----------------------------------------------------| 
| MODZCTA | MODZCTA | |          
| MODZCTA_NAME | Neighborhood name of the MODZCTA | |  
| LABEL | List of the ZCTAs that are bundled into the MODZCTA | |   
| LAT | Latitude of the central point within the MODZCTA | | 
| LONG | Longitude of the central point within the MODZCTA | |   
| PERCENTPOSITIVITY_7DAY | Percentage of people with a molecular test who tested positive by MODZCTA | Cumulative across current day and 6 previous days |
| PEOPLE_TESTED | Number of people who received a molecular test by MODZCTA | Cumulative across current day and 6 previous days | 
| PEOPLE_POSITIVE | Number of people with a positive result on a molecular test by MODZCTA | Cumulative across current day and 6 previous days | 
| MEDIAN_DAILY_TEST_RATE | Median rate of molecular testing per 100,000 people by MODZCTA | Median across current day and 6 previous days | 
| ADEQUATELY_TESTED | Indicator used by NYC to identify MODZCTA where the MEDIAN_DAILY_TEST_RATE exceeds 260 per 100,000 people | | 
| DATERANGE | Range of dates included in the most recent 7 days | | 

Neighborhood names represent the [Neighborhood Organizing Census Committee](https://www1.nyc.gov/site/census/index.page) boundaries, which were recently developed by the U.S. Census Bureau with input from community groups

Note that sum of counts in this file may not match values in citywide tables because of records with missing geographic information.

Unlike other data in this repository, this file excludes patients in congregate facilities to better track community transmission.

### now-cases-by-day.csv 

This file contains the same data as cases-by-day.csv, but limited to the most recent 90 days. For details, please visit [Trends/Readme/cases-by-day.csv](https://github.com/nychealth/coronavirus-data/tree/master/trends#cases-by-daycsv) 

### now-covid-like-illness.csv 

This file contains the same data as covid-like-illness.csv, but limited to the most recent 90 days. For details, please visit [Trends/Readme/covid-like-illness.csv](https://github.com/nychealth/coronavirus-data/blob/master/trends/Readme.md#covid-like-illnesscsv) 

### now-data-by-day.csv 

This file contains the same data as data-by-day.csv, but limited to the most recent 90 days. For details, please visit [Trends/Readme/data-by-day.csv](https://github.com/nychealth/coronavirus-data/tree/master/trends#data-by-daycsv) 

### now-deaths-by-day.csv 

This file contains the same data as deaths-by-day.csv, but limited to the most recent 90 days. For details, please visit [Trends/Readme/deaths-by-day.csv](https://github.com/nychealth/coronavirus-data/tree/master/trends#deaths-by-day) 

### now-hosp-by-day.csv 

This file contains the same data as hosp-by-day.csv, but limited to the most recent 90 days. For details, please visit [Trends/Readme/hosp-by-day.csv](https://github.com/nychealth/coronavirus-data/tree/master/trends#hosp-by-daycsv) 

### now-summary.csv   

This file contains summary information, including the cut-off date and time for data included in the most recent update, and several citywide indicators.     

Indicators include: 

| Variable Name | Definition | Timeframe | 
|-----------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| MEASURE | Indicator of interest | |         
| LAST_7_DAY | Percent positivity for the molecular test and counts of cases, hospitalizations, and deaths in the last 7 days | Most recent day and previous 6 days |   
| WEEKLY_AVG_LAST_4_WKS | Weekly average of percent positivity for the molecular test and counts of cases, hospitalizations, and deaths in the last 28 days | Average across most recent day and previous 27 days | 
| TOTAL | Cumulative counts of cases, hospitalizations, and deaths | Cumulative |   

Hospitalization counts reflect the total number of people with COVID-19 ever admitted to a hospital, not the number of people currently admitted. Death counts reflect confirmed classifications, and case counts reflect both confirmed and probable classifications, separately. 

### now-testing-by-age.csv 

This file contains the same data as testing-by-age.csv, but limited to the most recent 90 days. For details, please visit [Trends/Readme/testing-by-age.csv](https://github.com/nychealth/coronavirus-data/blob/master/trends/Readme.md#testing-by-agecsv) 

### now-tests.csv 

This file contains the same data as tests.csv, but limited to the most recent 90 days. For details, please visit [Trends/Readme/tests.csv](https://github.com/nychealth/coronavirus-data/blob/master/trends/Readme.md#testscsv) 

### pp-by-modzcta.csv 

This file contains person-level information on molecular testing: the percentage of people tested who tested positive in the 7 days preceding the indicated “end date,” stratified by day and by three different geographies: citywide, borough, MODZCTA. The level of geography is indicated in each column heading.

Please see the technical notes for a description of MODZCTA ([Geography: Zip codes and ZCTAs](https://github.com/nychealth/coronavirus-data#geography-zip-codes-and-zctas)), the different [types of COVID-19 laboratory tests](https://github.com/nychealth/coronavirus-data#laboratory-testing), and details on the [calculation of percent positivity](https://github.com/nychealth/coronavirus-data#calculation-of-percent-positivity). The data shown in this table are displayed by the date of specimen collection (i.e., when someone went to a healthcare provider for a test) for a molecular test.

Unlike other data in this repository, this file excludes patients in congregate facilities, and people who previously tested positive, to better track community transmission.
