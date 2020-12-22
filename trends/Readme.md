# trends/ 

This folder contains files with daily or weekly data shown across time. Note that these trend data are published by date of event, not by date of report. The Health Department recommends against interpreting daily changes to these files as one day’s worth of data, due to the difference between date of event and date of report.

## Files 

### antibody-by-week.csv   

This file contains person-level information on antibody testing: the number of people who received a test, the number of people with positive results, the percentage of people tested who tested positive, stratified by week. Please see the technical notes  for a description of the different [types of COVID-19 laboratory tests](https://github.com/nychealth/coronavirus-data#laboratory-testing). The dates shown in this table reflect the date of specimen collection (i.e., when someone went to a healthcare provider for a test).

People with an antibody test are aggregated by full-weeks starting each Sunday and ending on Saturday. For example, a person whose blood was collected for antibody testing on Monday, October 12 would be categorized as tested during the week ending October 17. A person tested twice in one week would only be counted once in that week. 

This file includes data since the week ending April 11, 2020 based on when the Health Department started to receive a higher volume of antibody tests following the start of the COVID-19 outbreak in NYC.

Indicators include: 

| Variable Name | Definition | Timeframe |   
|-----------------|----------------------------------------------------------------------------|------------------------------------------| 
| WEEKDATE | Week-ending date | |       
| NUM_PEOP_TEST | Number of people who received an antibody test | Full week preceding the week-ending date |        
| NUM_PEOP_POS | Number of people with a positive result on an antibody test | Full week preceding the week-ending date  |     
| PERCENT_POSITIVE | Percentage of people tested with an antibody test who tested positive | Full week preceding the week-ending date |     
| INCOMPLETE | Used for display purposes only | |    

Note that one person can have more than one test during different weeks. Therefore, the sum of counts across weeks may not match summary values.  

### caserate-by-modzcta.csv 

This file contains the rate of confirmed cases per 100,000 people, stratified by week and three different geographies: citywide, borough, and modified ZIP Code Tabulation Area (MODZCTA). The level of geography is indicated following the underscore (_) in each column heading. Please see the technical notes for a description of MODZCTA ([Geography: Zip codes and ZCTAs](https://github.com/nychealth/coronavirus-data#geography-zip-codes-and-zctas)).

People with confirmed COVID-19 are categorized based on the date of diagnosis, and are aggregated by full-weeks starting each Sunday and ending on Saturday. For example, a person who was diagnosed with COVID-19 on Monday October 12 would be categorized as diagnosed during the week ending October 17. Note that sum of counts in this file may not match values in citywide tables because of records with missing geographic information.

### cases-by-day.csv  

This file contains citywide and borough-specific daily counts of probable and confirmed cases. Cases are aggregated by the date of diagnosis. To address variation in the number of cases diagnosed per day, we have included a 7-day average (mean). This is calculated as the average of number of cases on that day and the previous 6 days.

This file includes data since February 29, 2020 based on the date that the Health Department classifies as the start of the COVID-19 outbreak in NYC (i.e., date of the first laboratory-confirmed case). 

Indicators include: 

| Variable name | Definition | Timeframe | 
|--------------------------------|---------------------------------------------------------------|---------------------------------| 
| DATE_OF_INTEREST | Date of diagnosis | | 
| CASE_COUNT | Count of confirmed cases citywide | Day |  
| PROBABLE_CASE_COUNT | Count of probable cases citywide | Day |  
| CASE_COUNT_7DAY_AVG | 7-day average of count of confirmed cases citywide | Current day and previous 6 days | 
| ALL_CASE_COUNT_7DAY_AVG | 7-day average of count of confirmed and probable cases citywide | Current day and previous 6 days | 
| BX_CASE_COUNT | Count of confirmed cases in the Bronx | Day | 
| BX_PROBABLE_CASE_COUNT | Count of probable cases in the Bronx | Day |   
| BX_CASE_COUNT_7DAY_AVG | 7-day average of count of confirmed cases in the Bronx | Current day and previous 6 days | 
| BX_ALL_CASE_COUNT_7DAY_AVG | 7-day average of count of confirmed and probable cases in the Bronx | Current day and previous 6 days | 
| BK_CASE_COUNT | Count of confirmed cases in Brooklyn | Day |     
| BK_PROBABLE_CASE_COUNT | Count of probable cases in Brooklyn | Day |  
| BK_CASE_COUNT_7DAY_AVG | 7-day average of count of confirmed cases in Brooklyn | Current day and previous 6 days |
| BK_ALL_CASE_COUNT_7DAY_AVG | 7-day average of count of confirmed and probable cases in Brooklyn | Current day and previous 6 days | 
| MN_CASE_COUNT | Count of confirmed cases in Manhattan | Day | 
| MN_PROBABLE_CASE_COUNT | Count of probable cases in Manhattan | Day |  
| MN_CASE_COUNT_7DAY_AVG | 7-day average of count of confirmed cases in Manhattan | Current day and previous 6 days | 
| MN_ALL_CASE_COUNT_7DAY_AVG | 7-day average of count of confirmed and probable cases in Manhattan | Current day and previous 6 days |
| QN_CASE_COUNT | Count of confirmed cases in Queens | Day | 
| QN_PROBABLE_CASE_COUNT | Count of probable cases in Queens | Day | 
| QN_CASE_COUNT_7DAY_AVG | 7-day average of count of confirmed cases in Queens | Current day and previous 6 days | 
| QN_ALL_CASE_COUNT_7DAY_AVG | 7-day average of count of confirmed and probable cases in Queens | Current day and previous 6 days |
| SI_CASE_COUNT | Count of confirmed cases in Staten Island | Day |  
| SI_PROBABLE_CASE_COUNT | Count of probable cases in Staten Island | Day | 
| SI_CASE_COUNT_7DAY_AVG | 7-day average of count of confirmed cases in Staten Island | Current day and previous 6 days | 
| SI_ALL_CASE_COUNT_7DAY_AVG | 7-day average of count of confirmed and probable cases in Staten Island | Current day and previous 6 days |
| INCOMPLETE | Used for display purposes only | | 

Note that sum of counts in this file may not match values in citywide tables because of records with missing geographic information.

### covid-like-illness-by-boro.csv

This file includes the rate of visits to NYC emergency departments (ED) per 100,000 people, and rates of subsequent admissions to the hospital through the ED, for influenza-like illness, pneumonia, or COVID-like illness (defined as having the ICD-10-CM code (U07.1) for COVID-19 disease documented). Data are stratified by date of visit, age groups, and patient borough of residence. Please see additional details about the Health Department's [syndromic surveillance system](https://github.com/nychealth/coronavirus-data#syndromic-surveillance) in the key technical notes section.  

The data in this file go back to February 1, 2020, to provide a view of the early days of the COVID-19 outbreak in NYC.

Indicators include: 

| Variable name | Definition | Timeframe | 
|---------------------|---------------|----------------| 
| Date | Date of ED visit | |    
| Borough | Borough of residence | |    
| Admit_0_4 | Rate of hospital admissions among people aged 0-4 years per 100,000 people by borough of residence | Day | 
| Admit_5_12 | Rate of hospital admissions among people aged 5-12 years per 100,000 people by borough of residence | Day | 
| Admit_13_17 | Rate of hospital admissions among people aged 13-17 years per 100,000 people by borough of residence | Day | 
| Admit_18_24 | Rate of hospital admissions among people aged 18-24 years per 100,000 people by borough of residence | Day | 
| Admit_25_34| Rate of hospital admissions among people aged 25-34 years per 100,000 people by borough of residence | Day | 
| Admit_35_44| Rate of hospital admissions among people aged 35-44 years per 100,000 people by borough of residence | Day | 
| Admit_45_54 | Rate of hospital admissions among people aged 45-54 years per 100,000 people by borough of residence | Day | 
| Admit_55_64 | Rate of hospital admissions among people aged 55-64 years per 100,000 people by borough of residence | Day | 
| Admit_65_74 | Rate of hospital admissions among people aged 65-74 years per 100,000 people by borough of residence | Day | 
| Admit_75 | Rate of hospital admissions among people aged 75+ years per 100,000 people by borough of residence | Day | 
| Admit_All_ages | Rate of hospital admissions among people of all ages per 100,000 people by borough of residence | Day |    			           
| Visit_0_4 | Rate of ED visits among people aged 0-4 years per 100,000 people by borough of residence | Day | 
| Visit_5_12| Rate of ED visits among people aged 5-12 years per 100,000 people by borough of residence | Day | 
| Visit_13_17 | Rate of ED visits among people aged 13-17 years per 100,000 people by borough of residence | Day | 
| Visit_18_24 | Rate of ED visits among people aged 18-24 years per 100,000 people by borough of residence | Day | 
| Visit_25_34 | Rate of ED visits among people aged 25-34 years per 100,000 people by borough of residence | Day | 
| Visit_35_44 | Rate of ED visits among people aged 35-44 years per 100,000 people by borough of residence | Day | 
| Visit_45_54 | Rate of ED visits among people aged 45-54 years per 100,000 people by borough of residence | Day | 
| Visit_55_64 | Rate of ED visits among people aged 55-64 years per 100,000 people by borough of residence | Day | 
| Visit_65_74 | Rate of ED visits among people aged 65-74 years per 100,000 people by borough of residence | Day | 
| Visit_75 | Rate of ED visits among people aged 75+ years per 100,000 people by borough of residence | Day | 
| Visit_All_ages | Rate of ED visits among people of all ages per 100,000 people by borough of residence | Day |

### covid-like-illness.csv 

covid-like-illness.csv was previously called syndromic_data.csv. 

This file includes the rate of visits to NYC EDs per 100,000 people, and rates of subsequent admissions to the hospital through the ED, for influenza-like illness, pneumonia, or COVID-like illness (defined as having the ICD-10-CM code (U07.1) for COVID-19 disease documented). Data are stratified by date of visit and age group. Please see additional details about the Health Department's [syndromic surveillance system](https://github.com/nychealth/coronavirus-data#syndromic-surveillance) in the key technical notes section.

The data in this file go back to February 1, 2020, to provide a view of the early days of the COVID-19 outbreak in NYC.

Indicators include: 

| Variable name | Definition | Timeframe | 
|----------------|------------------------------------------------------------------------------|-----------| 
| Date | Date of ED visit | |    
| Admit_0_4 | Rate of hospital admissions among people aged 0-4 years per 100,000 people | Day | 
| Admit_5_12 | Rate of hospital admissions among people aged 5-12 years per 100,000 people | Day | 
| Admit_13_17 | Rate of hospital admissions among people aged 13-17 years per 100,000 people | Day | 
| Admit_18_24 | Rate of hospital admissions among people aged 18-24 years per 100,000 people | Day | 
| Admit_25_34 | Rate of hospital admissions among people aged 25-34 years per 100,000 people | Day | 
| Admit_35_44 | Rate of hospital admissions among people aged 35-44 years per 100,000 people | Day | 
| Admit_45_54 | Rate of hospital admissions among people aged 45-54 years per 100,000 people | Day | 
| Admit_55_64 | Rate of hospital admissions among people aged 55-64 years per 100,000 people | Day | 
| Admit_65_74  | Rate of hospital admissions among people aged 65-74 years per 100,000 people | Day | 
| Admit_75 | Rate of hospital admissions among people aged 75+ years per 100,000 people | Day | 
| Admit_All_ages | Rate of hospital admissions among people of all ages per 100,000 people | Day |                                   
| Visit_0_4 | Rate of ED visits among people aged 0-4 years per 100,000 people | Day | 
| Visit_5_12 | Rate of ED visits among people aged 5-12 years per 100,000 people | Day | 
| Visit_13_17 | Rate of ED visits among people aged 13-17 years per 100,000 people | Day | 
| Visit_18_24 | Rate of ED visits among people aged 18-24 years per 100,000 people | Day | 
| Visit_25_34 | Rate of ED visits among people aged 25-34 years per 100,000 people | Day | 
| Visit_35_44 | Rate of ED visits among people aged 35-44 years per 100,000 people | Day | 
| Visit_45_54 | Rate of ED visits among people aged 45-54 years per 100,000 people | Day | 
| Visit_55_64 | Rate of ED visits among people aged 55-64 years per 100,000 people | Day | 
| Visit_65_74 | Rate of ED visits among people aged 65-74 years per 100,000 people | Day | 
| Visit_75 | Rate of ED visits among people aged 75+ years per 100,000 people | Day | 
| Visit_All_ages | Rate of ED visits among people of all ages per 100,000 people | Day | 
  
### data-by-day.csv  

This file contains the same data as cases-by-day.csv, hosp-by-day.csv, and deaths-by-day.csv, but combined for display purposes.
   
### deaths-by-day.csv  

This file contains citywide and borough-specific daily counts of probable and confirmed deaths. Deaths are aggregated by the date of death. To address variation in the number of cases diagnosed per day, we have included a 7-day average (mean). This is calculated as the average of number of cases on that day and the previous 6 days.

This file includes data since February 29, 2020 based on the date that the Health Department classifies as the start of the COVID-19 outbreak in NYC (date of the first laboratory-confirmed case).  

Indicators include: 

| Variable name | Definition | Timeframe | 
|--------------------------------|---------------------------------------------------------------|---------------------------------| 
| DATE_OF_INTEREST | Date of death | |  
| DEATH_COUNT | Count of confirmed deaths citywide | Day | 
| PROBABLE_DEATH_COUNT | Count of probable deaths citywide | Day | 
| DEATH_COUNT_7DAY_AVG | 7-day average of count of confirmed deaths citywide | Current day and previous 6 days | 
| ALL_DEATH_COUNT_7DAY_AVG | 7-day average of count of confirmed and probable deaths citywide | Current day and previous 6 days | 
| BX_DEATH_COUNT | Count of confirmed deaths in the Bronx | Day | 
| BX_PROBABLE_DEATH_COUNT | Count of probable deaths in the Bronx | Day | 
| BX_DEATH_COUNT_7DAY_AVG | 7-day average of count of confirmed deaths in the Bronx | Current day and previous 6 days | 
| BX_ALL_DEATH_COUNT_7DAY_AVG | 7-day average of count of confirmed and probable deaths in the Bronx | Current day and previous 6 days | 
| BK_DEATH_COUNT | Count of confirmed deaths in Brooklyn | Day |  
| BK_PROBABLE_DEATH_COUNT | Count of probable deaths in Brooklyn | Day | 
| BK_DEATH_COUNT_7DAY_AVG | 7-day average of count of confirmed deaths in Brooklyn  | Current day and previous 6 days | 
| BK_ALL_DEATH_COUNT_7DAY_AVG | 7-day average of count of confirmed and probable deaths in Brooklyn | Current day and previous 6 days | 
| MN_DEATH_COUNT | Count of confirmed deaths in Manhattan | Day |  
| MN_PROBABLE_DEATH_COUNT | Count of probable deaths in Manhattan | Day | 
| MN_DEATH_COUNT_7DAY_AVG | 7-day average of count of confirmed deaths in Manhattan | Current day and previous 6 days |
| MN_ALL_DEATH_COUNT_7DAY_AVG | 7-day average of count of confirmed and probable deaths in Manhattan | Current day and previous 6 days |
| QN_DEATH_COUNT | Count of confirmed deaths in Queens | Day |
| QN_PROBABLE_DEATH_COUNT | Count of probable deaths in Queens | Day | 
| QN_DEATH_COUNT_7DAY_AVG | 7-day average of count of confirmed deaths in Queens | Current day and previous 6 days | 
| QN_ALL_DEATH_COUNT_7DAY_AVG | 7-day average of count of confirmed and probable deaths in Queens | Current day and previous 6 days |
| SI_DEATH_COUNT | Count of confirmed deaths in Staten Island | Day |  
| SI_PROBABLE_DEATH_COUNT | Count of probable deaths in Staten Island | Day | 
| SI_DEATH_COUNT_7DAY_AVG | 7-day average of count of confirmed deaths in Staten Island | Current day and previous 6 days | 
| SI_ALL_DEATH_COUNT_7DAY_AVG | 7-day average of count of confirmed and probable deaths in Staten Island  | Current day and previous 6 days |
| INCOMPLETE | Used for display purposes only | | 

Note that sum of counts in this file may not match values in citywide tables because of records with missing geographic information.
   
### hosp-by-day.csv  

This file contains citywide and borough-specific daily counts of hospitalizations. Hospitalizations are aggregated by the date of admission. To address variation in the number of cases who are hospitalized per day, we have included a 7-day average (mean). This is calculated as the average of number of hospitalizations on that day and the previous 6 days.

This file includes data since February 29, 2020 based on the date that the Health Department classifies as the start of the COVID-19 outbreak in NYC (date of the first laboratory-confirmed case). 

Indicators include: 

| Variable name | Definition | Timeframe | 
|--------------------------------|---------------------------------------------------------------|---------------------------------| 
| DATE_OF_INTEREST | Date of admission | |  
| HOSPITALIZED_COUNT | Count of hospitalized cases citywide | Day | 
| HOSP_COUNT_7DAY_AVG | 7-day average of count of hospitalized cases citywide | Current day and previous 6 days | 
| BX_HOSPITALIZED_COUNT | Count of hospitalized cases in the Bronx | Day | 
| BX_HOSPITALIZED_COUNT_7DAY_AVG | 7-day average of count of hospitalized cases in the Bronx | Current day and previous 6 days | 
| BK_HOSPITALIZED_COUNT | Count of hospitalized cases in Brooklyn | Day |  
| BK_HOSPITALIZED_COUNT_7DAY_AVG | 7-day average of count of hospitalized cases in Brooklyn | Current day and previous 6 days | 
| MN_HOSPITALIZED_COUNT | Count of hospitalized cases in Manhattan | Day |  
| MN_HOSPITALIZED_COUNT_7DAY_AVG | 7-day average of count of hospitalized cases in Manhattan | Current day and previous 6 days | 
| QN_HOSPITALIZED_COUNT | Count of hospitalized cases in Queens | Day |  
| QN_HOSPITALIZED_COUNT_7DAY_AVG | 7-day average of count of hospitalized cases in Queens | Current day and previous 6 days | 
| SI_HOSPITALIZED_COUNT | Count of hospitalized cases in Staten Island | Day |  
| SI_HOSPITALIZED_COUNT_7DAY_AVG | 7-day average of count of hospitalized cases in Staten Island | Current day and previous 6 days | 
| INCOMPLETE | Used for display purposes only | | 

Note that sum of counts in this file may not match values in citywide tables because of records with missing geographic information.
  
### percentpositive-by-modzcta.csv 

This file contains the percentage of people tested for COVID-19 with a molecular test who tested positive, stratified by week and three different geographies: citywide, borough, and MODZCTA. The level of geography is indicated following the underscore (_) in each column heading. Please see the technical notes for a description of MODZCTA ([Geography: Zip codes and ZCTAs](https://github.com/nychealth/coronavirus-data#geography-zip-codes-and-zctas)), the different [types of COVID-19 laboratory tests](https://github.com/nychealth/coronavirus-data#laboratory-testing), and details on the [calculation of percent positivity](https://github.com/nychealth/coronavirus-data#calculation-of-percent-positivity). The dates shown in this table reflect the date of specimen collection (i.e., when someone went to a healthcare provider for a test).

People with a molecular test are aggregated by full-weeks starting each Sunday and ending on Saturday. For example, a person who had a nasal swab collected for molecular testing on Monday October 12 would be categorized as tested during the week ending October 17. A person tested twice in one week would only be counted once in that week. Therefore, the number of tests conducted in a week will differ from the number of people tested (as reported in other files) for the same week.
  
### testing-by-age.csv  

This file contains person-level information on molecular testing: the number of people who received a test, the percentage of people tested who tested positive and the rate of testing per 100,000 people, stratified by week and age group. Please see the technical notes for a description of the different [types of COVID-19 laboratory tests](https://github.com/nychealth/coronavirus-data#laboratory-testing). The dates shown in this table reflect the date of specimen collection (i.e., when someone went to a healthcare provider for a test).

People with a molecular test are aggregated by full-weeks starting each Sunday and ending on Saturday. For example, a person who had a nasal swab collected for molecular testing on Monday October 12 would be categorized as tested during the week ending October 17. A person tested twice in one week would only be counted once in that week. 

This file includes data since the week ending March 7, 2020 based on when the Health Department started to receive a higher volume of molecular tests following the start of the COVID-19 outbreak in NYC.

Indicators include: 

| Variable name | Definition | Timeframe |  
|-------------------|----------------------------------------------------------------------------------|------------------------------------------| 
| WEEK_ENDING | Week-ending date | | 
| PERPOS_ALL_AGEG | Percentage of people tested with a molecular test who tested positive among people of all ages | Full week preceding the week-ending date | 
| TESTRATE_ALL_AGEG | Rate of molecular testing per 100,000 among people of all ages | Full week preceding the week-ending date | 
| NUMTEST_ALL_AGEG | Number of people who received a molecular test among people of all ages | Full week preceding the week-ending date | 
| PERPOS_0_4 | Percentage of people aged 0-4 years tested with a molecular test who tested positive | Full week preceding the week-ending date |
| TESTRATE_0_4 | Rate of molecular testing per 100,000 people aged 0-4 years | Full week preceding the week-ending date | 
| NUMTEST_0_4 | Number of people aged 0-4 years who received a molecular test | Full week preceding the week-ending date | 
| PERPOS_5_12 | Percentage of people aged 5-12 years tested with a molecular test who tested positive | Full week preceding the week-ending date |
| TESTRATE_5_12 | Rate of molecular testing per 100,000 people aged 5-12 years | Full week preceding the week-ending date | 
| NUMTEST_5_12 | Number of people aged 5-12 years who received a molecular test | Full week preceding the week-ending date | 
| PERPOS_13_17 | Percentage of people aged 13-17 years tested with a molecular test who tested positive | Full week preceding the week-ending date | 
| TESTRATE_13_17 | Rate of molecular testing per 100,000 people aged 13-17 years | Full week preceding the week-ending date | 
| NUMTEST_13_17 | Number of people aged 13-17 years who received a molecular test | Full week preceding the week-ending date | 
| PERPOS_18_24 | Percentage of people aged 18-24 years tested with a molecular test who tested positive | Full week preceding the week-ending date | 
| TESTRATE_18_24 | Rate of molecular testing per 100,000 people aged 18-24 years | Full week preceding the week-ending date | 
| NUMTEST_18_24 | Number of people aged 18-24 years who received a molecular test | Full week preceding the week-ending date | 
| PERPOS_25_34 | Percentage of people aged 25-34 years tested with a molecular test who tested positive | Full week preceding the week-ending date |
| TESTRATE_25_34 | Rate of molecular testing per 100,000 people aged 25-34 years | Full week preceding the week-ending date | 
| NUMTEST_25_34 | Number of people aged 25-34 years who received a molecular test | Full week preceding the week-ending date | 
| PERPOS_35_44 | Percentage of people aged 35-44 years tested with a molecular test who tested positive | Full week preceding the week-ending date | 
| TESTRATE_35_44 | Rate of molecular testing per 100,000 people aged 35-44 years | Full week preceding the week-ending date | 
| NUMTEST_35_44 | Number of people aged 35-44 years who received a molecular test | Full week preceding the week-ending date | 
| PERPOS_45_54 | Percentage of people aged 45-54 years tested with a molecular test who tested positive | Full week preceding the week-ending date | 
| TESTRATE_45_54 | Rate of molecular testing per 100,000 people aged 45-54 years | Full week preceding the week-ending date | 
| NUMTEST_45_54 | Number of people aged 45-54 years who received a molecular test | Full week preceding the week-ending date | 
| PERPOS_55_64 | Percentage of people aged 55-64 years tested with a molecular test who tested positive | Full week preceding the week-ending date | 
| TESTRATE_55_64 | Rate of molecular testing per 100,000 people aged 55-64 years | Full week preceding the week-ending date | 
| NUMTEST_55_64 | Number of people aged 55-64 years who received a molecular test | Full week preceding the week-ending date | 
| PERPOS_65_74 | Percentage of people aged 65-74 years tested with a molecular test who tested positive | Full week preceding the week-ending date | 
| TESTRATE_65_74 | Rate of molecular testing per 100,000 people aged 65-74 years | Full week preceding the week-ending date | 
| NUMTEST_65_74 | Number of people aged 65-74 years who received a molecular test | Full week preceding the week-ending date | 
| PERPOS_75UP | Percentage of people aged 75+ years tested with a molecular test who tested positive | Full week preceding the week-ending date |
| TESTRATE_75UP | Rate of molecular testing per 100,000 people aged 75+ years | Full week preceding the week-ending date | 
| NUMTEST_75UP4 | Number of people aged 75+ years who received a molecular test | Full week preceding the week-ending date | 

Note that one person can have more than one test during different weeks. Therefore, the sum of counts across weeks may not match summary values. 

### testing-turnaround.csv

This file contains test-level information on molecular tests, stratified by week. Please see the technical notes for a description of the different [types of COVID-19 laboratory tests](https://github.com/nychealth/coronavirus-data#laboratory-testing). The dates shown in this table reflect the date of specimen collection (i.e., when someone went to a healthcare provider for a test).

Molecular tests are aggregated by full-weeks starting each Sunday and ending on Saturday. For example, a nasal swab collected for molecular testing on Monday October 12 would be categorized as tested during the week ending October 17.

This file includes data since the week ending March 7, 2020 based on when the Health Department started to receive a higher volume of molecular tests following the start of the COVID-19 outbreak in NYC.

| Variable Name | Definition | Timeframe |   
| -------------------|-----------------------------------------------------------------------|-----------|   
| WEEK_END | Week-ending date | |       
| TESTS | Number of molecular tests conducted | Week |        
| PERCENT_24HR | Percent of molecular tests with results reported within 24 hours  | Full week preceding the week-ending date |     
| PERCENT_48HR | Percent of molecular tests with results reported within 48 hours | Full week preceding the week-ending date |     
| LAG_MEDIAN | Median turnaround time (half of molecular tests have results reported faster than this time), in days | Full week preceding the week-ending date |  
| LAG_25TH_PERCENTILE | 25th percentile turnaround time (1 out of 4 molecular tests have results reported *faster* than this time), in days | Full week preceding the week-ending date | 
| LAG_75TH_PERCENTILE | 75th percentile turnaround time (1 out of 4 molecular tests have results reported *slower* than this time), in days | Full week preceding the week-ending date | 

Note that one person can have more than one test on different days. Therefore, the number of tests conducted in a week will differ from the number of people tested (as reported in other files) for the same week.

### testrate-by-modzcta.csv 

This file contains the rate of molecular testing per 100,000 people, stratified by week and three different geographies: citywide, borough, and MODZCTA. The level of geography is indicated following the underscore (_) in each column heading. Please see the technical notes for a description of MODZCTA ([Geography: Zip codes and ZCTAs](https://github.com/nychealth/coronavirus-data#geography-zip-codes-and-zctas)), and the different [types of COVID-19 laboratory tests](https://github.com/nychealth/coronavirus-data#laboratory-testing). The dates shown in this table reflect the date of specimen collection (i.e., when someone went to a healthcare provider for a test).

People with a molecular test are aggregated by full-weeks starting each Sunday and ending on Saturday. For example, a person who had a nasal swab collected for molecular testing on Monday October 12 would be categorized as tested during the week ending October 17. A person tested twice in one week would only be counted once in that week. Therefore, the number of tests conducted in a week will differ from the number of people tested (as reported in other files) for the same week.

### tests.csv   

This file contains person-level information on molecular and antigen testing: the number of people who received a test, the number of people with positive results, the percentage of people tested who tested positive, stratified by day and test type. Please see the technical notes for a description of the different [types of COVID-19 laboratory tests](https://github.com/nychealth/coronavirus-data#laboratory-testing), and details on the [calculation of percent positivity](https://github.com/nychealth/coronavirus-data#calculation-of-percent-positivity). The dates shown in this table reflect the date of specimen collection (i.e., when someone went to a healthcare provider for a test).

This file includes data since March 3, 2020 based on when the Health Department started to receive a higher volume of molecular tests following the start of the COVID-19 outbreak in NYC. Please note that antigen testing started to become more widely available in NYC in October 2020. The Health Department consistently receives electronic reports *only* for COVID-19 tests that are conducted in laboratories, and tests that are conducted at point-of-care (e.g., antigen tests) may not be routinely reported to the Health Department, especially if the test result is negative.

Indicators include: 

| Variable name | Definition | Timeframe |  
| -------------------------|----------------------------------------------------------------------------------|-------------------------------| 
| DATE | Date of specimen collection | | 
| TOTAL_TESTS | Number of people who received a molecular test  | Day | 
| POSTITIVE_TESTS | Number of people with a positive result on a molecular test | Day | 
| PERCENT_POSITIVE | Percentage of people tested with a molecular test who tested positive |  Day | 
| TOTAL_TESTS_7DAYS_AVG | 7-day average of number of people who received a molecular test | Current day and previous 6 days | 
| POSITIVE_TESTS_7DAYS_AVG | 7-day average of number of people with a positive result on a molecular test | Current day and previous 6 days | 
| PERCENT_POSITIVE_7DAYS_AVG | 7-day average of percentage of people tested with a molecular test who tested positive | Current day and 6 previous days | 
| TOTAL_ANTIGEN_TESTS | Number of people who received an antigen test  | Day | 
| TOTAL_ANTIGEN_TESTS_7DAYS_AVG | 7-day average of number of people who received an antigen test | Current day and previous 6 days | 
| INCOMPLETE | Used for display purposes only | | 

Note that one person can have more than one test on different days. Therefore, the number of positive persons every day will be different from the counts of confirmed or probable cases, which will count people only on the first day they test positive.  
