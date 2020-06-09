# NYC Coronavirus Disease 2019 (COVID-19) Data  
This repository contains data on Coronavirus Disease 2019 (COVID-19) in New York City, updated daily. You can view visualizations of these data on the [Health Department’s COVID-19 Data webpage](https://www1.nyc.gov/site/doh/covid/covid-19-data.page). Some other data are available via [NYC Open Data](https://data.cityofnewyork.us/browse?category=Health&q=covid).

Data are preliminary and subject to change. Information on this page will change as data and documentation are updated.  
 
The Health Department classifies the start of the outbreak in NYC as the date of the first laboratory-confirmed case, February 29, 2020.  
 
***  
 
## Types of Surveillance  
The Health Department conducts two main types of surveillance for COVID-19:   
- Syndromic surveillance  
- Reportable disease surveillance  
 
### Syndromic Surveillance  
We receive data from all 53 hospital emergency departments (EDs) in NYC about the types of illnesses people experience on a regular basis. This surveillance allows the Health Department to evaluate care-seeking trends at hospitals for influenza-like illness and pneumonia.   
 
The information on each patient is evaluated for descriptions that resemble influenza -like illness or pneumonia. Influenza -like illness is defined as mention of either:  
- Fever and cough    
- Fever and sore throat  
- Fever and shortness of breath or difficulty breathing
- Influenza  
 
Pneumonia is defined as mention of or diagnosis of pneumonia. Since the signs and symptoms of COVID-19 overlap with these categories that the Health Department tracks routinely, we are able to identify unusual spikes in people seeking care at hospitals. We are using this as a proxy measure to observe COVID-19-like disease in the population.  
*Strengths*:  The data show real-time, population-level trends of people seeking health care for COVID-like disease.  
*Limitations*: The data do not represent patients with laboratory-confirmed COVID-19.  
 
### Reportable Disease Surveillance  
The Health Department receives electronic laboratory reports for a number of infectious diseases, including COVID-19, as required by law in the [NYC Health Code](https://www1.nyc.gov/site/doh/providers/reporting-and-services/notifiable-diseases-and-conditions-reporting-central.page). When a specimen is collected from a patient for laboratory testing for the virus that causes COVID-19, the laboratory must report all results, whether positive, negative, or inconclusive, to the Health Department. Demographic information on the person being tested is reported to the Health Department, including name, address, and date of birth.  
*Strengths*: This standard reporting system allows for rapid and detailed information to be transmitted routinely to the Health Department.    
*Limitations*: 
- Because of delays in reporting, the most recent data may be incomplete. Current data will be updated in the future as information on cases, hospitalizations, and deaths are reported to the Health Department.  
- Additionally, the Health Department is currently advising people with mild to moderate symptoms to stay at home and not seek testing. Many cases in the community, without laboratory testing, will not be included in these counts because they have never had a positive laboratory test.   
- These data are also limited by testing supply capacity, including the materials required for testing.   
- Information on reported deaths can be limited by delays in reporting by hospitals or funeral homes.   
 
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
Note that hospitalization information is missing from a number of facilities, which is a limitation for any analysis considering hospitalization status by geography (e.g., borough).  
 
### Reporting on COVID-19 Deaths 
COVID-19 deaths are reported from March 11, 2020 as this was the first date of death for a patient with confirmed COVID-19.  
 
There are two classifications of COVID-19 deaths reported:  
- A death is classified as **confirmed** if the decedent was an NYC resident who had a positive laboratory test for the virus that causes COVID-19.  
- A death is classified as **probable** if the decedent was an NYC resident (or residency pending) who had no known positive laboratory test for the virus that causes COVID-19 but the death certificate lists “COVID-19” or an equivalent as a cause of death.  
 
As new information becomes available, some deaths previously classified as probable may be reclassified as confirmed.  
 
Differences between death counts between NYC and New York State:  
 
Data on deaths reported by NYC are derived from the Health Department’s surveillance database and will be different from data reported by the New York State Department of Health. The State Department of Health reports data on deaths from:  
- The State Hospital Emergency Response Data System  
- Daily calls to hospitals and other facilities that are caring for patients, such as nursing homes  
 
The NYC Health Department reports data on deaths that reflect both:  
- Positive tests for COVID-19 confirmed by laboratories  
- Confirmations of a person’s death from the City’s Office of the Chief Medical Examiner and our Bureau of Vital Statistics, which is responsible for the registration, analysis and reporting of all deaths in NYC  
 
Due to the time required by the Health Department to confirm that a death was due to COVID-19, the City’s reported total for any given day is usually lower than the State’s number.  
 
### Race and Ethnicity 
Race and ethnicity information is often missing  in reportable disease surveillance. Information on race/ethnicity typically comes from electronic laboratory reports and unfortunately, race/ethnicity data is often missing in laboratory reports. For the COVID-19 response, the Health Department has electronically imported aggregated data from partners such as hospitals, hospital systems, or Regional Health Information Organizations to improve the completeness of race/ethnicity data for hospitalized people. However, health records may also be missing the race/ethnicity information. Additionally, the Health Department is working to import race/ethnicity information for people who have died. However, this information is often incomplete or not immediately available because it can take a few days for the information to be entered into the electronic death registration system. Race/ethnicity information is typically collected by funeral directors from next of kin of the decedent.  
 
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
 
Note that sum of counts in this file may not match values in Citywide tables because of records with missing geographic information. This file does not currently contain information on probable deaths. 
 
### by-age.csv  
This file contains counts and rates of confirmed cases, hospitalizations, and deaths, by age group. Rates are:  
- Cumulative since the start of the outbreak  
- Per 100,000 people by age group  
 
Note that sum of counts in this file may not match Citywide values because of records with missing demographic information. This file does not currently contain information on probable deaths.  
 
### by-sex.csv  
This file contains counts and rates of confirmed cases, hospitalizations, and deaths, by sex as reported to the Health Department by laboratories. Rates are:  
- Cumulative since the start of the outbreak  
- Per 100,000 people by sex  
 
Due to the small number of cases among transgender and gender-nonconforming people, data on these cases are not included in this table at this time.  
 
Note that sum of counts in this file may not match Citywide values because of records with missing demographic information. This file does not currently contain information on probable deaths.  
 
### by-poverty.csv  
This file contains counts and rates of confirmed cases, hospitalizations, and deaths, by ZCTA-level neighborhood poverty group in NYC (low, medium, high, very high). Methods for determining neighborhood poverty are outlined in technical notes above (Poverty Groups). Rates are:   
- Cumulative since the start of the outbreak  
- Age-adjusted according to [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf)  
- Per 100,000 people by ZCTA of residence     
 
Note that sum of counts in this file may not match Citywide values because of records with missing geographic information. This file does not currently contain information on probable deaths.    
 
### by-race.csv  
This file contains counts and rates of confirmed cases, hospitalizations, and deaths by race/ethnicity group. Rates are:  
- Cumulative since the start of the outbreak  
- Age-adjusted according to [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf) 
- Per 100,000 people by race/ethnicity group  
 
Data on people identified as American Indian/Alaska Native, two or more races, or other races/ethnicities not listed are not included in this table, as precise race-specific population estimates are not available for these groups in NYC. The Hispanic/Latino category includes people of any race. Race/ethnicity information is most complete for people who have been hospitalized or have died. There are much less data currently available on race/ethnicity group for non-hospitalized cases.   
Note that sum of counts in this file may not match Citywide values because of records with missing demographic information. This file does not currently contain information on probable deaths.    
 
### case-hosp-death.csv  
This file contains daily counts of confirmed cases, hospitalizations, and deaths. This file does not currently contain information on probable deaths. Counts are aggregated separately by the following dates of interest: 
- Cases are by date of diagnosis  
- Hospitalizations are by date of admission   
- Deaths are by date of death  
 
Because of delays in reporting, the most recent data may be incomplete. Data shown currently will be updated in the future as new information on cases, hospitalizations, and deaths are reported.  
 
### data-by-modzcta.csv  
This file contains data by modified ZIP code tabulation areas (ZCTA). This unit of geography is similar to ZIP codes but combines census blocks with smaller populations to allow more stable estimates of population size for rate calculation.  Please see description of modified ZCTAs in the technical notes section (Geography: Zip codes and ZCTAs).  
 
This file contains the following cumulative indicators by modified ZCTA:  
- Count of confirmed cases  
- Rate of confirmed cases per 100,000 people by ZCTA 
- Population denominators for ZCTAs derived from intercensal estimates by the Bureau of Epidemiology Services (see “Rates per 100,000 people” for more details)  
- Count of confirmed deaths  
- Rate of confirmed deaths per 100,000 people by ZCTA 
- Percentage of people ever tested for COVID-19 with a polymerase chain reaction (PCR) test who tested positive
- Count of people tested for COVID-19 with a PCR test
 
This file includes the corresponding neighborhood and borough for each modified ZCTA. 
- Modified ZCTA 
- Neighborhood name  
- Borough name  
 
Neighborhood names represent the [Neighborhood Organizing Census Committee](https://www1.nyc.gov/site/census/index.page) boundaries, which were recently developed by the U.S. Census Bureau with input from community groups. 
 
Note that sum of counts in this file may not match values in Citywide tables because of records with missing geographic information. This file does not currently contain information on probable deaths.   
 
### summary.csv  
This file contains summary information, including the cut-off date and time for data included in this update, and cumulative counts of cases, hospitalizations, and deaths.    
 
Hospitalization counts reflect the total number of people with COVID-19 ever admitted to a hospital, not the number of people currently admitted. Death counts reflect both confirmed and probable deaths, separately. 
 
### syndromic-data.csv  
This file includes the rate of visits to NYC emergency departments (ED) per 100,000 people, and rates of subsequent admissions to the hospital through the ED, for influenza-like illness or pneumonia, by date of visit for all ages and by age group (0-17, 18-44, 45-64, 65-74, 75+ years), since February 1, 2020 based on the Health Department’s syndromic surveillance system.  
  
### tests.csv  
This file contains the number of polymerase chain reaction (PCR) tests administered by person by day, the number of people with positive results by day, and the percent of all people tested who were positive by day. To address wide variation in single-day testing data, the file also includes a 3-day percent positive value, calculated as the percent all people tested who were positive in the 3-day period leading up to each day. 
 
Note that one person can have more than one test on different days. Therefore, the number of positive persons every day will be different from the epi curves at the top of the webpage as the epi curves will count people only on the first day they test positive. 
 
Additionally, the metric we are showing here reflects percent positivity by date of specimen collection (when someone went to their doctor for at test). The metric shown on the [milestone webpage](https://www1.nyc.gov/site/doh/covid/covid-19-goals.page) shows citywide percent positivity by the date that the lab result was reported, which is slightly different. Therefore the two metrics will not be the same for each daily value but show the same patterns. 
 
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
 
Because of delays in reporting, the most recent data may be incomplete. Data shown currently will be updated in the future as new information on cases, hospitalizations, and deaths are reported.  
 
Note that sum of counts in this file may not match values in Citywide tables because of records with missing geographic information. This file does not currently contain information on probable deaths.   
 
### Boro/boroughs-by-age.csv  
This file includes borough-specific counts and rates of confirmed cases, hospitalizations, and deaths, by age group. Rates are:  
- Cumulative since the start of the outbreak  
- Per 100,000 people by age group  
 
Note that sum of counts in this file may not match values in Citywide tables because of records with missing demographic or geographic information. This file does not currently contain information on probable deaths.   
 
### Boro/boroughs-by-race.csv  
This file includes borough-specific counts and rates of cases, hospitalizations, and deaths, by race/ethnicity group. Rates are:  
- Cumulative since the start of the outbreak  
- Per 100,000 people by borough of residence and race/ethnicity group  
- Age-adjusted according to [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf) 
 
Data on people identified as American Indian/Alaska Native, two or more races, or certain other races/ethnicities not listed are not included in this table, as precise race-specific population estimates are not available for these groups in NYC. The Hispanic/Latino category includes people of any race. Race/ethnicity information is most complete for people who have been hospitalized or have died. There are much less data currently available on race/ethnicity group for non-hospitalized cases.   
 
Note that sum of counts in this file may not match values in Citywide tables because of records with missing demographic or geographic information. This file does not currently contain information on probable deaths.   
 
### Boro/boroughs-by-sex.csv  
This file includes borough-specific counts and rates of confirmed cases, hospitalizations, and deaths, by sex. Rates are:  
- Cumulative since the start of the outbreak  
- Per 100,000 people by borough of residence and sex  
 
Due to the small number of cases among transgender and gender-nonconforming people, data on these cases are not included in this table at this time.  
 
Note that sum of counts in this file may not match values in Citywide tables because of records with missing demographic or geographic information. This file does not currently contain information on probable deaths.   

***  
  
### Deaths/
This folder contains data on COVID-19 deaths.
 
### Deaths/deaths-by-boro-age.csv  
This file contains rates of death by age group and NYC borough of residence for confirmed deaths. This file does not currently contain information on probable deaths. Rates are:  
- Cumulative since the start of the outbreak  
- Per 100,000 people by age group and borough of residence 
 
### Deaths/deaths-by-race-age.csv  
This file contains rates of death by race/ethnicity group and age group for confirmed deaths. This file does not currently contain information on probable deaths. Rates are:  
- Cumulative since the start of the outbreak  
- Per 100,000 people by age group and race/ethnicity group 
 
Data on people identified as American Indian/Alaska Native, two or more races, or certain other races/ethnicities not listed are not included in this table, as precise race-specific population estimates are not available for these groups in NYC. The Hispanic/Latino category includes people of any race. Race/ethnicity information is most complete for people who have been hospitalized or have died. There are much less data currently available on race/ethnicity group for non-hospitalized cases.   
 
### Deaths/deaths-by-underlying-condition.csv  
This file contains cumulative counts of confirmed deaths by age group, and counts of cases where underlying conditions were present, absent, or not known. Underlying conditions currently include diabetes, lung disease, cancer, immunodeficiency, heart disease, hypertension, asthma, kidney disease, gastrointestinal/liver disease, and obesity. “Pending” refers to cases that are still under investigation. This file does not currently contain information on probable deaths. 
 
### Deaths/probable-confirmed-by-age.csv  
This file includes counts of confirmed and probable deaths, by age group. Data on probable deaths that are missing demographic information are classified as “Data pending.” Note that sum of counts in this file may not match Citywide values because of records with missing demographic information.  
 
### Deaths/probable-confirmed-by-sex.csv  
This file includes counts of confirmed and probable deaths, by sex. Data on probable deaths  that are missing demographic information are classified as “Data pending.” Note that sum of counts in this file may not match Citywide values because of records with missing demographic information.  
Due to the small number of cases among transgender and gender-nonconforming people, data on these cases are not included in this table at this time.  
 
### Deaths/probable-confirmed-by-race.csv  
This file includes counts of confirmed and probable deaths, by race/ethnicity group. Data on people identified as American Indian/Alaska Native, two or more races, or another race/ethnicity not listed are included in the “Other/Unknown” category. The Hispanic/Latino category includes people of any race.   
 
Data on probable deaths  that are missing demographic information are classified as “Data pending.” Note that sum of counts in this file may not match Citywide values because of records with missing demographic information.  
 
### Deaths/probable-confirmed-by-location.csv  
This file includes counts of confirmed and probable deaths, by location of death. The “Hospital/Emergency room” category includes any hospital-associated death, including deaths that occurred in the emergency department, an inpatient ward or intensive care unit. The “Nursing home/Hospice” includes any death that occurred in an assisted living or long-term care facility. The “Other/Unknown” category includes deaths that occurred  in any setting not listed in this table, including patients who were dead on arrival or where information on location of death is unknown. Note that sum of counts in this file may not match Citywide values because of records with missing information. 
 
### Deaths/probable-confirmed-dod.csv  
This file contains counts of people who died, by date of death, for both confirmed and probable COVID-19 deaths. This file includes deaths that occurred on or after March 11 are included (March 11 was the first date of death for a confirmed COVID-19 death). Please refer to “Reporting on Deaths” section of Technical notes for definitions. 
 
Because of delays in reporting, the most recent data may be incomplete. Data shown currently will be updated in the future as data on deaths are reported or updated. 

***

### Geography-resources/
This folder contains additional resources for data provided by MODZCTA (modified ZIP code tabulation area) - geographic files for modified ZIP Code Tabulation Area geographies (MODZCTA). For details please visit its [Readme](https://github.com/nychealth/coronavirus-data/blob/master/Geography-resources/README.md).
