# latest/ 

This folder contains files with data that focus on the most recent period of the outbreak. It includes daily 7-day cumulative percent positivity by modified ZIP code tabulation areas (MODZCTA), and trend data that cover the most recent 90 days.

## Files 

### now-summary.csv   

This file contains summary information, including the cut-off date and time for data included in the update, and several citywide indicators.     

Indicators include: 

| Variable Name | Definition | Timeframe | 
|-----------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| MEASURE | Indicator of interest | |         
| LAST_7_DAY | Percent positivity and counts of confirmed cases, hospitalizations, and deaths in the last 7 days | Most recent day and previous 6 days |   
| WEEKLY_AVG_LAST_4_WKS | Weekly average of percent positivity and counts of confirmed cases, hospitalizations, and deaths in the last 28 days | Average across most recent day and previous 27 days | 
| TOTAL | Cumulative counts of confirmed cases, hospitalizations, and deaths | Cumulative |   

Hospitalization counts reflect the total number of people with COVID-19 ever admitted to a hospital, not the number of people currently admitted. Death counts reflect both confirmed and probable deaths, separately. 

### last7days-by-modzcta.csv

This file contains the number of people who received a polymerase chain reaction (PCR) test, the number of people with positive results, the percentage of people tested who tested positive, and the median rate of PCR testing per 100,000 people, stratified by MODZCTA. Please see the technical notes section for a description of MODZCTA (Geography: Zip codes and ZCTAs), and the different categories of COVID-19 tests (Types of Surveillance: Reportable Disease Surveillance). The dates shown in this table reflect the date of specimen collection (i.e., when someone went to a healthcare provider for a test). Please note that the number of people with positive results does not include people who previously tested positive.

Indicators, which are calculated for the most recent 7-days, include:

| Variable Name | Definition | Timeframe  | 
|-------------------------|------------------------------------------------------------------------------------|----------------------------------------------------| 
| MODZCTA | MODZCTA | |          
| MODZCTA_NAME | Neighborhood name of the MODZCTA | |    
| PERCENTPOSITIVITY_7DAY | Percentage of people with a PCR test who tested positive by MODZCTA | Cumulative across current day and 6 previous days |
| PEOPLE_TESTED | Number of people who received a PCR test by MODZCTA | Cumulative across current day and 6 previous days | 
| PEOPLE_POSITIVE | Number of people with a positive result on a PCR test by MODZCTA | Cumulative across current day and 6 previous days | 
| MEDIAN_DAILY_TEST_RATE | Median rate of PCR testing per 100,000 people by MODZCTA | Median across current day and 6 previous days | 
| ADEQUATELY_TESTED | Indicator used by NYC to identify MODZCTA where MEDIAN_DAILY_TEST_RATE exceeds 260 per 100,000 people | | 
| DATERANGE | Range of dates included in the most recent 7 days | | 

Neighborhood names represent the [Neighborhood Organizing Census Committee](https://www1.nyc.gov/site/census/index.page) boundaries, which were recently developed by the U.S. Census Bureau with input from community groups

Note that sum of counts in this file may not match values in citywide tables because of records with missing geographic information.

### pp-by-modzcta.csv 

This file contains the percentage of people with a PCR test who tested positive in the 7 days preceding the indicated “end date,” stratified by day and by three different geographies: citywide, borough, MODZCTA. The level of geography is indicated in each column heading.

The data shown in this table are displayed by the date of specimen collection (i.e., when someone went to a healthcare provider for a test) for a PCR test. Please see description of the different categories of COVID-19 tests in the technical notes section (Types of Surveillance: Reportable Disease Surveillance). Note that one person can have more than one test on different days, and a person tested twice in the most recent 7 days would only be counted once. Therefore, the sum of counts across 7-day time periods may not match summary values.

Unlike other data in this repository, this file excludes patients in congregate facilities, and people who previously tested positive, to better track community transmission. 

### now-data-by-day.csv 

This file contains the same data as Trends/data-by-day.csv, but limited to the most recent 90 days. For details, please visit [Trends/Readme/data-by-day.csv](https://github.com/nychealth/coronavirus-data/tree/master/trends#data-by-daycsv) 
 
### now-covid-like-illness.csv 

This file contains the same data as covid-like-illness.csv, but limited to the most recent 90 days. For details, please visit [Trends/Readme/covid-like-illness.csv](https://github.com/nychealth/coronavirus-data/blob/master/trends/Readme.md#covid-like-illnesscsv) 
 
### now-tests.csv 

This file contains the same data as tests.csv, but limited to the most recent 90 days. For details, please visit [Trends/Readme/tests.csv](https://github.com/nychealth/coronavirus-data/blob/master/trends/Readme.md#testscsv) 
 
### now-testing-by-age.csv 

This file contains the same data as testing-by-age.csv, but limited to the most recent 90 days. For details, please visit [Trends/Readme/testing-by-age.csv](https://github.com/nychealth/coronavirus-data/blob/master/trends/Readme.md#testing-by-agecsv) 
