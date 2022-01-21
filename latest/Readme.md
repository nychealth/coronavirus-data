# latest/ 

This folder contains files with data that focus on the most recent period of the outbreak. It includes daily 7-day cumulative percent positivity for the molecular test by modified ZIP Code Tabulation Areas (MODZCTA), daily 28-day counts and rates of hospitalizations and deaths by MODZCTA, and trend data that cover the most recent 90 days.

## Files 
### breakthrough-summary.csv
This file contains cumulative counts and average weekly rates of cases, hospitalizations, and deaths by vaccination status,  since January 17, 2021. Data are updated on Thursdays containing data through the Saturday 12 days prior. As of 1/6/2022, data include children age 5-11 years.

It includes the following definitions:
- "Vaccinated" means people age 5 and over who are fully vaccinated at the time of case diagnosis: 14 days after the administration of the 2nd dose in a 2-dose series, or after the administration of a single-dose vaccine. 
- "Unvaccinated" means people age 5 and over with no record of vaccination status.
- Cases, hospitalization, and deaths: defined per this repository's common standards.
- Rates are per 100,000 people. Hospitalization and death rates are age-adjusted. The denominator for average weekly rates for vaccinated people is the count of NYC residents recorded as fully vaccinated by the week of an event (case, hospitalization, or death) included in the rate; the denominator for unvaccinated people is the total city population minus the number of fully or partially vaccinated people  as of the week of event. 

### now-weekly-breakthrough.csv
This file contains weekly counts and rates of cases and hospitalizations by vaccination status, and citywide. Data are updated on Thursdays containing data through the Saturday 12 days prior. As of 1/6/2022, data from the week of 12/18/2021 onward include children age 5-11 years. 

Definitions of vaccinated and unvaccinated people are the same as for breakthrough-summary.csv.


| Variable name          | Definition                                                                | Timeframe                                |
|------------------------|---------------------------------------------------------------------------|------------------------------------------|
| Week_of_diagnosis      | Week-ending date                                                          |                                          |
| vax_case_count         | Count of cases diagnosed among fully vaccinated people                    | Full week preceding the week-ending date |
| vax_case_rate          | Rate of cases diagnosed per 100,000 fully vaccinated people               | Full week preceding the week-ending date |
| vax_hosp_count         | Count of hospitalizations among fully vaccinated people                   | Full week preceding the week-ending date |
| vax_hosp_rate_adj      | Age-adjusted rate of hospitalizations per 100,000 fully vaccinated people | Full week preceding the week-ending date |
| vax_death_count        | Count of deaths among fully vaccinated people                             | Full week preceding the week-ending date |
| vax_death_rate_adj     | Age-adjusted rate of deaths per 100,000 fully vaccinated people           | Full week preceding the week-ending date |
| unvax_case_count       | Count of cases diagnosed among unvaccinated people                        | Full week preceding the week-ending date |
| unvax_case_rate        | Rate of cases diagnosed per 100,000 unvaccinated people                   | Full week preceding the week-ending date |
| unvax_hosp_count       | Count of hospitalizations among unvaccinated people                       | Full week preceding the week-ending date |
| unvax_hosp_rate_adj    | Age-adjusted rate of hospitalizations per 100,000 unvaccinated people     | Full week preceding the week-ending date |
| unvax_death_count      | Count of deaths among unvaccinated people                                 | Full week preceding the week-ending date |
| unvax_death_rate_adj   | Age-adjusted rate of deaths per 100,000 unvaccinated people               | Full week preceding the week-ending date |
| citywide_case_rate     | Rate of cases diagnosed per 100,000 people citywide                       | Full week preceding the week-ending date |
| citywide_hosp_rate_adj | Age-adjusted rate of hospitalizations per 100,000 people citywide         | Full week preceding the week-ending date |
| citywide_death_rate_adj| Age-adjusted rate of deaths per 100,000 unvaccinated people citywide      | Full week preceding the week-ending date |

### hosp_death_last28days-by-modzcta.csv

