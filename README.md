  # NYC Coronavirus Disease 2019 (COVID-19) Data   
This repository contains data on Coronavirus Disease 2019 (COVID-19) in New York City. Data are updated daily, which the exception of all tables in the testing and recent data folders which are updated weekly on Thursday. You can view visualizations of these data on the [Health Department’s COVID-19 Data webpage](https://www1.nyc.gov/site/doh/covid/covid-19-data.page). Additional data related to COVID-19 are available via [NYC Open Data](https://data.cityofnewyork.us/browse?category=Health&q=covid). 

Data are preliminary and subject to change. Information on this page will change as data and documentation are updated.   

The Health Department classifies the start of the outbreak in NYC as the date of the first laboratory-confirmed case, February 29, 2020.   

## Key notes  
### Report date versus date of event 
Due to lags common with surveillance data, we receive reports of events (diagnoses, hospitalizations and deaths) that happened on past days. We publish trend data (e.g., case-hosp-death.csv) using date of event (date of diagnosis, date of hospitalization or date of death), not date of report.  

Publishing data by date of event better reflects when things actually happened, as opposed to when the Health Department learned about them. We strongly discourage data users from using daily changes to cumulative files as trend data – this is prone to misuse and misinterpretation.  

### Questions and custom requests 
- We will answer questions about the data in this repository as we are able to. If you have a question, please search the [Issues](https://github.com/nychealth/coronavirus-data/issues?q=) to see if it’s already been addressed.  
- We are not able to accommodate custom data requests placed via Github.   

### Types of Surveillance   
The Health Department conducts two main types of surveillance for COVID-19:    
- Syndromic surveillance   
- Reportable disease surveillance   

#### Syndromic Surveillance   
We receive data from all 53 hospital emergency departments (EDs) in NYC about the types of illnesses people experience on a regular basis. This surveillance allows the Health Department to evaluate care-seeking trends at hospitals for influenza-like illness and pneumonia.    

The information on each patient is evaluated for descriptions that resemble influenza-like illness or pneumonia. Influenza-like illness is defined as mention of either:   
- Fever and cough     
- Fever and sore throat   
- Fever and shortness of breath or difficulty breathing 
- Influenza   
  
Pneumonia is defined as mention of or diagnosis of pneumonia. Since the signs and symptoms of COVID-19 overlap with these categories that the Health Department tracks routinely, we are able to identify unusual spikes in people seeking care at hospitals. We are using this as a proxy measure to observe COVID-19-like disease in the population.   
*Strengths*:  The data show real-time, population-level trends of people seeking health care for COVID-like disease.   
*Limitations*: The data do not represent patients with laboratory-confirmed COVID-19.   

#### Reportable Disease Surveillance 
The Health Department receives electronic laboratory reports for a number of infectious diseases, including COVID-19, as required by law in the [NYC Health Code](https://www1.nyc.gov/site/doh/providers/reporting-and-services/notifiable-diseases-and-conditions-reporting-central.page). When a specimen is collected from a patient for laboratory testing for the virus that causes COVID-19, the laboratory must report all results, whether positive, negative, or inconclusive, to the Health Department. Demographic information on the person being tested is reported to the Health Department, including name, address, and date of birth.   


There are two categories of COVID-19 tests: 
- *Diagnostic tests*: The primary test for COVID-19 infection is the polymerase chain reaction (PCR) test. The PCR test works through direct detection of viral RNA, and typically involves collecting a nasal swab. The [laboratory criteria](https://cdn.ymaws.com/www.cste.org/resource/resmgr/2020ps/Interim-20-ID-01_COVID-19.pdf) for reporting a person with confirmed COVID-19 infection (“case”) are based on the PCR test, and as such, all of the confirmed COVID-19 cases reported out by the Health Department represent people with PCR positive tests. 
- *Antibody tests*: Exposure to COVID-19 can be detected by measuring antibodies, which can reflect a person’s immune response to the virus. Antibodies are proteins produced by the body’s immune system that can be found in the blood. People can test positive for antibodies after they have been exposed, sometimes when they no longer test positive for the virus itself. It is important to note that the science around COVID-19 antibody tests is evolving rapidly and there is still much uncertainty about what individual and population level antibody test results mean for the epidemiology of COVID-19.   
 
*Strengths*: This standard reporting system allows for rapid and detailed information to be transmitted routinely to the Health Department.     
*Limitations*:  
- Because of delays in reporting, the most recent data may be incomplete. Current data will be updated in the future as information on laboratory tests are reported to the Health Department. 

- Health Department recommendations for testing have changed throughout the COVID-19 outbreak. For the first few months of the outbreak, the Health Department previously advised people with mild to moderate symptoms to stay at home and not seek testing to conserve testing supplies and personal protective equipment. Consequently, many cases in the community early in the outbreak were never diagnosed with a laboratory test and  will not be included in these counts.    
- The data include information from patients who reside in congregate facilities, such as correctional facilities and long-term care facilities. While data reported from these facilities may sometimes influence local trends, cases reported from these facilities do not necessarily represent community-based transmission.  
- Information on reported deaths can be limited by delays in reporting by hospitals or funeral homes.    
- These data only provide information on people tested. People receiving an antibody test may be systematically different from other people in the city; therefore, these data may not reflect antibody prevalence among all New Yorkers. Increasing instances of screening programs further impact the generalizability of these data, as screening programs influence who and how many people are tested over time. Examples of screening programs in NYC include: employers screening their workers (e.g., hospitals), and long-term care facility screening. 
- There may be potential biases toward people receiving an antibody test having a positive result because people who were previously ill are preferentially seeking testing, in addition to the testing of persons with higher exposure (e.g., health care workers, first responders) 
- These data are based on electronic laboratory reports, which often lack information on demographic and clinical characteristics of interest, such as race and ethnicity, co-occurring medical conditions, presence and onset date of COVID-19 symptoms, or occupation. 

***   

## Technical Notes   

### Case reporting   
NYC COVID-19 data include people who live in NYC or who live in another country but are being treated in NYC. The data do not include people who live outside of NYC but in the United States.   

### Rates vs. Cases   
The Health Department is reporting rates of cases, hospitalizations, and deaths in addition to counts. We report rates to give clear comparisons between different groups — such as borough, sex, or age — with differently sized populations. For example, we may report that the rate of confirmed COVID-19 cases is 100 per 100,000 population in NYC. That means for every 100,000 people living in NYC, there are 100 people diagnosed with COVID-19.   

### Changes to Reported Data   
We update data for earlier dates after we resolve testing and reporting delays. Reported data reflect what we know at the time of the report, not what occurred in real time. For example, we may find that a person who was originally reported to live in NYC no longer does. This person would be removed from our dataset after their address is updated, and our case count would decrease by one.    
  
### Rates per 100,000 People   
Rates for annual citywide-, borough-, ZCTA (ZIP Code Tabulation Area)-, and demographic-specific categories were calculated using interpolated intercensal population estimates updated in 2019. These rates differ from previously reported rates based on the 2000 Census or previous versions of population estimates. The Health Department produced these population estimates based on estimates from the U.S. Census Bureau and NYC Department of City Planning.    

Rates of cases, hospitalizations, and deaths for poverty and race/ethnicity groups were calculated using direct standardization for age at diagnosis and weighting by [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf).   

### Geography: ZIP codes and ZCTAs  
We report information by geography using modified ZIP Code Tabulation Areas (ZCTA). It can be challenging to map data that are reported by ZIP Code. A ZIP Code doesn’t actually refer to an area, but rather a collection of points that make up a mail delivery route. Furthermore, there are some buildings that have their own ZIP Code, and some non-residential areas with ZIP Codes.  

To deal with the challenges of ZIP Codes, the Health Department uses ZCTAs which solidify ZIP codes into units of area. Often, data reported by ZIP code are actually mapped by ZCTA. The ZCTA geography was developed by the U.S. Census Bureau.  

The Health Department sometimes reports data by modified ZCTA, which combines census blocks with smaller populations to allow more stable estimates of population size for rate calculation.  

### Poverty Groups   
Neighborhood-level poverty groups were classified in a manner consistent with Health Department practices to [describe and monitor disparities in health in NYC](https://www1.nyc.gov/assets/doh/downloads/pdf/epi/epiresearch-SES-measure.pdf). Neighborhood poverty measures are defined as the percentage of people earning below the Federal Poverty Threshold (FPT) within a ZCTA. The standard cut-points for defining categories of neighborhood-level poverty in NYC are:    
- Low: <10% of residents in ZCTA living below the FPT   
- Medium: 10% to <20%   
- High: 20% to <30%    
- Very high: ≥30% residents living below the FPT   
  
### Age Groups  
We are reporting out data for the following age groups: 0-17, 18-44, 45-64, 65-74, and 75+. We use these age groups because we found COVID-19 trends to be similar within these groups.   

### Reporting on Hospitalization Status  
The Health Department imports information on hospitalization status from a number of partners, including hospitals, hospital systems, and Regional Health Information Organizations, into our surveillance database. Because data from these partners can be incomplete, the Health Department also estimates the number of people diagnosed with COVID-19 who have ever been hospitalized by matching confirmed cases to other sources of hospital admission information. These other sources include:   
- The Health Department’s syndromic surveillance database that tracks daily hospital admissions from all 53 emergency departments across NYC   
- Regional health information organizations 
- NYC public hospitals 
- DOHMH’s electronic death registry system 
- Remote access to electronic health record systems  

Note that hospitalization information can be missing or incomplete from a number of facilities, which is a limitation for any analysis considering hospitalization status by geography (e.g., borough).   

### Reporting on COVID-19 Deaths  
COVID-19 deaths are reported from March 11, 2020 as this was the first date of death for a patient with confirmed COVID-19.   

There are two classifications of COVID-19 deaths reported:   
- A death is classified as **confirmed** if the decedent was an NYC resident who had a positive laboratory test for the virus that causes COVID-19.   
- A death is classified as **probable** if the decedent was an NYC resident (or residency pending) who had no known positive laboratory test for the virus that causes COVID-19 but the death certificate lists “COVID-19” or an equivalent as a cause of death.   
  
As new information becomes available, some deaths previously classified as probable may be reclassified as confirmed.  

Starting in June, 2020, people who died more than 60 days after their COVID-19 diagnosis and who did not have "COVID" or similar listed on their death certificate have been removed from the death count. This is to address instances in which somebody contracted COVID-19 and survived it, but later died.

Differences between death counts between NYC and New York State: Data on deaths reported by NYC are derived from the Health Department’s surveillance database and will be different from data reported by the New York State Department of Health. The State Department of Health reports data on deaths from:   
- The State Hospital Emergency Response Data System   
- Daily calls to hospitals and other facilities that are caring for patients, such as nursing homes   

The NYC Health Department reports data on deaths that reflect both:   
- Positive tests for COVID-19 confirmed by laboratories   
- Confirmations of a person’s death from the City’s Office of the Chief Medical Examiner and our Bureau of Vital Statistics, which is responsible for the registration, analysis and reporting of all deaths in NYC   
  
### Race and Ethnicity  
Race and ethnicity information is often missing in reportable disease surveillance. Information on race/ethnicity typically comes from electronic laboratory reports and unfortunately, race/ethnicity data is often missing in laboratory reports. For the COVID-19 response, the Health Department has electronically imported aggregated data from partners such as hospitals, hospital systems, or Regional Health Information Organizations to improve the completeness of race/ethnicity data for hospitalized people. However, health records may also be missing the race/ethnicity information. Additionally, the Health Department is working to import race/ethnicity information for people who have died. However, this information is often incomplete or not immediately available because it can take a few days for the information to be entered into the electronic death registration system. Race/ethnicity information is typically collected by funeral directors from next of kin of the decedent. 

Racial health inequities result from a history of structural and institutional racism against people of color. These inequities do not represent personal characteristics of people in these groups. Rather, they represent the effects of long term practices that promote (or fail to end) inequities. Persistent, systemic, and intergenerational systems of oppression manifest in the form of unequal access to basic resources necessary to ensure wellness, including employment, housing, food, green spaces, and health care. In the aggregate, people of color are denied resources that are more often available to white people. The structural inequities that result are further endangering people of color during this pandemic, leading to greater risk of harm to their health. 

***   
  
## Files   
### boro.csv   
This file contains counts and rates of confirmed cases, by NYC borough of residence. Rates are:   
- Cumulative since the start of the outbreak   
- Per 100,000 people by borough of residence  

This file is no longer being updated. For data by borough, see by-boro.csv or files in Boro\.   

### by-boro.csv   
This file contains counts and rates of confirmed cases, hospitalizations, and deaths, by NYC borough of residence. Rates are:   
- Cumulative since the start of the outbreak   
- Per 100,000 people by borough of residence  

Indicators include: 

| Variable name      | Definition                                                            | Timeframe  |
| -------------------|-----------------------------------------------------------------------|-----------:| 
| BOROUGH            | Borough                                                               |            |
| CASE_RATE          | Rate of confirmed cases per 100,000 people by borough of residence    | Cumulative |
| HOSPITALIZED_RATE  | Rate of hospitalized cases per 100,000 people by borough of residence | Cumulative |
| DEATH_RATE         | Rate of confirmed deaths per 100,000 people by borough of residence   | Cumulative |
| CASE_COUNT         | Count of confirmed cases                                              | Cumulative |
| HOSPITALIZED_COUNT | Count of hospitalized cases                                           | Cumulative |
| DEATH_COUNT        | Count of confirmed deaths                                             | Cumulative |

 Note that sum of counts in this file may not match values in Citywide tables because of records with missing geographic information. This file does not contain information on probable deaths.  

### by-age.csv   
This file contains counts and rates of confirmed cases, hospitalizations, and deaths, by age group. Rates are:   
- Cumulative since the start of the outbreak   
- Per 100,000 people by age group   

Indicators include: 

| Variable name      | Definition                                                            | Timeframe  |
| -------------------|-----------------------------------------------------------------------|-----------:| 
| AGE_GROUP          | Age group, in years                                                   |            |
| CASE_RATE          | Rate of confirmed cases per 100,000 people by borough of residence    | Cumulative |
| HOSPITALIZED_RATE  | Rate of hospitalized cases per 100,000 people by borough of residence | Cumulative |
| DEATH_RATE         | Rate of confirmed deaths per 100,000 people by borough of residence   | Cumulative |
| CASE_COUNT         | Count of confirmed cases                                              | Cumulative |
| HOSPITALIZED_COUNT | Count of hospitalized cases                                           | Cumulative |
| DEATH_COUNT        | Count of confirmed deaths                                             | Cumulative |

Note that sum of counts in this file may not match Citywide values because of records with missing demographic information. This file does not contain information on probable deaths.   

### by-sex.csv   
This file contains counts and rates of confirmed cases, hospitalizations, and deaths, by sex as reported to the Health Department by laboratories. Rates are:   
- Cumulative since the start of the outbreak   
- Per 100,000 people by sex   

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| SEX_GROUP| Sex| |          
| CASE_RATE| Rate of confirmed cases per 100,000 people by sex| Cumulative |     
| HOSPITALIZED_RATE | Rate of hospitalized cases per 100,000 people by sex | Cumulative |   
| DEATH_RATE | Rate of confirmed deaths per 100,000 people by sex | Cumulative | 
| CASE_COUNT| Count of confirmed cases | Cumulative |     
| HOSPITALIZED_COUNT | Count of hospitalized cases  | Cumulative | 
| DEATH_COUNT | Count of confirmed deaths  | Cumulative | 

Due to the small number of cases among transgender and gender-nonconforming people, data on these cases are not included in this table at this time.   

Note that sum of counts in this file may not match Citywide values because of records with missing demographic information. This file does not contain information on probable deaths.   

### by-poverty.csv   
This file contains counts and rates of confirmed cases, hospitalizations, and deaths, by ZCTA-level neighborhood poverty group in NYC (low, medium, high, very high). Methods for determining neighborhood poverty are outlined in technical notes above (Poverty Groups). Rates are:    
- Cumulative since the start of the outbreak   
- Age-adjusted according to [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf)   
- Per 100,000 people by ZCTA of residence      

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| POVERTY_GROUP| ZCTA-level neighborhood poverty group| |          
| CASE_RATE_ADJ| Age-adjusted rate of confirmed cases per 100,000 people by ZCTA of residence | Cumulative |     
| HOSPITALIZED_RATE_ADJ | Age-adjusted rate of hospitalized cases per 100,000 people by ZCTA of residence | Cumulative |   
| DEATH_RATE_ADJ | Age-adjusted rate of confirmed deaths per 100,000 people by ZCTA of residence | Cumulative | 
| CASE_COUNT| Count of confirmed cases | Cumulative |     
| HOSPITALIZED_COUNT | Count of hospitalized cases  | Cumulative | 
| DEATH_COUNT | Count of confirmed deaths  | Cumulative | 

Note that sum of counts in this file may not match Citywide values because of records with missing geographic information. This file does not contain information on probable deaths.     

### by-race.csv   
This file contains counts and rates of confirmed cases, hospitalizations, and deaths by race/ethnicity group. Rates are:   
- Cumulative since the start of the outbreak   
- Age-adjusted according to [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf)  
- Per 100,000 people by race/ethnicity group   

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| RACE_GROUP| Race/ethnicity group| |        
| CASE_RATE_ADJ| Age-adjusted rate of confirmed cases per 100,000 people by race/ethnicity group | Cumulative |     
| HOSPITALIZED_RATE_ADJ | Age-adjusted rate of hospitalized cases per 100,000 people by race/ethnicity group | Cumulative |   
| DEATH_RATE_ADJ | Age-adjusted rate of confirmed deaths per 100,000 people by race/ethnicity group | Cumulative | 
| CASE_COUNT| Count of confirmed cases | Cumulative |     
| HOSPITALIZED_COUNT | Count of hospitalized cases  | Cumulative | 
| DEATH_COUNT | Count of confirmed deaths  | Cumulative |   

Data on people identified as American Indian/Alaska Native, two or more races, or other races/ethnicities not listed are not included in this table. The Hispanic/Latino category includes people of any race. Race/ethnicity information is most complete for people who have been hospitalized or have died. There are much less data currently available on race/ethnicity group for non-hospitalized cases.    

Note that sum of counts in this file may not match Citywide values because of records with missing demographic information. This file does not contain information on probable deaths.     

### case-hosp-death.csv   
This file contains daily counts of confirmed cases, hospitalizations, and deaths. To address variation in cases diagnosed per day, we have included a rolling 7-day average (mean) of daily case counts. This is calculated as the average of cases diagnosed on that day and the previous 6 days.  This file does not contain information on probable deaths. Counts are aggregated separately by the following dates of interest:  
- Cases are by date of diagnosis   
- Hospitalizations are by date of admission    
- Deaths are by date of death   

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| DATE_OF_INTEREST| Date of diagnosis (cases), date of admission (hospitalizations), date of death (deaths)| |          
| CASE_COUNT| Count of confirmed cases | Day |     
| HOSPITALIZED_COUNT | Count of hospitalized cases  | Day | 
| DEATH_COUNT | Count of confirmed deaths  | Day | 
| CASE_COUNT_7DAY_AVG | 7-day average of count of confirmed cases | Current day and previous 6 days|  
| INCOMPLETE | Used for display purposes only | N/A | 

Because of delays in reporting, the most recent data may be incomplete. This file includes a display variable set at a fixed value for the most recent 7 days, to indicate the period in which data in the chart on the website are most likely to be incomplete. Data shown currently will be updated in the future as new information on cases, hospitalizations, and deaths are reported.   

### data-by-modzcta.csv   
This file contains data by modified ZIP code tabulation areas (ZCTA). This unit of geography is similar to ZIP codes but combines census blocks with smaller populations to allow more stable estimates of population size for rate calculation.  Please see description of modified ZCTAs in the technical notes section (Geography: Zip codes and ZCTAs).   

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| MODIFIED_ZCTA | Modified ZIP code tabulation areas (ZCTA) | |          
| NEIGHBORHOOD_NAME | Neighborhood names represent the [Neighborhood Organizing Census Committee](https://www1.nyc.gov/site/census/index.page) boundaries, which were recently developed by the U.S. Census Bureau with input from community groups | |   
| BOROUGH| Borough of the modified ZCTA | | 
| COVID_CASE_COUNT| Count of confirmed cases | Cumulative | 
| COVID_CASE_RATE| Rate of confirmed cases per 100,000 people by modified ZCTA| Cumulative | 
| POP_DENOMINATOR | Population denominators for modified ZCTAs derived from intercensal estimates by the Bureau of Epidemiology Services (see “Rates per 100,000 people” for more details) | Cumulative | 
| COVID_DEATH_COUNT| Count of confirmed deaths| Cumulative | 
| COVID_DEATH_RATE| Rate of confirmed deaths per 100,000 people by modified ZCTA| Cumulative | 
| PERCENT_POSITIVE| Percentage of people ever tested for COVID-19 with a polymerase chain reaction (PCR) test who tested positive | Cumulative | 
| TOTAL_COVID_TESTS | Count of people tested for COVID-19 with a PCR test | Cumulative | 



Neighborhood names represent the [Neighborhood Organizing Census Committee](https://www1.nyc.gov/site/census/index.page) boundaries, which were recently developed by the U.S. Census Bureau with input from community groups.  

Note that sum of counts in this file may not match values in Citywide tables because of records with missing geographic information. This file does not contain information on probable deaths.    

### summary.csv   
This file contains summary information, including the cut-off date and time for data included in this update, and cumulative counts of cases, hospitalizations, and deaths.     

Hospitalization counts reflect the total number of people with COVID-19 ever admitted to a hospital, not the number of people currently admitted. Death counts reflect both confirmed and probable deaths, separately.  

### syndromic-data.csv and syndromic-data-4-week.csv  
These files includes the rate of visits to NYC emergency departments (ED) per 100,000 people, and rates of subsequent admissions to the hospital through the ED, for influenza-like illness or pneumonia, by date of visit for all ages and by age group (0-17, 18-44, 45-64, 65-74, 75+ years). Syndromic-data-4-week.csv includes the most recent 28 days, and syndromic-data.csv is since February 1, 2020 based on the Health Department’s syndromic surveillance system.   

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| DATE | Date of emergency department visit | Cumulative |    
| Admit 0-17 | Rate of hospital admissions per 100,000 people by age group | Cumulative | 
| Admit 18-44 | Rate of hospital admissions per 100,000 people by age group | Cumulative | 
| Admit 45-64 | Rate of hospital admissions per 100,000 people by age group | Cumulative | 
| Admit 65-74 | Rate of hospital admissions per 100,000 people by age group | Cumulative | 
| Admit 75+ | Rate of hospital admissions per 100,000 people by age group | Cumulative | 
| Admit All ages | Rate of hospital admissions per 100,000 people | Cumulative | 
| Visit 0-17 | Rate of emergency department visits per 100,000 people by age group | Cumulative | 
| Visit 18-44 | Rate of emergency department visits per 100,000 people by age group | Cumulative | 
| Visit 45-64 | Rate of emergency department visits per 100,000 people by age group | Cumulative | 
| Visit 65-74 | Rate of emergency department visits per 100,000 people by age group | Cumulative | 
| Visit 75+ | Rate of emergency department visits per 100,000 people by age group | Cumulative | 
| Visit All ages | Rate of emergency department visits per 100,000 people | Cumulative | 

### tests.csv   
This file contains the number of people who received a polymerase chain reaction (PCR) test by day, the number of people with positive results by day, and the percent of all people tested who were positive by day. To address wide variation in single day testing data, the file also includes 7-day averages (means) for the number of people tested and the number of people who were positive.  These are calculated as the average of that day’s count and the previous 6 days.   

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| DATE | Date of specimen collection || 
| TOTAL_TESTS | Number of people who received a PCR test  | Day | 
| POSTITIVE_TESTS | Number of people with positive results| Day | 
| PERCENT_POSITIVE | Percentage of tests that are positive| Day | 
| TOTAL_TESTS_7DAYS_AVG | 7-day average of number of people who received a PCR test| Current day and previous 6 days| 
| POSITIVE_TESTS_7DAYS_AVG | 7-day average of number of people with positive results| Current day and previous 6 days| 
| INCOMPLETE | Used for display purposes only | N/A | 

Note that one person can have more than one test on different days. Therefore, the number of positive persons every day will be different from the epi curves at the top of the webpage as the epi curves will count people only on the first day they test positive.  

Additionally, the metric we are showing here reflects percent positivity by date of specimen collection (when someone went to their doctor for a test).   

### tests-by-zcta.csv   
This file contains the cumulative number of NYC residents who were tested for COVID-19 and the number of people tested who tested positive, by ZCTA of residence.   

The cumulative counts are as of the date of extraction from the NYC Health Department's disease surveillance database.   
 
This file is no longer being updated as of June 9, 2020. For data on testing by modified ZCTA, see data-by-modzcta.csv. 

***   

### Boro/ 
This folder contains borough-specific data. 

### Boro/boroughs-case-hosp-death.csv   
This file includes borough-specific daily counts of confirmed cases, hospitalizations, and deaths. Counts are aggregated separately by the following dates of interest: 
- Cases are by date of diagnosis   
- Hospitalizations are by date of admission    
- Deaths are by date of death   

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| DATE_OF_INTEREST| Date of diagnosis (cases), date of admission (hospitalizations), date of death (deaths)| |          
| BK_CASE_COUNT| Count of confirmed cases  in Brooklyn | Cumulative |     
| BK_HOSPITALIZED_COUNT | Count of hospitalized cases  in Brooklyn | Cumulative | 
| BK_DEATH_COUNT | Count of confirmed deaths in Brooklyn | Cumulative | 
| BX_CASE_COUNT| Count of confirmed cases  in the Bronx| Cumulative |     
| BX_HOSPITALIZED_COUNT | Count of hospitalized cases in the Bronx| Cumulative | 
| BX_DEATH_COUNT | Count of confirmed deaths  in the Bronx| Cumulative | 
| MN_CASE_COUNT| Count of confirmed cases  in Manhattan| Cumulative |     
| MN_HOSPITALIZED_COUNT | Count of hospitalized cases  in Manhattan | Cumulative | 
| MN_DEATH_COUNT | Count of confirmed deaths in Manhattan | Cumulative | 
| QN_CASE_COUNT| Count of confirmed cases  in Queens| Cumulative |     
| QN_HOSPITALIZED_COUNT | Count of hospitalized cases  in Queens | Cumulative | 
| QN_DEATH_COUNT | Count of confirmed deaths in Queens | Cumulative | 
| SI_CASE_COUNT| Count of confirmed cases  in Staten Island| Cumulative |     
| SI_HOSPITALIZED_COUNT | Count of hospitalized cases  in Staten Island| Cumulative | 
| SI_DEATH_COUNT | Count of confirmed deaths in Staten Island| Cumulative | 

Because of delays in reporting, the most recent data may be incomplete. Data shown currently will be updated in the future as new information on cases, hospitalizations, and deaths are reported.   

Note that sum of counts in this file may not match values in Citywide tables because of records with missing geographic information. This file does not contain information on probable deaths.    

### Boro/boroughs-by-age.csv   
This file includes borough-specific counts and rates of confirmed cases, hospitalizations, and deaths, by age group. Rates are:   
- Cumulative since the start of the outbreak   
- Per 100,000 people by age group   
 
Indicators include: 
| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| AGE_GROUP| Age group in years| |        
| BK_CASE_COUNT| Count of confirmed cases in Brooklyn | Cumulative |     
| BK_HOSPITALIZED_COUNT | Count of hospitalized cases in Brooklyn  | Cumulative | 
| BK_DEATH_COUNT | Count of confirmed deaths in Brooklyn  | Cumulative | 
| BK_CASE_RATE| Rate of confirmed cases in Brooklyn per 100,000 people by age group | Cumulative |     
| BK_HOSPITALIZED_RATE | Rate of hospitalized cases in Brooklyn per 100,000 people by age group | Cumulative |   
| BK_DEATH_RATE | Rate of confirmed deaths in Brooklyn per 100,000 people  by age group | Cumulative | 
| BX_CASE_COUNT| Count of confirmed cases in the Bronx| Cumulative |     
| BX_HOSPITALIZED_COUNT | Count of hospitalized cases in the Bronx  | Cumulative | 
| BX_DEATH_COUNT | Count of confirmed deaths in the Bronx | Cumulative | 
| BX_CASE_RATE| Rate of confirmed cases in the Bronx per 100,000 people by age group | Cumulative |     
| BX_HOSPITALIZED_RATE | Rate of hospitalized cases in the Bronx per 100,000 people by age group | Cumulative |   
| BX_DEATH_RATE | Rate of confirmed deaths in the Bronx per 100,000 people  by age group | Cumulative | 
| MN_CASE_COUNT| Count of confirmed cases in Manhattan| Cumulative |     
| MN_HOSPITALIZED_COUNT | Count of hospitalized cases in Manhattan | Cumulative | 
| MN_DEATH_COUNT | Count of confirmed deaths in Manhattan | Cumulative | 
| MN_CASE_RATE| Rate of confirmed cases in Manhattan per 100,000 people by age group | Cumulative |     
| MN_HOSPITALIZED_RATE | Rate of hospitalized cases in Manhattan per 100,000 people by age group | Cumulative |   
| MN_DEATH_RATE | Rate of confirmed deaths in Manhattan per 100,000 people  by age group | Cumulative | 
| QN_CASE_COUNT| Count of confirmed cases in Queens| Cumulative |     
| QN_HOSPITALIZED_COUNT | Count of hospitalized cases in Queens | Cumulative | 
| QN_DEATH_COUNT | Count of confirmed deaths in Queens | Cumulative | 
| QN_CASE_RATE| Rate of confirmed cases in Queens per 100,000 people by age group | Cumulative |     
| QN_HOSPITALIZED_RATE | Rate of hospitalized cases in Queens per 100,000 people by age group | Cumulative |   
| QN_DEATH_RATE | Rate of confirmed deaths in Queens per 100,000 people  by age group | Cumulative | 
| SI_CASE_COUNT| Count of confirmed cases in Staten Island| Cumulative |     
| SI_HOSPITALIZED_COUNT | Count of hospitalized cases in Staten Island | Cumulative | 
| SI_DEATH_COUNT | Count of confirmed deaths in Staten Island | Cumulative | 
| SI_CASE_RATE| Rate of confirmed cases in Staten Island per 100,000 people by age group | Cumulative |     
| SI_HOSPITALIZED_RATE | Rate of hospitalized cases in Staten Island per 100,000 people by age group | Cumulative |   
| SI_DEATH_RATE | Rate of confirmed deaths in Staten Island per 100,000 people  by age group | Cumulative | 

Note that sum of counts in this file may not match values in Citywide tables because of records with missing demographic or geographic information. This file does not contain information on probable deaths.    

### Boro/boroughs-by-race.csv   
This file includes borough-specific counts and rates of cases, hospitalizations, and deaths, by race/ethnicity group. Rates are:   
- Cumulative since the start of the outbreak   
- Per 100,000 people by borough of residence and race/ethnicity group   
- Age-adjusted according to [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf)  

Indicators include: 
| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| RACE_GROUP| Race/ethnicity group| |          
| BK_CASE_COUNT| Count of confirmed cases in Brooklyn | Cumulative |     
| BK_HOSPITALIZED_COUNT | Count of hospitalized cases in Brooklyn | Cumulative | 
| BK_DEATH_COUNT | Count of confirmed deaths in Brooklyn | Cumulative | 
| BK_CASE_RATE_ADJ | Age-adjusted rate of confirmed cases in Brooklyn per 100,000 people by race/ethnicity group | Cumulative |     
| BK_HOSPITALIZED_RATE_ADJ | Age-adjusted rate of hospitalized cases in Brooklyn per 100,000 people by race/ethnicity group | Cumulative |   
| BK_DEATH_RATE_ADJ | Age-adjusted rate of confirmed deaths in Brooklyn per 100,000 people by race/ethnicity group | Cumulative | 
| BX_CASE_COUNT| Count of confirmed cases in the Bronx| Cumulative |     
| BX_HOSPITALIZED_COUNT | Count of hospitalized cases in the Bronx | Cumulative | 
| BX_DEATH_COUNT | Count of confirmed deaths in the Bronx | Cumulative | 
| BX_CASE_RATE_ADJ | Age-adjusted rate of confirmed cases in the Bronx per 100,000 people by race/ethnicity group | Cumulative |     
| BX_HOSPITALIZED_RATE_ADJ | Age-adjusted rate of hospitalized cases in the Bronx per 100,000 people by race/ethnicity group | Cumulative |   
| BX_DEATH_RATE_ADJ | Age-adjusted rate of confirmed deaths in the Bronx per 100,000 people by race/ethnicity group | Cumulative | 
| MN_CASE_COUNT| Count of confirmed cases in Manhattan| Cumulative |     
| MN_HOSPITALIZED_COUNT | Count of hospitalized cases in Manhattan | Cumulative | 
| MN_DEATH_COUNT | Count of confirmed deaths in Manhattan | Cumulative | 
| MN_CASE_RATE_ADJ | Age-adjusted rate of confirmed cases in Manhattan per 100,000 people by race/ethnicity group | Cumulative |     
| MN_HOSPITALIZED_RATE_ADJ | Age-adjusted rate of hospitalized cases in Manhattan per 100,000 people by race/ethnicity group | Cumulative |   
| MN_DEATH_RATE_ADJ | Age-adjusted rate of confirmed deaths in Manhattan per 100,000 people by race/ethnicity group | Cumulative | 
| QN_CASE_COUNT| Count of confirmed cases in Queens| Cumulative |     
| QN_HOSPITALIZED_COUNT | Count of hospitalized cases in Queens | Cumulative | 
| QN_DEATH_COUNT | Count of confirmed deaths in Queens | Cumulative | 
| QN_CASE_RATE_ADJ | Age-adjusted rate of confirmed cases in Queens per 100,000 people by race/ethnicity group | Cumulative |     
| QN_HOSPITALIZED_RATE_ADJ | Age-adjusted rate of hospitalized cases in Queens  per 100,000 people by race/ethnicity group | Cumulative |   
| QN_DEATH_RATE_ADJ | Age-adjusted rate of confirmed deaths in Queens per 100,000 people by race/ethnicity group | Cumulative | 
| SI_CASE_COUNT| Count of confirmed cases in Staten Island| Cumulative |     
| SI_HOSPITALIZED_COUNT | Count of hospitalized cases in Staten Island | Cumulative | 
| SI_DEATH_COUNT | Count of confirmed deaths in Staten Island | Cumulative | 
| SI_CASE_RATE_ADJ | Age-adjusted rate of confirmed cases in Staten Island per 100,000 people by race/ethnicity group | Cumulative |     
| SI_HOSPITALIZED_RATE_ADJ | Age-adjusted rate of hospitalized cases in Staten Island per 100,000 people by race/ethnicity group | Cumulative |   
| SI_DEATH_RATE_ADJ | Age-adjusted rate of confirmed deaths in Staten Island per 100,000 people by race/ethnicity group | Cumulative | 

Data on people identified as American Indian/Alaska Native, two or more races, or certain other races/ethnicities not listed are not included in this table. The Hispanic/Latino category includes people of any race. Race/ethnicity information is most complete for people who have been hospitalized or have died. There are much less data currently available on race/ethnicity group for non-hospitalized cases.    

Note that sum of counts in this file may not match values in Citywide tables because of records with missing demographic or geographic information. This file does not contain information on probable deaths.    

### Boro/boroughs-by-sex.csv   
This file includes borough-specific counts and rates of confirmed cases, hospitalizations, and deaths, by sex as reported to the Health Department by laboratories. Rates are:   
- Cumulative since the start of the outbreak   
- Per 100,000 people by borough of residence and sex   

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| GROUP| Sex | |          
| BK_CASE_COUNT| Count of confirmed cases in Brooklyn | Cumulative |     
| BK_HOSPITALIZED_COUNT | Count of hospitalized cases in Brooklyn | Cumulative | 
| BK_DEATH_COUNT | Count of confirmed deaths in Brooklyn | Cumulative | 
| BK_CASE_RATE| Rate of confirmed cases per in Brooklyn 100,000 people by sex| Cumulative |     
| BK_HOSPITALIZED_RATE | Rate of hospitalized cases in Brooklyn per 100,000 people by sex | Cumulative |   
| BK_DEATH_RATE | Rate of confirmed deaths in Brooklyn per 100,000 people by sex | Cumulative | 
| BX_CASE_COUNT| Count of confirmed cases in the Bronx| Cumulative |     
| BX_HOSPITALIZED_COUNT | Count of hospitalized cases in the Bronx | Cumulative | 
| BX_DEATH_COUNT | Count of confirmed deaths in the Bronx | Cumulative | 
| BX_CASE_RATE| Rate of confirmed cases per in the Bronx 100,000 people by sex| Cumulative |     
| BX_HOSPITALIZED_RATE | Rate of hospitalized cases in the Bronx per 100,000 people by sex | Cumulative |   
| BX_DEATH_RATE | Rate of confirmed deaths in the Bronx per 100,000 people by sex | Cumulative | 
| MN_CASE_COUNT| Count of confirmed cases in Manhattan| Cumulative |     
| MN_HOSPITALIZED_COUNT | Count of hospitalized cases in Manhattan | Cumulative | 
| MN_DEATH_COUNT | Count of confirmed deaths in Manhattan | Cumulative | 
| MN_CASE_RATE| Rate of confirmed cases per in Manhattan 100,000 people by sex| Cumulative |     
| MN_HOSPITALIZED_RATE | Rate of hospitalized cases in Manhattan per 100,000 people by sex | Cumulative |   
| MN_DEATH_RATE | Rate of confirmed deaths in Manhattan per 100,000 people by sex | Cumulative | 
| QN_CASE_COUNT| Count of confirmed cases in Queens| Cumulative |     
| QN_HOSPITALIZED_COUNT | Count of hospitalized cases in Queens | Cumulative | 
| QN_DEATH_COUNT | Count of confirmed deaths in Queens | Cumulative | 
| QN_CASE_RATE| Rate of confirmed cases per in Queens 100,000 people by sex| Cumulative |     
| QN_HOSPITALIZED_RATE | Rate of hospitalized cases in Queens per 100,000 people by sex | Cumulative |   
| QN_DEATH_RATE | Rate of confirmed deaths in Queens per 100,000 people by sex | Cumulative | 
| SI_CASE_COUNT| Count of confirmed cases in Staten Island| Cumulative |     
| SI_HOSPITALIZED_COUNT | Count of hospitalized cases in Staten Island | Cumulative | 
| SI_DEATH_COUNT | Count of confirmed deaths in Staten Island | Cumulative | 
| SI_CASE_RATE| Rate of confirmed cases per in Staten Island 100,000 people by sex| Cumulative |     
| SI_HOSPITALIZED_RATE | Rate of hospitalized cases in Staten Island per 100,000 people by sex | Cumulative |   
| SI_DEATH_RATE | Rate of confirmed deaths in Staten Island per 100,000 people by sex | Cumulative | 

Due to the small number of cases among transgender and gender-nonconforming people, data on these cases are not included in this table at this time.   

Note that sum of counts in this file may not match values in Citywide tables because of records with missing demographic or geographic information. This file does not contain information on probable deaths.    

***   

### Deaths/ 
This folder contains data on COVID-19 deaths. 

### Deaths/deaths-by-boro-age.csv   
This file contains rates of death by age group and NYC borough of residence for confirmed deaths. This file does not contain information on probable deaths. Rates are:   
- Cumulative since the start of the outbreak   
- Per 100,000 people by age group and borough of residence  

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| BOROUGH| Borough | |          
| AGE_0_17_YRS | Rate of confirmed deaths among people aged 0-17 years per 100,000 people by borough | Cumulative | 
| AGE_18_44_YRS | Rate of confirmed deaths among people aged 18-44 years per 100,000 people by borough | Cumulative | 
| AGE_45_64_YRS | Rate of confirmed deaths among people aged 45-64 years per 100,000 people by borough | Cumulative | 
| AGE_65_74_YRS | Rate of confirmed deaths among people aged 65-74 years per 100,000 people by borough | Cumulative | 
| AGE_GE_75_YRS | Rate of confirmed deaths among people aged 75 years and older per 100,000 people by borough | Cumulative | 

### Deaths/deaths-by-race-age.csv   
This file contains rates of death by race/ethnicity group and age group for confirmed deaths. This file does not contain information on probable deaths. Rates are:   
- Cumulative since the start of the outbreak   
- Per 100,000 people by age group and race/ethnicity group  
 
Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| RACE_GROUP | Race/ethnicity group| |          
| AGE_0_17_YRS | Rate of confirmed deaths among people aged 0-17 years per 100,000 people by race/ethnicity| Cumulative | 
| AGE_18_44_YRS | Rate of confirmed deaths among people aged 18-44 years per 100,000 people by race/ethnicity | Cumulative | 
| AGE_45_64_YRS | Rate of confirmed deaths among people aged 45-64 years per 100,000 people by race/ethnicity | Cumulative | 
| AGE_65_74_YRS | Rate of confirmed deaths among people aged 65-74 years per 100,000 people by race/ethnicity | Cumulative | 
| AGE_GE_75_YRS | Rate of confirmed deaths among people aged 75 years and older per 100,000 people by race/ethnicity | Cumulative | 

Data on people identified as American Indian/Alaska Native, two or more races, or certain other races/ethnicities not listed are not included in this table. The Hispanic/Latino category includes people of any race. Race/ethnicity information is most complete for people who have been hospitalized or have died. There are much less data currently available on race/ethnicity group for non-hospitalized cases.    

### Deaths/deaths-by-underlying-condition.csv   
This file contains cumulative counts of confirmed deaths by age group, and counts of cases where underlying conditions were present, absent, or not known. Underlying conditions currently include diabetes, lung disease, cancer, immunodeficiency, heart disease, hypertension, asthma, kidney disease, gastrointestinal/liver disease, and obesity. “Pending” refers to cases that are still under investigation. This file does not contain information on probable deaths.  

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| AGE_GROUP | Age group in years | |          
| DEATH_COUNT_TOTAL | Count of confirmed deaths by age group| Cumulative | 
| DEATH_COUNT_ILLNESS | Count of confirmed deaths among people with underlying conditions by age group | Cumulative | 
| DEATH_COUNT_NO_ILLNESS | Count of confirmed deaths among people with no underlying conditions by age group | Cumulative | 
| DEATH_COUNT_PENDING_ILLNESS | Count of confirmed deaths among people under investigation for underlying illness by age group | Cumulative | 

### Deaths/probable-confirmed-by-boro.csv   
This file includes counts of confirmed and probable deaths, by NYC borough of residence. Data on probable deaths that are missing demographic information are classified as “Data pending.” Note that sum of counts in this file may not match Citywide values because of records with missing demographic information.   

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| BOROUGH| Borough | |          
| CONFIRMED_DEATH | Count of confirmed deaths by borough| Cumulative | 
| PROBABLE_DEATH | Count of probable deaths by borough| Cumulative | 


### Deaths/probable-confirmed-by-age.csv   
This file includes counts of confirmed and probable deaths, by age group. Data on probable deaths that are missing demographic information are classified as “Data pending.” Note that sum of counts in this file may not match Citywide values because of records with missing demographic information.  

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| AGE_GROUP | Age group in years | |          
| CONFIRMED_DEATH | Count of confirmed deaths by age group| Cumulative | 
| PROBABLE_DEATH | Count of probable deaths by age group | Cumulative | 


### Deaths/probable-confirmed-by-sex.csv   
This file includes counts of confirmed and probable deaths, by sex. Data on probable deaths that are missing demographic information are classified as “Data pending.” Note that sum of counts in this file may not match Citywide values because of records with missing demographic information.   

Due to the small number of cases among transgender and gender-nonconforming people, data on these cases are not included in this table at this time.   

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| SEX | Sex | |          
| CONFIRMED_DEATH | Count of confirmed deaths by sex| Cumulative | 
| PROBABLE_DEATH | Count of probable deaths by sex | Cumulative | 


### Deaths/probable-confirmed-by-race.csv   
This file includes counts of confirmed and probable deaths, by race/ethnicity group. Data on people identified as American Indian/Alaska Native, two or more races, or another race/ethnicity not listed are included in the “Other/Unknown” category. The Hispanic/Latino category includes people of any race.    

Data on probable deaths that are missing demographic information are classified as “Data pending.” Note that sum of counts in this file may not match Citywide values because of records with missing demographic information.   

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| RACE_GROUP | Race/ethnicity group | |          
| CONFIRMED_DEATH | Count of confirmed deaths by race/ethnicity group| Cumulative | 
| PROBABLE_DEATH | Count of probable deaths by race/ethnicity group | Cumulative | 

 
### Deaths/probable-confirmed-by-location.csv   
This file includes counts of confirmed and probable deaths, by location of death. The “Hospital/Emergency room” category includes any hospital-associated death, including deaths that occurred in the emergency department, an inpatient ward or intensive care unit. The “Nursing home/Hospice” includes any death that occurred in an assisted living or long-term care facility. The “Other/Unknown” category includes deaths that occurred in any setting not listed in this table, including patients who were dead on arrival or where information on location of death is unknown. Note that sum of counts in this file may not match Citywide values because of records with missing information.  

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| LOCATION_OF_DEATH | Location of death | |          
| CONFIRMED_DEATH | Count of confirmed deaths by location of death| Cumulative | 
| PROBABLE_DEATH | Count of probable deaths by location of death | Cumulative | 


### Deaths/probable-confirmed-dod.csv   
This file contains counts of people who died, by date of death, for both confirmed and probable COVID-19 deaths. This file includes deaths that occurred on or after March 11 are included (March 11 was the first date of death for a confirmed COVID-19 death).  This file also includes a display variable set at a fixed value for the most recent 7 days, to indicate the period in which data in the chart on the website are most likely to be incomplete due to reporting delays. 

Please refer to “Reporting on Deaths” section of Technical notes for definitions.  

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| DATE_OF_DEATH | Date of death | |          
| CONFIRMED_DEATH | Count of confirmed deaths by date of death| Cumulative | 
| PROBABLE_DEATH | Count of probable deaths by date of death | Cumulative | 

Because of delays in reporting, the most recent data may be incomplete. Data shown currently will be updated in the future as data on deaths are reported or updated.  

*** 

### Geography-resources/ 
This folder contains additional resources for data provided by MODZCTA (modified ZIP code tabulation area) - geographic files for modified ZIP Code Tabulation Area geographies (MODZCTA). For details please visit its [Readme](https://github.com/nychealth/coronavirus-data/blob/master/Geography-resources/README.md). 

***   

### testing/ 
This folder contains data on antibody tests, which are also referred to as serology tests because they are performed on a blood sample. Reported antibody tests are de-duplicated such that there is one record per person, per week.  

Antibody testing started to become more widely available in NYC in April 2020. Cumulative data include all serology tests reported to the Health Department after March 3, 2020, and data reported by week include tests reported starting on April 5, 2020. 

### testing/antibody-by-week.csv   
This file contains person-level information on antibody tests, by week, as reported to the Health Department by laboratories. 

Antibody tests are categorized based on the date of specimen collection, and are aggregated by full-weeks starting each Sunday and ending on Saturday. For example, a person whose blood was collected for antibody testing on Wednesday, May 6 would be categorized as tested during the week ending May 9. A person tested twice in one week would only be counted once in that week. 

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| WEEKDATE| Week-ending date | |     
| NUM_PEOP_TEST | Count of people tested with an antibody test by week  | Cumulative from April 5, 2020 |      
| NUM_PEOP_POS | Count of people with a positive result on an antibody test by week | Cumulative from April 5, 2020 |   
| PERCENT_POSITIVE | Percentage of people with a positive result on an antibody test by week | Cumulative from April 5, 2020 |   
| INCOMPLETE | Used for display purposes only | N/A |  

Note that one person can have more than one serology test during different weeks. Therefore, the sum of counts across weeks may not match summary values. People are considered positive if they ever receive a positive antibody result, regardless of whether they have received negative results as well. 

### testing/antibody-by-modzcta.csv   
This file contains person-level information on antibody tests by modified ZIP code tabulation areas (ZCTA). This unit of geography is similar to ZIP codes but combines census blocks with smaller populations to allow more stable estimates of population size. Please see a description of modified ZCTAs in the technical notes section (Geography: Zip codes and ZCTAs). Modified ZCTAs reflect the first non-missing address within NYC for each person reported with an antibody test result.  

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| MODZCTA_FIRST| Modified ZIP code tabulation areas (ZCTA) | |     
| NUM_PEOP_TEST | Number of people tested with an antibody test by modified ZCTA  | Cumulative |      
| NUM_PEOP_POS | Number of people with a positive result on an antibody test by modified ZCTA  | Cumulative |   
| PERCENT_POSITIVE | Percentage of people ever tested for COVID-19 with an antibody test who tested positive by modified ZCTA  | Cumulative |   
| TEST_RATE | Rate of antibody testing per 100,000 people by modified ZCTA  | Cumulative |   

Note that the sum of counts may not match summary values because of records with missing geographic information. People are considered positive if they ever receive a positive antibody result, regardless of whether they have received negative results as well. 

### testing/antibody-by-age.csv   
This file contains person-level information on antibody tests, by age group, as reported to the Health Department by laboratories. Age is calculated from each person’s date of birth to the date of their first reported antibody test.  

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| DEMO_VARIABLE| Age group in years | |     
| NUM_PEOP_TEST | Count of people tested with an antibody test by age group  | Cumulative |      
| NUM_PEOP_POS | Count of people with a positive result on an antibody test by age group | Cumulative |   
| PERCENT_POSITIVE | Percentage of people ever tested for COVID-19 with an antibody test who tested positive by age group  | Cumulative |   
| TEST_RATE | Rate of antibody testing per 100,000 people by age group | Cumulative | 

The sum of counts may not match summary values because of records with missing demographic information. People in each category are counted once and are considered positive if they ever receive a positive antibody result, regardless of whether they have received negative results as well. 

### testing/antibody-by-boro.csv   
This file contains person-level information on antibody tests, by NYC borough of residence, as reported to the Health Department by laboratories. Borough reflects the first non-missing address within NYC for each person reported with an antibody test result.  

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| DEMO_VARIABLE| Borough of residence | |     
| NUM_PEOP_TEST | Count of people tested with an antibody test by borough  | Cumulative |      
| NUM_PEOP_POS | Count of people with a positive result on an antibody test by borough | Cumulative |   
| PERCENT_POSITIVE | Percentage of people ever tested for COVID-19 with an antibody test who tested positive by borough | Cumulative |   
| TEST_RATE | Rate of antibody testing per 100,000 people by borough | Cumulative | 

The sum of counts may not match summary values because of records with missing geographic information. People in each category are counted once and are considered positive if they ever receive a positive antibody result, regardless of whether they have received negative results as well. 

### testing/antibody-by-poverty.csv   
This file contains person-level information on antibody tests, by ZCTA-level neighborhood poverty group in NYC (low, medium, high, very high). Methods for determining neighborhood poverty are outlined in technical notes above (Poverty Groups). The ZCTAs used for classification reflect the first non-missing address within NYC for each person reported with an antibody test result.  

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| DEMO_VARIABLE| ZCTA-level neighborhood poverty group | |     
| NUM_PEOP_TEST | Count of people tested with an antibody test by neighborhood poverty group  | Cumulative |      
| NUM_PEOP_POS | Count of people with a positive result on an antibody test by neighborhood poverty group | Cumulative |   
| PERCENT_POSITIVE | Percentage of people ever tested for COVID-19 with an antibody test who tested positive by neighborhood poverty group | Cumulative |   
| TEST_RATE | Rate of antibody testing per 100,000 people by neighborhood poverty group | Cumulative | 

The sum of counts may not match summary values because of records with missing geographic information. People in each category are counted once and are considered positive if they ever receive a positive antibody result, regardless of whether they have received negative results as well. 

### testing/antibody-by-sex.csv   
This file contains person-level information on antibody tests, by sex, as reported to the Health Department by laboratories.  

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| DEMO_VARIABLE| Sex | |     
| NUM_PEOP_TEST | Count of people tested with an antibody test by sex  | Cumulative |      
| NUM_PEOP_POS | Count of people with a positive result on an antibody test by sex   | Cumulative |   
| PERCENT_POSITIVE | Percentage of people ever tested for COVID-19 with an antibody test who tested positive by sex   | Cumulative |   
| TEST_RATE | Rate of antibody testing per 100,000 people by sex   | Cumulative | 

The sum of counts may not match summary values because of records with missing demographic information. People in each category are counted once and are considered positive if they ever receive a positive antibody result, regardless of whether they have received negative results as well. 

***   

### recent/ 
This folder contains data from the most recent 4-week period, with a one-week lag. We update these files on Thursdays, with data through the previous Saturday. 

### recent/recent-4-week-citywide.csv  
This file contains counts of confirmed cases and deaths. This file does not contain information on probable deaths. Counts are aggregated separately by week and the following dates of interest:  
- Cases are by date of diagnosis   
- Deaths are by date of death   

Confirmed cases and deaths are aggregated by full-weeks starting each Sunday and ending on Saturday. Because of delays in reporting, all data are lagged to include the most recent complete week (week 1), and the three prior most recent weeks. For example, in the weekly update that occurred on Thursday, July 23, weeks 1-4 represent the following dates of interest:   
- Week 1: July 13-18 
- Week 2: July 5-12 
- Week 3: June 28 – July 4 
- Week 4: June 21-27 

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| Most recent (week 1) | Summary count of confirmed cases and  confirmed deaths| Most recent complete week |    
| WEEK 2 | Summary count of confirmed cases and  confirmed deaths | Week 2 |    
| WEEK 3 | Summary count of confirmed cases and  confirmed deaths | Week 3 |    
| WEEK 3 | Summary count of confirmed cases and  confirmed deaths | Week 4 |    


### recent/recent-4-week-by-modzcta.csv    
This file contains data by modified ZIP code tabulation areas (ZCTA). This unit of geography is similar to ZIP codes but combines census blocks with smaller populations to allow more stable estimates of population size for rate calculation.  Please see description of modified ZCTAs in the technical notes section (Geography: Zip codes and ZCTAs).   

This file contains indicators over the most recent 4 weeks (with a 1-week lag to account for reporting delays) that are aggregated by modified ZCTA and the following dates of interest:   
- Cases are by date of diagnosis   
- Deaths are by date of death   

Confirmed cases and deaths are aggregated by full-weeks starting each Sunday. Because of delays in reporting, all data are lagged to include the most recent complete week (week 1), and the four prior most recent weeks. For example, in the weekly update that occurred on Thursday, July 23, weeks 1-4 represent the following dates of interest:   
- Week 1: July 13-18 
- Week 2: July 5-12 
- Week 3: June 28 – July 4 
- Week 4: June 21-27 

Indicators include: 

| Variable Name | Definition | Timeframe | 
| -------------------|-----------------------------------------------------------------------|-----------:| 
| MODIFIED_ZCTA | Modified ZIP code tabulation areas (ZCTA) | |          
| NEIGHBORHOOD_NAME | Neighborhood names represent the [Neighborhood Organizing Census Committee](https://www1.nyc.gov/site/census/index.page) boundaries, which were recently developed by the U.S. Census Bureau with input from community groups | |   
| COVID_CASE_COUNT_WEEK*X* | Count of confirmed cases by week. *X* indicates the corresponding week number | Repeated for weeks 1-4 |    
| COVID_CASE_COUNT_4WEEK | Summary count of confirmed cases | Cumulative across weeks 1-4 |    
| COVID_CASE_RATE_ WEEK*X* | Rate of confirmed cases per 100,000 people by modified ZCTA *X* indicates the corresponding week number | Repeated for weeks 1-4 |    
| COVID_CASE_RATE_4WEEK | Rate of confirmed cases per 100,000 people by modified ZCTA | Cumulative across weeks 1-4 |    
| PCTCHANGE_2WEEK | Percent change in the count of confirmed cases, comparing the last 2 weeks of the 4 week period to the first 2 weeks (week 3 + week 4)/ (week 1 + week 2))*100. | Cumulative across weeks 1-4 | 
| COVID_DEATH_COUNT_4WEEK | Count of confirmed deaths  | Cumulative across weeks 1-4 |    
| COVID_DEATH_RATE_4WEEK | Rate of confirmed deaths per 100,000 people by modified ZCTA | Cumulative across weeks 1-4 |    
| NUM_PEOP_TEST_4WEEK | Number of people who recieved a polymerase chain reaction (PCR) test | Cumulative across weeks 1-4 |    
| TESTING_RATE_4WEEK | Rate of people getting a PCR test per 100,000 people by modified ZCTA | Cumulative across weeks 1-4 |    
| PERCENT_POSITIVE_4WEEK | Percent of all people tested with a PCR test who were positive | Cumulative across weeks 1-4 |    

