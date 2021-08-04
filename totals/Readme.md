# totals/ 

This folder contains cumulative totals since the start of the COVID-19 outbreak in NYC, which the Health Department defines as the diagnosis of the first confirmed COVID-19 case on February 29, 2020. The Health Department recommends against interpreting daily changes to these files as one day’s worth of data, due to the difference between date of event and date of report.

## Files 

### antibody-by-age.csv   

This file contains person-level information on antibody testing: the number of people who received a test, the number of people with positive results, the percentage of people tested who tested positive, and the rate of testing per 100,000 people, stratified by age group. Please see the technical notes for a description of the different [types of COVID-19 laboratory tests](https://github.com/nychealth/coronavirus-data#laboratory-testing).

Indicators include: 

| Variable Name | Definition | Timeframe | 
|------------------|----------------------------------------------------------------------------------------|------------| 
| DEMO_VARIABLE | Age group in years | |     
| NUM_PEOP_TEST | Number of people who received an antibody test by age group  | Cumulative |      
| NUM_PEOP_POS | Number of people with a positive result on an antibody test by age group | Cumulative |   
| PERCENT_POSITIVE | Percentage of people tested with an antibody test who tested positive by age group | Cumulative |
| TEST_RATE | Rate of antibody testing per 100,000 people by age group | Cumulative | 

The sum of counts may not match summary values because of records with missing demographic information.

### antibody-by-boro.csv   

This file contains person-level information on antibody testing: the number of people who received a test, the number of people with positive results, the percentage of people tested who tested positive, and the rate of testing per 100,000 people, stratified by borough of residence. Please see the technical notes for a description of the different [types of COVID-19 laboratory tests](https://github.com/nychealth/coronavirus-data#laboratory-testing).

Indicators include: 

| Variable Name | Definition | Timeframe | 
|------------------|----------------------------------------------------------------------------------------------------|------------|  
| DEMO_VARIABLE | Borough of residence | |     
| NUM_PEOP_TEST | Number of people who received an antibody test by borough of residence | Cumulative |      
| NUM_PEOP_POS | Number of people with a positive result on an antibody test by borough of residence | Cumulative |   
| PERCENT_POSITIVE | Percentage of people tested with an antibody test who tested positive by borough of residence | Cumulative |
| TEST_RATE | Rate of antibody testing per 100,000 people by borough of residence | Cumulative | 

The sum of counts may not match summary values because of records with missing geographic information.

### antibody-by-modzcta.csv   

This file contains person-level information on antibody testing: the number of people who received a test, the number of people with positive results, the percentage of people tested who tested positive, and the rate of antibody testing per 100,000 people, stratified by modified ZIP code tabulation areas (MODZCTA). Please see the technical notes for a description of MODZCTA ([Geography: Zip codes and ZCTAs](https://github.com/nychealth/coronavirus-data#geography-zip-codes-and-zctas)), and the different [types of COVID-19 laboratory tests](https://github.com/nychealth/coronavirus-data#laboratory-testing).

Indicators include: 

| Variable Name | Definition | Timeframe | 
|------------------|---------------------------------------------------------------------------------------------|------------|
| MODZCTA_FIRST| MODZCTA | |     
| NEIGHBORHOOD_NAME | Neighborhood name of the MODZCTA | |   
| LABEL | List of the ZIP Code Tabulation Areas (ZCTAs) that are bundled into the MODZCTA | |   
| LAT | Latitude of the central point within the MODZCTA | | 
| LONG | Longitude of the central point within the MODZCTA | |  
| NUM_PEOP_TEST | Number of people who received an antibody test by MODZCTA | Cumulative |      
| NUM_PEOP_POS | Number of people with a positive result on an antibody test by MODZCTA | Cumulative |   
| PERCENT_POSITIVE | Percentage of people tested with an antibody test who tested positive by MODZCTA | Cumulative |   
| TEST_RATE | Rate of antibody testing per 100,000 people by MODZCTA | Cumulative |   

Neighborhood names represent the [Neighborhood Organizing Census Committee](https://www1.nyc.gov/site/census/index.page) boundaries, which were recently developed by the U.S. Census Bureau with input from community groups. 

The sum of counts may not match summary values because of records with missing geographic information.

### antibody-by-poverty.csv   

This file contains person-level information on antibody testing: the number of people who received a test, the number of people with positive results, the percentage of people tested who tested positive, and the rate of testing per 100,000 people, stratified by ZCTA-level neighborhood poverty group in NYC (low, medium, high, very high). Please see the technical notes for a description of methods for determining neighborhood poverty ([Poverty Groups](https://github.com/nychealth/coronavirus-data#poverty-groups)), and the different [types of COVID-19 laboratory tests](https://github.com/nychealth/coronavirus-data#laboratory-testing)).

Indicators include: 

| Variable Name | Definition | Timeframe | 
|------------------|----------------------------------------------------------------------------------------------------------|------------:|  
| DEMO_VARIABLE| ZCTA-level neighborhood poverty group | |     
| NUM_PEOP_TEST | Number of people who received an antibody test by neighborhood poverty group  | Cumulative |      
| NUM_PEOP_POS | Number of people with a positive result on an antibody test by neighborhood poverty group | Cumulative |   
| PERCENT_POSITIVE | Percentage of people tested with an antibody test who tested positive by neighborhood poverty group | Cumulative |   
| TEST_RATE | Rate of antibody testing per 100,000 people by neighborhood poverty group | Cumulative | 

The sum of counts may not match summary values because of records with missing geographic information.

### antibody-by-sex.csv   

This file contains person-level information on antibody testing: the number of people who received a test, the number of people with positive results, the percentage of people tested who tested positive, and the rate of testing per 100,000 people, stratified by sex as reported to the Health Department by laboratories. Please see the technical notes for a description of the different [types of COVID-19 laboratory tests](https://github.com/nychealth/coronavirus-data#laboratory-testing).

Indicators include: 

| Variable Name | Definition | Timeframe | 
|------------------|-----------------------------------------------------------------------------------|------------| 
| DEMO_VARIABLE | Sex reported to the Health Department by laboratories | |     
| NUM_PEOP_TEST | Number of people who received an antibody test by sex | Cumulative |      
| NUM_PEOP_POS | Number of people with a positive result on an antibody test by sex | Cumulative |   
| PERCENT_POSITIVE | Percentage of people tested with an antibody test who tested positive by sex | Cumulative |   
| TEST_RATE | Rate of antibody testing per 100,000 people by sex | Cumulative | 

Due to the small number of cases among transgender and gender-nonconforming people, data on these cases are not included in this table at this time.

The sum of counts may not match summary values because of records with missing demographic information.

### by-age.csv   

This file contains counts and rates of confirmed cases, hospitalizations, and deaths, by age group. Rates are:   

- Cumulative since the start of the outbreak   

- Per 100,000 people by age group   

Indicators include: 

| Variable name | Definition | Timeframe | 
|--------------------|------------------------------------------------------------|------------| 
| AGE_GROUP | Age group in years | | 
| CONFIRMED_CASE_RATE | Rate of confirmed cases per 100,000 people by age group | Cumulative | 
| CASE_RATE | Rate of confirmed and probable cases per 100,000 people by age group | Cumulative | 
| HOSPITALIZED_RATE | Rate of hospitalized cases per 100,000 people by age group | Cumulative | 
| DEATH_RATE | Rate of confirmed deaths per 100,000 people by age group | Cumulative | 
| CONFIRMED_CASE_COUNT | Number of confirmed cases by age group | Cumulative | 
| PROBABLE_CASE_COUNT | Number of probable cases by age group | Cumulative | 
| CASE_COUNT | Number of confirmed and probable cases by age group | Cumulative | 
| HOSPITALIZED_COUNT | Number of hospitalized cases by age group | Cumulative | 
| DEATH_COUNT | Number of confirmed deaths by age group | Cumulative | 

Note that sum of counts in this file may not match citywide values because of records with missing demographic information. This file does not contain information on probable deaths.   

### by-boro.csv   

This file contains counts and rates of confirmed cases, hospitalizations, and deaths, by borough of residence. Rates are:   

- Cumulative since the start of the outbreak   

- Per 100,000 people by borough of residence  

Indicators include: 

| Variable name | Definition | Timeframe | 
|--------------------|-----------------------------------------------------------------------|------------|
| BOROUGH | Borough of residence | | 
| CONFIRMED_CASE_RATE | Rate of confirmed cases per 100,000 people by borough of residence | Cumulative | 
| CASE_RATE | Rate of confirmed and probable cases per 100,000 people by borough of residence | Cumulative | 
| HOSPITALIZED_RATE | Rate of hospitalized cases per 100,000 people by borough of residence | Cumulative | 
| DEATH_RATE | Rate of confirmed deaths per 100,000 people by borough of residence | Cumulative | 
| CONFIRMED_CASE_COUNT | Number of confirmed cases by borough of residence | Cumulative | 
| PROBABLE_CASE_COUNT | Number of probable cases by borough of residence | Cumulative | 
| CASE_COUNT | Number of confirmed and probable cases by borough of residence | Cumulative | 
| HOSPITALIZED_COUNT | Number of hospitalized cases by borough of residence | Cumulative | 
| DEATH_COUNT | Number of confirmed deaths by borough of residence | Cumulative | 

Note that sum of counts in this file may not match values in citywide tables because of records with missing geographic information. This file does not contain information on probable deaths.  

### by-group.csv
This file contains the contents of by-age.csv, by-boro.csv, by-poverty.csv, by-race.csv, and by-sex.csv.

### by-poverty.csv   

This file contains counts and rates of confirmed cases, hospitalizations, and deaths, by ZCTA-level neighborhood poverty group in NYC (low, medium, high, very high). Methods for determining neighborhood poverty are outlined in the technical notes (Poverty Groups). Rates are:    

- Cumulative since the start of the outbreak   

- Age-adjusted according to [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf)   

- Per 100,000 people by neighborhood poverty group     

Indicators include: 

| Variable name | Definition | Timeframe | 
|-----------------------|------------------------------------------------------------------------------------------|------------|
| POVERTY_GROUP | ZCTA-level neighborhood poverty group | |  
| CONFIRMED_CASE_RATE_ADJ | Age-adjusted rate of confirmed cases per 100,000 people by neighborhood poverty group | Cumulative |     
| CASE_RATE_ADJ | Age-adjusted rate of confirmed and probable cases per 100,000 people by neighborhood poverty group | Cumulative |     
| HOSPITALIZED_RATE_ADJ | Age-adjusted rate of hospitalized cases per 100,000 people by neighborhood poverty group | Cumulative |   
| DEATH_RATE_ADJ | Age-adjusted rate of confirmed deaths per 100,000 people by neighborhood poverty group | Cumulative | 
| CONFIRMED_CASE_COUNT | Number of confirmed cases by neighborhood poverty group | Cumulative |     
| CASE_COUNT | Number of confirmed and probable cases by neighborhood poverty group | Cumulative |     
| HOSPITALIZED_COUNT | Number of hospitalized cases by neighborhood poverty group | Cumulative | 
| DEATH_COUNT | Number of confirmed deaths by neighborhood poverty group | Cumulative | 

Note that sum of counts in this file may not match citywide values because of records with missing geographic information. This file does not contain information on probable deaths.     

### by-race.csv   

This file contains counts and rates of confirmed cases, hospitalizations, and deaths by race/ethnicity group. Rates are:   

- Cumulative since the start of the outbreak   

- Age-adjusted according to [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf)  

- Per 100,000 people by race/ethnicity group   

Indicators include: 

| Variable name | Definition | Timeframe | 
|-----------------------|------------------------------------------------------------------------------------|------------|
| RACE_GROUP | Race/ethnicity group | |        
| CONFIRMED_CASE_RATE_ADJ | Age-adjusted rate of confirmed cases per 100,000 people by race/ethnicity group | Cumulative |     
| CASE_RATE_ADJ | Age-adjusted rate of confirmed and probable cases per 100,000 people by race/ethnicity group | Cumulative |     
| HOSPITALIZED_RATE_ADJ | Age-adjusted rate of hospitalized cases per 100,000 people by race/ethnicity group | Cumulative |   
| DEATH_RATE_ADJ | Age-adjusted rate of confirmed deaths per 100,000 people by race/ethnicity group | Cumulative | 
| CONFIRMED_CASE_COUNT | Number of confirmed cases by race/ethnicity group | Cumulative |     
| CASE_COUNT | Number of confirmed and probable cases by race/ethnicity group | Cumulative |     
| HOSPITALIZED_COUNT | Number of hospitalized cases by race/ethnicity group | Cumulative | 
| DEATH_COUNT | Number of confirmed deaths by race/ethnicity group | Cumulative | 
  
Data on people identified as American Indian/Alaska Native, two or more races, or other races/ethnicities are not included in this table. The Hispanic/Latino category includes people of any race. Race/ethnicity information is most complete for people who have been hospitalized or have died. There are much less data currently available on race/ethnicity for people who have not been hospitalized.    

Note that sum of counts in this file may not match citywide values because of records with missing demographic information. This file does not contain information on probable deaths.     

Differences in health outcomes among racial and ethnic groups are due to long-term institutional and personal biases against people of color. There is no evidence that these health inequities are due to personal traits. Lasting racism and an inequitable distribution of resources needed for wellness cause these health inequities. These resources include quality jobs, housing, health care and food, among others. The greater impact of the COVID-19 pandemic on people of color shows how these inequities influence health outcomes.

### by-sex.csv   

This file contains counts and rates of confirmed cases, hospitalizations, and deaths, by sex as reported to the Health Department by laboratories. Rates are:   

- Cumulative since the start of the outbreak   

- Per 100,000 people by sex   

Indicators include: 

| Variable name | Definition | Timeframe | 
|--------------------|------------------------------------------------------|------------| 
| SEX_GROUP | Sex reported to the Health Department by laboratories | |          
| CONFIRMED_CASE_RATE | Rate of confirmed cases per 100,000 people by sex | Cumulative |     
| CASE_RATE | Rate of confirmed and probable cases per 100,000 people by sex | Cumulative |     
| HOSPITALIZED_RATE | Rate of hospitalized cases per 100,000 people by sex | Cumulative |   
| DEATH_RATE | Rate of confirmed deaths per 100,000 people by sex | Cumulative | 
| CONFIRMED_CASE_COUNT | Number of confirmed cases by sex | Cumulative |     
| CASE_COUNT | Number of confirmed and probable cases by sex | Cumulative |     
| HOSPITALIZED_COUNT | Number of hospitalized cases by sex | Cumulative | 
| DEATH_COUNT | Number of confirmed deaths by sex | Cumulative | 

Due to the small number of cases reported among transgender and gender-nonconforming people, data on these cases are not included in this table at this time.   

Note that sum of counts in this file may not match citywide values because of records with missing demographic information. This file does not contain information on probable deaths.   

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
| COVID_CASE_COUNT | Number of confirmed cases by MODZCTA | Cumulative | 
| COVID_CASE_RATE | Rate of confirmed cases per 100,000 people by MODZCTA | Cumulative | 
| POP_DENOMINATOR | Population denominators for MODZCTA derived from intercensal estimates by the Bureau of Epidemiology Services (see “Rates per 100,000 people” for more details) | | 
| COVID_DEATH_COUNT | Number of confirmed deaths by MODZCTA | Cumulative | 
| COVID_DEATH_RATE | Rate of confirmed deaths per 100,000 people by MODZCTA | Cumulative | 
| PERCENT_POSITIVE | Percentage of people ever tested for COVID-19 with a molecular test who tested positive by MODZCTA | Cumulative | 
| TOTAL_COVID_TESTS | Number of people tested for COVID-19 with a molecular test by MODZCTA | Cumulative | 

Neighborhood names represent the [Neighborhood Organizing Census Committee](https://www1.nyc.gov/site/census/index.page) boundaries, which were recently developed by the U.S. Census Bureau with input from community groups.  

Note that sum of counts in this file may not match values in citywide tables because of records with missing geographic information. This file does not contain information on probable deaths.    

### deaths-by-boro-age.csv   

This file contains rates of confirmed deaths, by age group and borough of residence. This file does not contain information on probable deaths. Rates are:   

- Cumulative since the start of the outbreak   

- Per 100,000 people by age group and borough of residence  

Indicators include: 

| Variable name | Definition | Timeframe | 
|---------------|---------------------------------------------------------------------------------------------------|------------| 
| BOROUGH_GROUP | Borough of residence | |          
| AGE_0_17_YRS  | Rate of confirmed deaths among people aged 0-17 years per 100,000 people by borough of residence | Cumulative | 
| AGE_18_24_YRS | Rate of confirmed deaths among people aged 18-24 years per 100,000 people by borough of residence | Cumulative | 
| AGE_25_34_YRS | Rate of confirmed deaths among people aged 25-34 years per 100,000 people by borough of residence | Cumulative | 
| AGE_35_44_YRS | Rate of confirmed deaths among people aged 35-44 years per 100,000 people by borough of residence | Cumulative | 
| AGE_45_54_YRS | Rate of confirmed deaths among people aged 45-54 years per 100,000 people by borough of residence | Cumulative | 
| AGE_55_64_YRS | Rate of confirmed deaths among people aged 55-64 years per 100,000 people by borough of residence | Cumulative | 
| AGE_65_74_YRS | Rate of confirmed deaths among people aged 65-74 years per 100,000 people by borough of residence | Cumulative | 
| AGE_GE_75_YRS | Rate of confirmed deaths among people aged 75+ years per 100,000 people by borough of residence | Cumulative |
  
### deaths-by-race-age.csv    

This file contains rates of confirmed deaths, by age group and race/ethnicity group. This file does not contain information on probable deaths. Rates are:   

- Cumulative since the start of the outbreak   

- Per 100,000 people by age group and race/ethnicity group  

| Variable name | Definition | Timeframe | 
|---------------|---------------------------------------------------------------------------------------------------|------------| 
| RACE_GROUP | Race/ethnicity group | |          
| AGE_0_17_YRS | Rate of confirmed deaths among people aged 0-17 years per 100,000 people by race/ethnicity group | Cumulative | 
| AGE_18_24_YRS | Rate of confirmed deaths among people aged 18-24 years per 100,000 people by race/ethnicity group | Cumulative | 
| AGE_25_34_YRS | Rate of confirmed deaths among people aged 25-34 years per 100,000 people by race/ethnicity group | Cumulative | 
| AGE_35_44_YRS | Rate of confirmed deaths among people aged 35-44 years per 100,000 people by race/ethnicity group | Cumulative | 
| AGE_45_54_YRS | Rate of confirmed deaths among people aged 45-54 years per 100,000 people by race/ethnicity group | Cumulative | 
| AGE_55_64_YRS | Rate of confirmed deaths among people aged 55-64 years per 100,000 people by race/ethnicity group | Cumulative | 
| AGE_65_74_YRS | Rate of confirmed deaths among people aged 65-74 years per 100,000 people by race/ethnicity group | Cumulative | 
| AGE_GE_75_YRS | Rate of confirmed deaths among people aged 75+ years per 100,000 people by race/ethnicity groupy | Cumulative | 

Data on people identified as American Indian/Alaska Native, two or more races, or certain other races/ethnicities not listed are not included in this table. The Hispanic/Latino category includes people of any race. Race/ethnicity information is most complete for people who have been hospitalized or have died. There are much less data currently available on race/ethnicity for people who have not been hospitalized.

Differences in health outcomes among racial and ethnic groups are due to long-term institutional and personal biases against people of color. There is no evidence that these health inequities are due to personal traits. Lasting racism and an inequitable distribution of resources needed for wellness cause these health inequities. These resources include quality jobs, housing, health care and food, among others. The greater impact of the COVID-19 pandemic on people of color shows how these inequities influence health outcomes.

### deaths-by-underlying-condition.csv   

This file contains cumulative counts, by age group and whether underlying conditions were present, absent, or not known. Underlying conditions currently include diabetes, lung disease, cancer, immunodeficiency, heart disease, hypertension, asthma, kidney disease, gastrointestinal/liver disease, and obesity. “Pending” refers to cases that are still under investigation. This file does not contain information on probable deaths.  

Indicators include: 

| Variable name | Definition | Timeframe | 
|-----------------------------|------------------------------------------------------------------------------------------------|------------| 
| AGE_GROUP | Age group in years | |          
| DEATH_COUNT_TOTAL | Number of confirmed deaths by age group | Cumulative | 
| DEATH_COUNT_ILLNESS | Number of confirmed deaths among people with underlying conditions by age group | Cumulative | 
| DEATH_COUNT_NO_ILLNESS | Number of confirmed deaths among people with no underlying conditions by age group | Cumulative | 
| DEATH_COUNT_PENDING_ILLNESS | Number of confirmed deaths among people under investigation for underlying illness by age group | Cumulative |

### group-cases-by-boro.csv 

This file contains borough-specific counts and rates of confirmed cases, by age group, race/ethnicity group, and sex as reported to the Health Department by laboratories. Rates are:   

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

This file contains borough-specific counts and rates of confirmed deaths, by age group, race/ethnicity group, and sex as reported to the Health Department by laboratories. Rates are:   

- Cumulative since the start of the outbreak   

- Per 100,000 people by borough of residence and demographic groups   

Indicators include: 

| Variable name | Definition | Timeframe | 
|----------------|---------------------------------------------------------------------------------|------------| 
| GROUP | Used for display purposes only | | 
| SUBGROUP | Indicates the age group in years, race/ethnicity group, or sex of stratification | |    
| BK_DEATH_COUNT | Number of confirmed deaths in Brooklyn by indicated group | Cumulative |     
| BK_DEATH_RATE | Rate of confirmed deaths in Brooklyn per 100,000 people by indicated group | Cumulative |     
| BX_DEATH_COUNT | Number of confirmed deaths in the Bronx by indicated group| Cumulative |     
| BX_DEATH_RATE | Rate of confirmed deaths in the Bronx per 100,000 people by indicated group | Cumulative |     
| MN_DEATH_COUNT | Number of confirmed deaths in Manhattan by indicated group | Cumulative |     
| MN_DEATH_RATE | Rate of confirmed deaths in Manhattan per 100,000 people by indicated group | Cumulative |     
| QN_DEATH_COUNT | Number of confirmed deaths in Queens by indicated group | Cumulative |     
| QN_DEATH_RATE | Rate of confirmed deaths in Queens per 100,000 people by indicated group | Cumulative |     
| SI_DEATH_COUNT | Number of confirmed deaths in Staten Island by indicated group | Cumulative |     
| SI_DEATH_RATE | Rate of confirmed deaths in Staten Island per 100,000 people by indicated group | Cumulative |     

Rates for race/ethnicity groups (Asian/Pacific-Islander, Black/African-American, Hispanic/Latino, White) are age-adjusted according to [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf). Data on people identified as American Indian/Alaska Native, two or more races, or certain other races/ethnicities not listed are not included in this table. The Hispanic/Latino category includes people of any race. Race/ethnicity information is most complete for people who have been hospitalized or have died. There are much less data currently available on race/ethnicity for people who have not been hospitalized.

Due to the small number of cases among transgender and gender-nonconforming people, data on these cases are not included in this table at this time. 

Note that sum of counts in this file may not match values in citywide tables because of records with missing demographic or geographic information. This file does not contain information on probable deaths.

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

### probable-confirmed-by-age.csv   

This file contains counts of confirmed and probable deaths, by age group. Data on probable deaths that are missing demographic information are classified as “Data pending.”

Indicators include: 

| Variable name | Definition | Timeframe | 
|-----------------|----------------------------------------|------------| 
| AGE_GROUP | Age group in years | |          
| CONFIRMED_DEATH | Number of confirmed deaths by age group | Cumulative | 
| PROBABLE_DEATH | Number of probable deaths by age group | Cumulative | 

 Note that sum of counts in this file may not match citywide values because of records with missing demographic information.  

### probable-confirmed-by-boro.csv   

This file contains counts of confirmed and probable deaths, by borough of residence. Data on probable deaths that are missing demographic information are classified as “Data pending.” 

Indicators include: 

| Variable name | Definition | Timeframe | 
|-----------------|---------------------------------------------------|------------| 
| BOROUGH_GROUP | Borough of residence | |          
| CONFIRMED_DEATH | Number of confirmed deaths by borough of residence | Cumulative | 
| PROBABLE_DEATH | Number of probable deaths by borough of residence | Cumulative | 

Note that sum of counts in this file may not match citywide values because of records with missing demographic information.   

### probable-confirmed-by-location.csv   

This file contains counts of confirmed and probable deaths, by location of death. The “Hospital/Emergency room” category includes any hospital-associated death, including deaths that occurred in the emergency department, an inpatient ward, or intensive care unit. The “Nursing home/Hospice” category includes any death that occurred in an assisted living or long-term care facility. The “Other/Unknown” category includes deaths that occurred in any setting not listed in this table, including patients who were dead on arrival at the hospital or for whom information on location of death is unknown.

Indicators include: 

| Variable name | Definition | Timeframe | 
|-------------------|------------------------------------------------|------------| 
| LOCATION_OF_DEATH | Location of death | |          
| CONFIRMED_DEATH | Number of confirmed deaths by location of death | Cumulative | 
| PROBABLE_DEATH | Number of probable deaths by location of death | Cumulative | 

Note that sum of counts in this file may not match citywide values because of records with missing information.  

### probable-confirmed-by-race.csv   

This file contains counts of confirmed and probable deaths, by race/ethnicity group. Data on probable deaths that are missing demographic information are classified as “Data pending.”

Indicators include: 

| Variable name | Definition | Timeframe | 
|-----------------|---------------------------------------------------|------------| 
| RACE_GROUP | Race/ethnicity group | |          
| CONFIRMED_DEATH | Number of confirmed deaths by race/ethnicity group | Cumulative | 
| PROBABLE_DEATH | Number of probable deaths by race/ethnicity group | Cumulative | 

Data on people identified as American Indian/Alaska Native, two or more races, or another race/ethnicity not listed are included in the “Other/Unknown” category. The Hispanic/Latino category includes people of any race.    

Note that sum of counts in this file may not match citywide values because of records with missing demographic information.

Differences in health outcomes among racial and ethnic groups are due to long-term institutional and personal biases against people of color. There is no evidence that these health inequities are due to personal traits. Lasting racism and an inequitable distribution of resources needed for wellness cause these health inequities. These resources include quality jobs, housing, health care and food, among others. The greater impact of the COVID-19 pandemic on people of color shows how these inequities influence health outcomes.  

### probable-confirmed-by-sex.csv   

This file contains counts of confirmed and probable deaths, by sex as reported to the Health Department. Data on probable deaths that are missing demographic information are classified as “Data pending.”

Indicators include: 

| Variable name | Definition | Timeframe | 
|-----------------|----------------------------------|------------| 
| SEX | Sex reported to the Health Department | |           
| CONFIRMED_DEATH | Number of confirmed deaths by sex | Cumulative | 
| PROBABLE_DEATH | Number of probable deaths by sex | Cumulative | 

Due to the small number of cases among transgender and gender-nonconforming people, data on these cases are not included in this table at this time.

Note that sum of counts in this file may not match citywide values because of records with missing demographic information.  

### summary.csv   

This file contains cumulative summary information, including the cut-off date and time for data included in the most recent update, and several citywide indicators.  

Hospitalization counts reflect the total number of people with COVID-19 ever admitted to a hospital, not the number of people currently admitted. Case and death counts reflect both confirmed and probable classifications, separately.
