# totals/ 

This folder contains cumulative totals since the start of the COVID-19 outbreak in NYC, which the Health Department defines as the diagnosis of the first confirmed COVID-19 case on February 29, 2020. The Health Department recommends against interpreting daily changes to these files as one day’s worth of data, due to the difference between date of event and date of report.

## Files 

### by-group.csv

This file contains counts and rates of cases, hospitalizations, and deaths, stratified by age, sex, borough, race/ethnicity, and neighborhood poverty (low, medium, high, very high). Methods for determining neighborhood poverty are outlined in the technical notes ([Poverty Groups](https://github.com/nychealth/coronavirus-data#poverty-groups)). 

Rates are:   
- Cumulative since the start of the outbreak   
- Per 100,000 people by specified group   
- Age-adjusted according to [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf) for race/ethnicity and neighborhood poverty groups 

Indicators include: 

| Variable name | Definition | Timeframe | 
|--------------------|------------------------------------------------------------|------------| 
| group |Population group category | | 
| subgroup | Population subgroup: age group in years, sex, borough of residence, race/ethnicity, or neighborhood poverty group| | 
| CONFIRMED_CASE_RATE | Rate of confirmed cases per 100,000 people by age group | Cumulative | 
| CASE_RATE | Rate of confirmed and probable cases per 100,000 people by age group | Cumulative | 
| HOSPITALIZED_RATE | Rate of hospitalized confirmed and probable cases per 100,000 people by age group | Cumulative | 
| DEATH_RATE | Rate of total deaths per 100,000 people by age group | Cumulative | 
| CONFIRMED_CASE_COUNT | Number of confirmed cases by age group | Cumulative | 
| PROBABLE_CASE_COUNT | Number of probable cases by age group | Cumulative | 
| CASE_COUNT | Number of confirmed and probable cases by age group | Cumulative | 
| HOSPITALIZED_COUNT | Number of hospitalized confirmed and probable cases by age group | Cumulative | 
| DEATH_COUNT | Number of total deaths by age group | Cumulative | 

Note that sum of counts in this file may not match citywide values because of records with missing demographic information. 

Demograhic information is based on what is reported to the Health Department by laboratories. 

Due to the small number of cases reported among transgender and gender-nonconforming people, data on these cases are not included in this table at this time. Data on people identified as American Indian/Alaska Native, two or more races, or other races/ethnicities are not included in this table. The Hispanic/Latino category includes people of any race. Race/ethnicity information is most complete for people who have been hospitalized or have died. There are much less data currently available on race/ethnicity for people who have not been hospitalized.    

Differences in health outcomes among racial and ethnic groups are due to long-term institutional and personal biases against people of color. There is no evidence that these health inequities are due to personal traits. Lasting racism and an inequitable distribution of resources needed for wellness cause these health inequities. These resources include quality jobs, housing, health care and food, among others. The greater impact of the COVID-19 pandemic on people of color shows how these inequities influence health outcomes.

Note: this file replaces by-age.csv, by-boro.csv, by-poverty.csv, by-race.csv, and by-sex.csv. Those files are no longer being updated.

### data-by-modzcta.csv   

This file contains data by MODZCTA. Please see the technical notes for a description of MODZCTA ([Geography: Zip codes and ZCTAs](https://github.com/nychealth/coronavirus-data#geography-zip-codes-and-zctas)).

Indicators include: 

| Variable name | Definition | Timeframe | 
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------:| 
| MODIFIED_ZCTA | MODZCTA | |          
| NEIGHBORHOOD_NAME | Neighborhood name of the MODZCTA | |   
| BOROUGH_GROUP | Borough of the MODZCTA | | 
| LABEL | List of the ZCTAs that are bundled into the MODZCTA | |   
| LAT | Latitude of the central point within the MODZCTA | | 
| LONG | Longitude of the central point within the MODZCTA | |  
| COVID_CONFIRMED_CASE_COUNT | Number of confirmed cases by MODZCTA | Cumulative | 
| COVID_PROBABLE_CASE_COUNT | Number of probable cases by MODZCTA | Cumulative | 
| COVID_CASE_COUNT | Number of confirmed and probable cases by MODZCTA | Cumulative | 
| COVID_CONFIRMED_CASE_RATE | Rate of confirmed cases per 100,000 people by MODZCTA | Cumulative | 
| COVID_CASE_RATE | Rate of confirmed and probable cases per 100,000 people by MODZCTA | Cumulative | 
| POP_DENOMINATOR | Population denominators for MODZCTA derived from intercensal estimates by the Bureau of Epidemiology Services (see “Rates per 100,000 people” for more details) | | 
| COVID_DEATH_COUNT | Number of total deaths by MODZCTA | Cumulative | 
| COVID_DEATH_RATE | Rate of total deaths per 100,000 people by MODZCTA | Cumulative | 
| PERCENT_POSITIVE | Percentage of people ever tested for COVID-19 with a molecular test who tested positive by MODZCTA | Cumulative | 
| TOTAL_COVID_TESTS | Number of people tested for COVID-19 with a molecular test by MODZCTA | Cumulative | 

Neighborhood names represent the [Neighborhood Organizing Census Committee](https://www1.nyc.gov/site/census/index.page) boundaries, which were recently developed by the U.S. Census Bureau with input from community groups.  

Note that sum of counts in this file may not match values in citywide tables because of records with missing geographic information.

### deaths-by-boro-age.csv   

This file contains rates of deaths, by age group and borough of residence. Rates are:   

- Cumulative since the start of the outbreak   

- Per 100,000 people by age group and borough of residence  

Indicators include: 

| Variable name | Definition | Timeframe | 
|---------------|---------------------------------------------------------------------------------------------------|------------| 
| BOROUGH_GROUP | Borough of residence | |          
| AGE_0_17_YRS  | Rate of deaths among people aged 0-17 years per 100,000 people by borough of residence | Cumulative | 
| AGE_18_24_YRS | Rate of deaths among people aged 18-24 years per 100,000 people by borough of residence | Cumulative | 
| AGE_25_34_YRS | Rate of deaths among people aged 25-34 years per 100,000 people by borough of residence | Cumulative | 
| AGE_35_44_YRS | Rate of deaths among people aged 35-44 years per 100,000 people by borough of residence | Cumulative | 
| AGE_45_54_YRS | Rate of deaths among people aged 45-54 years per 100,000 people by borough of residence | Cumulative | 
| AGE_55_64_YRS | Rate of deaths among people aged 55-64 years per 100,000 people by borough of residence | Cumulative | 
| AGE_65_74_YRS | Rate of deaths among people aged 65-74 years per 100,000 people by borough of residence | Cumulative | 
| AGE_GE_75_YRS | Rate of deaths among people aged 75+ years per 100,000 people by borough of residence | Cumulative |
  
### deaths-by-race-age.csv    

This file contains rates of deaths, by age group and race/ethnicity group. Rates are:   

- Cumulative since the start of the outbreak   

- Per 100,000 people by age group and race/ethnicity group  

| Variable name | Definition | Timeframe | 
|---------------|---------------------------------------------------------------------------------------------------|------------| 
| RACE_GROUP | Race/ethnicity group | |          
| AGE_0_17_YRS | Rate of deaths among people aged 0-17 years per 100,000 people by race/ethnicity group | Cumulative | 
| AGE_18_24_YRS | Rate of deaths among people aged 18-24 years per 100,000 people by race/ethnicity group | Cumulative | 
| AGE_25_34_YRS | Rate of deaths among people aged 25-34 years per 100,000 people by race/ethnicity group | Cumulative | 
| AGE_35_44_YRS | Rate of deaths among people aged 35-44 years per 100,000 people by race/ethnicity group | Cumulative | 
| AGE_45_54_YRS | Rate of deaths among people aged 45-54 years per 100,000 people by race/ethnicity group | Cumulative | 
| AGE_55_64_YRS | Rate of deaths among people aged 55-64 years per 100,000 people by race/ethnicity group | Cumulative | 
| AGE_65_74_YRS | Rate of deaths among people aged 65-74 years per 100,000 people by race/ethnicity group | Cumulative | 
| AGE_GE_75_YRS | Rate of deaths among people aged 75+ years per 100,000 people by race/ethnicity groupy | Cumulative | 

Data on people identified as American Indian/Alaska Native, two or more races, or certain other races/ethnicities not listed are not included in this table. The Hispanic/Latino category includes people of any race. Race/ethnicity information is most complete for people who have been hospitalized or have died. There are much less data currently available on race/ethnicity for people who have not been hospitalized.

Differences in health outcomes among racial and ethnic groups are due to long-term institutional and personal biases against people of color. There is no evidence that these health inequities are due to personal traits. Lasting racism and an inequitable distribution of resources needed for wellness cause these health inequities. These resources include quality jobs, housing, health care and food, among others. The greater impact of the COVID-19 pandemic on people of color shows how these inequities influence health outcomes.

### group-cases-by-boro.csv 

This file contains borough-specific counts and rates of cases, by age group, race/ethnicity group, and sex as reported to the Health Department by laboratories. Rates are:   

- Cumulative since the start of the outbreak   

- Per 100,000 people by borough of residence and demographic groups   

Indicators include: 

| Variable name | Definition | Timeframe | 
|--------------|-----------------------------------------------------------------------------------|------------| 
| GROUP | Used for display purposes only | | 
| SUBGROUP | Indicates the age group in years, race/ethnicity group, or sex of stratification | |     
| Borough_CONFIRMED_CASE_COUNT | Number of confirmed cases in the indicated borough, by indicated group | Cumulative |  
| Borough_PROBABLE_CASE_COUNT | Number of probable cases in the indicated borough, by indicated group | Cumulative |    
| Borough_CASE_COUNT | Number of confirmed and probable cases in the indicated borough, by indicated group | Cumulative |  
| Borough_CONFIRMED_CASE_RATE | Rate of confirmed cases in indicated borough per 100,000 people by indicated group | Cumulative |
| Borough_CASE_RATE | Rate of confirmed and probable cases in indicated borough per 100,000 people by indicated group | Cumulative |        

Rates for race/ethnicity groups (Asian/Pacific-Islander, Black/African-American, Hispanic/Latino, White) are age-adjusted according to [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf). Data on people identified as American Indian/Alaska Native, two or more races, or certain other races/ethnicities not listed are not included in this table. The Hispanic/Latino category includes people of any race. Race/ethnicity information is most complete for people who have been hospitalized or have died. There are much less data currently available on race/ethnicity for people who have not been hospitalized.

Due to the small number of cases among transgender and gender-nonconforming people, data on these cases are not included in this table at this time. 

Note that sum of counts in this file may not match values in citywide tables because of records with missing demographic or geographic information.   

### group-data-by-boro.csv 

This file contains the same data as group-cases-by-boro.csv, group-hosp-by-boro.csv, and group-death-by-boro.csv, but combined for display purposes.

### group-death-by-boro.csv 

This file contains borough-specific counts and rates of deaths, by age group, race/ethnicity group, and sex as reported to the Health Department by laboratories. Rates are:   

- Cumulative since the start of the outbreak   

- Per 100,000 people by borough of residence and demographic groups   

Indicators include: 

| Variable name | Definition | Timeframe | 
|----------------|---------------------------------------------------------------------------------|------------| 
| GROUP | Used for display purposes only | | 
| SUBGROUP | Indicates the age group in years, race/ethnicity group, or sex of stratification | |    
| BK_DEATH_COUNT | Number of deaths in Brooklyn by indicated group | Cumulative |     
| BK_DEATH_RATE | Rate of deaths in Brooklyn per 100,000 people by indicated group | Cumulative |     
| BX_DEATH_COUNT | Number of deaths in the Bronx by indicated group| Cumulative |     
| BX_DEATH_RATE | Rate of deaths in the Bronx per 100,000 people by indicated group | Cumulative |     
| MN_DEATH_COUNT | Number of deaths in Manhattan by indicated group | Cumulative |     
| MN_DEATH_RATE | Rate of deaths in Manhattan per 100,000 people by indicated group | Cumulative |     
| QN_DEATH_COUNT | Number of deaths in Queens by indicated group | Cumulative |     
| QN_DEATH_RATE | Rate of deaths in Queens per 100,000 people by indicated group | Cumulative |     
| SI_DEATH_COUNT | Number of deaths in Staten Island by indicated group | Cumulative |     
| SI_DEATH_RATE | Rate of deaths in Staten Island per 100,000 people by indicated group | Cumulative |     

Rates for race/ethnicity groups (Asian/Pacific-Islander, Black/African-American, Hispanic/Latino, White) are age-adjusted according to [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf). Data on people identified as American Indian/Alaska Native, two or more races, or certain other races/ethnicities not listed are not included in this table. The Hispanic/Latino category includes people of any race. Race/ethnicity information is most complete for people who have been hospitalized or have died. There are much less data currently available on race/ethnicity for people who have not been hospitalized.

Due to the small number of cases among transgender and gender-nonconforming people, data on these cases are not included in this table at this time. 

Note that sum of counts in this file may not match values in citywide tables because of records with missing demographic or geographic information. 

### group-hosp-by-boro.csv 

This file contains borough-specific counts and rates of hospitalized cases, by age group, race/ethnicity group, and sex as reported to the Health Department by laboratories. Rates are:   

- Cumulative since the start of the outbreak   

- Per 100,000 people by borough of residence and demographic groups   

Indicators include: 

| Variable name | Definition | Timeframe | 
|--------------|-----------------------------------------------------------------------------------|------------| 
| GROUP | Used for display purposes only | | 
| SUBGROUP | Indicates the age group in years, race/ethnicity group, or sex of stratification | |          
| BK_HOSPITALIZED_COUNT | Number of hospitalized cases in Brooklyn by indicated group | Cumulative |     
| BK_HOSPITALIZED_RATE | Rate of hospitalized cases in Brooklyn per 100,000 people by indicated group | Cumulative |     
| BX_HOSPITALIZED_COUNT | Number of hospitalized cases in the Bronx by indicated group| Cumulative |     
| BX_HOSPITALIZED_RATE | Rate of hospitalized cases in the Bronx per 100,000 people by indicated group | Cumulative |     
| MN_HOSPITALIZED_COUNT | Number of hospitalized cases in Manhattan by indicated group | Cumulative |     
| MN_HOSPITALIZED_RATE | Rate of hospitalized cases in Manhattan per 100,000 people by indicated group | Cumulative |     
| QN_HOSPITALIZED_COUNT | Number of hospitalized cases in Queens by indicated group | Cumulative |     
| QN_HOSPITALIZED_RATE | Rate of hospitalized cases in Queens per 100,000 people by indicated group | Cumulative |     
| SI_HOSPITALIZED_COUNT | Number of hospitalized cases in Staten Island by indicated group | Cumulative |     
| SI_HOSPITALIZED_RATE | Rate of hospitalized cases in Staten Island per 100,000 people by indicated group | Cumulative |     

Rates for race/ethnicity groups (Asian/Pacific-Islander, Black/African-American, Hispanic/Latino, White) are age-adjusted according to [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf). Data on people identified as American Indian/Alaska Native, two or more races, or certain other races/ethnicities not listed are not included in this table. The Hispanic/Latino category includes people of any race. Race/ethnicity information is most complete for people who have been hospitalized or have died. There are much less data currently available on race/ethnicity for people who have not been hospitalized.

Due to the small number of cases among transgender and gender-nonconforming people, data on these cases are not included in this table at this time. 

Note that sum of counts in this file may not match values in citywide tables because of records with missing demographic or geographic information.

### summary.csv   

This file contains cumulative summary information, including the cut-off date and time for data included in the most recent update, and several citywide indicators.  

Hospitalization counts reflect the total number of people with COVID-19 ever admitted to a hospital, not the number of people currently admitted. Case and death counts reflect totals, separately.
