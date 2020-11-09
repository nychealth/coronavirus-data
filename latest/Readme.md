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

This file contains data by MODZCTA. Please see description of MODZCTA in the technical notes section (Geography: Zip codes and ZCTAs). Counts are aggregated separately by the following dates of interest:  

- Cases are by date of diagnosis   

- People tested and percent positivity by date of specimen collection (i.e, when someone went to a healthcare provider for a test)

Indicators, which are calculated for the most recent 7-days, include: 

| Variable Name | Definition | Timeframe  | 
|-------------------------|------------------------------------------------------------------------------------|----------------------------------------------------| 
| MODZCTA | MODZCTA | |          
| MODZCTA_NAME | Neighborhood name of the MODZCTA | |    
| PEOPLE_POSITIVE | Count of people who tested positive by MODZCTA | Cumulative across most recent 7 days | 
| PERCENTPOSITIVITY_7DAY | Percentage of people tested with a polymerase chain reaction (PCR) test who tested positive by MODZCTA | Cumulative across most recent 7 days | 
| PEOPLE_TESTED | Number of people who received a PCR test by MODZCTA | Cumulative across most recent 7 days | 
| DATERANGE | Range of dates included in the most recent 7 days | | 

Neighborhood names represent the [Neighborhood Organizing Census Committee](https://www1.nyc.gov/site/census/index.page) boundaries, which were recently developed by the U.S. Census Bureau with input from community groups

Note that sum of counts in this file may not match values in citywide tables because of records with missing geographic information.

### pp-by-modzcta.csv 

This file contains the percentage of people tested for COVID-19 with a PCR test who tested positive in the 7 days preceding the indicated “end date,” stratified by day and by three different geographies: citywide, borough, MODZCTA. The level of geography is indicated in each column heading. Please see description of MODZCTA in the technical notes section (Geography: Zip codes and ZCTAs). 

The data shown in this table are displayed by the date of specimen collection (i.e., when someone went to a healthcare provider for a test) for a PCR test. Please see description of the different categories of COVID-19 tests in the technical notes section (Types of Surveillance: Reportable Disease Surveillance). Note that one person can have more than one test on different days, and a person tested twice in the most recent 7 days would only be counted once. Therefore, the sum of counts across 7-day time periods may not match summary values.

Unlike other data in this repository, this file excludes patients in congregate facilities, and people who previously tested positive, to better track community transmission. 

### now-data-by-day.csv 

This file contains the same data as Trends/data-by-day.csv, but limited to the most recent 90 days. For details, see Trends/Readme.md 
 
### now-covidlike-illness.csv 

This file contains the same data as covidlike-illness.csv, but limited to the most recent 90 days. For details, see Trends/Readme.md 
 
### now-tests.csv 

This file contains the same data as tests.csv, but limited to the most recent 90 days. For details, see Trends/Readme.md 
 
### now-testing-by-age.csv 

This file contains the same data as testing-by-age.csv, but limited to the most recent 90 days. For details, see Trends/Readme.md 