This file contains counts and rates of hospitalizations and deaths, by MODZCTA. Please see the technical notes for a [description of MODZCTA](https://github.com/nychealth/coronavirus-data#geography). 

Indicators include:

| Variable Name | Definition | Timeframe  | 
|-------------------------|------------------------------------------------------------------------------------|----------------------------------------------------| 
| MODZCTA | MODZCTA | |          
| MODZCTA_NAME | Neighborhood name of the MODZCTA | | 
| LABEL | List of the ZIP Code Tabulation Areas (ZCTAs) that are bundled into the MODZCTA | |   
| LAT | Latitude of the central point within the MODZCTA | | 
| LONG | Longitude of the central point within the MODZCTA | |
| HOSPITALIZATION_COUNT_28DAY | Number of hospitalized cases by MODZCTA | Cumulative across current day and 27 previous days |
| HOSPITALIZATION_RATE_28DAY | Rate of hospitalized cases per 100,000 people by MODZCTA | Cumulative across current day and 27 previous days |
| DEATH_COUNT_28DAY | Number of deaths by MODZCTA | Cumulative across current day and 27 previous days |
| DEATH_RATE_28DAY | Rate of deaths per 100,000 people by MODZCTA | Cumulative across current day and 27 previous days |
| DATERANGE | Range of dates included in the most recent 28 days | | 

The rate of hospitalized cases per 100,000 people (HOSPITALIZATION_RATE_28DAY) is suppressed for a specific MODZCTA when the HOSPITALIZATION_COUNT_28DAY is between 1 and 5 due to imprecise and unreliable estimates. Both the rate of deaths per 100,000 people (DEATH_RATE_28DAY) and count (DEATH_COUNT_28DAY) are suppressed for a specific MODZCTA when DEATH_COUNT_28DAY is between 1 and 5 due to imprecise and unreliable estimates and also to protect patient confidentiality. 

Neighborhood names represent the [Neighborhood Organizing Census Committee](https://www1.nyc.gov/site/census/index.page) boundaries, which were recently developed by the U.S. Census Bureau with input from community groups.

Note that sum of counts in this file may not match values in citywide tables because of:
* Records with missing geographic information
* Cells that are suppressed due to imprecise and unreliable estimates or for the protection of patient confidentiality

### last7days-by-modzcta.csv

This file contains person-level information on molecular testing: the number of people who received a test, the number of people with positive results, the percentage of people tested who tested positive, and the median rate of testing per 100,000 people, stratified by MODZCTA. Please see the technical notes for a [description of MODZCTA](https://github.com/nychealth/coronavirus-data#geography), the different [types of COVID-19 laboratory tests](https://github.com/nychealth/coronavirus-data#laboratory-testing), and details on the [calculation of percent positivity](https://github.com/nychealth/coronavirus-data#calculation-of-percent-positivity). The dates shown in this table reflect the date of specimen collection (i.e., when someone went to a healthcare provider for a test). Please note that the number of people with positive results does not include people who previously tested positive.

Indicators include:

| Variable Name | Definition | Timeframe  | 
|-------------------------|------------------------------------------------------------------------------------|---------------------------------------------| 
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
| DAILY_AVG_7DAY | *For percent positivity:* Percentage of people with a molecular test who tested positive in the last 7 days; *For others:* daily average of the counts of cases, hospitalizations, and deaths in the last 7 days | Most recent day and previous 6 days |  
| DAILY_AVG_28DAY | *For percent positivity:* Percentage of people with a molecular test who tested positive in the last 28 days; *For others:* daily average of the counts of cases, hospitalizations, and deaths in the last 28 days | Average across most recent day and previous 27 days | 
| LAST_7_DAY | Percent positivity for the molecular test and counts of cases, hospitalizations, and deaths in the last 7 days | Most recent day and previous 6 days |   
| WEEKLY_AVG_LAST_4_WKS | Weekly average of percent positivity for the molecular test and counts of cases, hospitalizations, and deaths in the last 28 days | Average across most recent day and previous 27 days | 
| TOTAL | Cumulative counts of cases, hospitalizations, and deaths | Cumulative |   

Hospitalization counts reflect the total number of people with COVID-19 ever admitted to a hospital, not the number of people currently admitted. Death counts reflect confirmed classifications, and case counts reflect both confirmed and probable classifications, separately. 

### now-testing-by-age.csv 

This file contains the same data as testing-by-age.csv, but limited to the most recent 90 days. For details, please visit [Trends/Readme/testing-by-age.csv](https://github.com/nychealth/coronavirus-data/blob/master/trends/Readme.md#testing-by-agecsv) 

### now-tests.csv 

This file contains the same data as tests.csv, but limited to the most recent 90 days. For details, please visit [Trends/Readme/tests.csv](https://github.com/nychealth/coronavirus-data/blob/master/trends/Readme.md#testscsv) 

### now-weekly-case-rate-age.csv, now-weekly-hosp-rate-age.csv, now-weekly-death-rate-age.csv
These files contain weekly case, hospitalization, and death rates by age over the last 12 weeks. For details see [documentation at Trends](https://github.com/nychealth/coronavirus-data/tree/main/trends#weekly-case-rate-agecsv).

### now-weekly-case-rate-race.csv, now-weekly-hosp-rate-race.csv, now-weekly-death-rate-race.csv
These files contain weekly case, hospitalization, and death rates by race/ethnicity over the last 12 weeks. For details see [documentation at Trends](https://github.com/nychealth/coronavirus-data/tree/main/trends#weekly-case-rate-racecsv).

### pp-by-modzcta.csv 

This file contains person-level information on molecular testing: the percentage of people tested who tested positive in the 7 days preceding the indicated “end date,” stratified by day and by three different geographies: citywide, borough, MODZCTA. The level of geography is indicated in each column heading.

Please see the technical notes for a [description of MODZCTA](https://github.com/nychealth/coronavirus-data#geography), the different [types of COVID-19 laboratory tests](https://github.com/nychealth/coronavirus-data#laboratory-testing), and details on the [calculation of percent positivity](https://github.com/nychealth/coronavirus-data#calculation-of-percent-positivity). The data shown in this table are displayed by the date of specimen collection (i.e., when someone went to a healthcare provider for a test) for a molecular test.

Unlike other data in this repository, this file excludes patients in congregate facilities, and people who previously tested positive, to better track community transmission.

### 7day-transmission-rate.csv

This file contains the rate of confirmed and probable cases per 100,000 people in the past 7 days, stratified by day and three different geographies: citywide, borough, and United Hospital Fund (UHF) neighborhood. The level of geography is indicated following the underscore (_) in each column heading. Please see the technical notes for a [description of UHF neighborhoods](https://github.com/nychealth/coronavirus-data#geography). This metric is designed to align with the [Centers for Disease Control and Prevention levels of tranmissions](https://covid.cdc.gov/covid-data-tracker/#county-view).

Note that sum of counts in this file may not match values in citywide tables because of records with missing geographic information.

### now-transmission-by-uhf42.csv

This file contains the 7-day rate of confirmed and probable cases per 100,000 people, for the most recent day of data, by UHF24 (United Hospital Fund) neighborhood. 
