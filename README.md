# NYC Coronavirus Disease 2019 (COVID-19) Data   

This repository contains data on Coronavirus Disease 2019 (COVID-19) in New York City (NYC). The Health Department classifies the start of the COVID-19 outbreak in NYC as the date of the first laboratory-confirmed case, February 29, 2020.  

You can view visualizations of these data on the [Health Department’s COVID-19 Data webpage](https://www1.nyc.gov/site/doh/covid/covid-19-data.page). Additional data related to COVID-19 are available via [NYC Open Data](https://data.cityofnewyork.us/browse?category=Health&q=covid). 

Data are preliminary and subject to change. Information on this page will change as data and documentation are updated. Tables are updated either weekly on Thursday (at a 3-day lag or with data through the previous Saturday) or monthly (at a 14-day lag).

***

This Readme includes:
- How to use this repository
- Important changes (by date)
- Key Technical notes
- Contents

***

## How to use this repository
This repository contains CSV (comma separated values) files of data, and Readme files with important documentation of the data. If you are unfamiliar with Github, you may find these instructions helpful:

**To download data**, scroll up to the green button labelled "Code." Clicking this button will start a download of a ZIP file of the entire contents of this repository.

Alternatively, you can download a single file. Click on a file you would like to download. Next, click the "Raw" button. Right click and save as a CSV file. 

**For help understanding a file**, you can consult the documentation we have provided in the Readme files for each folder of data. To find  Readme files, just click on a folder name, above, and scroll down. Documentation is organized by file name, so you can scroll through the Readme, find the name of the file you are using for, and read documentation on it. Additionally, some universal documentation is provided in the [Key Technical Notes](https://github.com/nychealth/coronavirus-data/blob/master/README.md#key-technical-notes). 

**Questions and custom requests**: We will try to answer questions about the data in this repository as we are able to. If you have a question, please search the [Issues](https://github.com/nychealth/coronavirus-data/issues?q=) to see if it’s already been addressed. Please understand that we are responding to a pandemic and we might not be able to address all questions in a timely manner.  We are not able to accommodate custom data requests placed via Github.  

***
## Update on May 11, 2023

The Health Department made several changes to this repository and the [COVID-19 Data webpage](https://www1.nyc.gov/site/doh/covid/covid-19-data.page) on May 11, 2023. These include:
* We are applying a revised the COVID-19 death definition and COVID-19 deaths will no longer be classified as confirmed or probable. Deaths from April 3, 2023, will be counted as a COVID-19 death if: 
  - the death certificate lists COVID-19 or an equivalent term as the underlying or a contributing cause of death, or 
  - a case investigation for a confirmed, probable, or suspect COVID-19 case determined that COVID-19 was the cause of death or contributed to the death.
* In line with the death definition change change, total deaths will be presented instead of confirmed and probable deaths in all graphs and tables. 
* We have revised the tables for weekly hospitalization and death rates by age and race/ethnicity to correctly categorize people with COVID-19 based on date of event (hospital admission or death). These files previously categorized people with COVID-19 based on date of COVID-19 diagnosis. Trends using the updated data remain the same. 

## Update on April 3, 2023

Starting the week of April 3, 2023, the Health Department will update data in this repository and on the [COVID-19 Data webpage](https://www1.nyc.gov/site/doh/covid/covid-19-data.page) weekly on Thursdays. 

## Update on October 28, 2022

The Health Department uploaded historical probable deaths among NYC residents recently reported from other jurisdictions. These were cases where COVID was listed on the death certificate but without a corresponding positive lab and took place in 2020, 2021, and early 2022.  

## Update on September 14, 2021
- Antibody-by-age, -by-boro, -by-poverty, and -by-sex data are now found in antibody-by-group.csv. The other files will no longer be updated.
- by-age, by-boro, by-poverty, by-race, and by-sex will no longer be updated. Those data are now found in by-group.csv.
- deaths-by-boro-age, deaths-by-underlying-conditions, and probable-confirmed-by-age, -by-location, -by-boro, -by-race, and -by-sex are no longer updated. 

## Important: Update on August 11, 2021

As indicated in commit notes from 8/11, there were technical issues with our data processing on 8/9 and 8/10. While these issues were being fixed, data updates were paused for those days. Data updated on 8/11 include backfill for days with no updates. Differences in counts in cumulative files from 8/8 to 8/11 reflect events that have happened over a broad recent time period and should not be interpreted as events that have happened since the previous update. As always, data are preliminary and subject to change, and dates are backfilled as additional data come in.

## Important: Update on August 2, 2021

The Health Department made several changes to this repository and the [COVID-19 Data webpage](https://www1.nyc.gov/site/doh/covid/covid-19-data.page) on August 2, 2021. These include:
* Adding weekly case, hospitalization, and death rate files by race/ethnicity, and age.
* Adding 7-day Transmission Rates for Citywide, Borough, and UHF42 neighborhoods
* Revising case, hospitalization, and death rates to reflect both confirmed and probable cases

## Important: Update on June 10, 2021

The Health Department made several changes to this repository and the [COVID-19 Data webpage](https://www1.nyc.gov/site/doh/covid/covid-19-data.page) on June 10, 2021. These include:

* Adding data on SARS-CoV-2 variants, including the number and type of variants identified in NYC over time
  * Please see the technical notes for a description of SARS-CoV-2 variants and genomic sequencing in NYC
  * Data on SARS-CoV-2 variants will be updated weekly on Thursday (with data through the previous Saturday)

## Important: Update on March 24, 2021

As indicated in commit notes from 3/19 and 3/20, there were technical issues in the data transmission from New York State to New York City. This resulted in counts that were lower than expected for several days. While this transmission error was being fixed, data updates were paused for 3/21, 3/22, and 3/23. Data updated on 3/24 include backfill for days with low counts and days with no updates. Differences in counts in cumulative files from 3/20 to 3/24 reflect events that have happened over a broad recent time period and should not be interpreted as events that have happened since the previous update. As always, data are preliminary and subject to change, and dates are backfilled as additional data come in.

***

## Important: Changes on March 3, 2021

The Health Department made several changes to this repository and the [COVID-19 Data webpage](https://www1.nyc.gov/site/doh/covid/covid-19-data.page) on March 3, 2021. These include:

* Adding rates of hospitalizations and confirmed deaths by modified ZIP code tabulation areas 
  * Case rates will be calculated for the most recent 28-days on a 14-day lag, and updated daily

* Adding trends in rates of hospitalizations and confirmed deaths by multiple geographies
  * Case rates will be calculated for each month on a 14-day lag, and updated monthly
  
***

## Important: Changes on December 7, 2020

The Health Department made several changes to this repository and the [COVID-19 Data webpage](https://www1.nyc.gov/site/doh/covid/covid-19-data.page) on December 7, 2020. These include:

* Changing the naming convention for the main categories of COVID-19 tests
  * Data referenced in this repository as "molecular tests" correspond to data previously labeled as "PCR tests." Please see the technical notes for a description of the different [types of COVID-19 laboratory tests](https://github.com/nychealth/coronavirus-data#laboratory-testing)
  
* Including probable COVID-19 cases into summary data and epi curves
  * Please see the technical notes for a description of the different [case definitions for COVID-19](https://github.com/nychealth/coronavirus-data#case-definitions-for-covid-19)
  * Cumulative data, such as case, hospitalization, and death rates, are for confirmed COVID-19 cases only
  
* Updating all files by geography to reflect a revised geocoding process
  * The Health Department receives borough of residence and other address information as part of routine reportable disease surveillance. These geographic data require substantial cleaning prior to analysis and presentation, and the data in this repository reflect an updated geocoding process as of December 7, 2020. Therefore, counts and rates by geographies (i.e., borough, modified ZIP code tabulation area) may change slightly.

*** 

## Important: Changes on November 9, 2020

In order to support an update to the [Health Department’s COVID-19 Data webpage](https://www1.nyc.gov/site/doh/covid/covid-19-data.page) on November 9, 2020, changes were made to this repository, including revisions to some key files, filenames, and locations. These changes include: 

* Adding daily 7-day cumulative percent positivity by modified ZIP code tabulation areas
* Adding test rate and percent positivity by age 
* Adding testing turnaround time 
* Using more granular categories for the display of data by age 
* Revising the output and presentation of data by borough 
* Reclassifying files as Latest, Trends, or Totals 
* Adding files with the now- prefix that truncate trend data to the last 90 days to display data with a focus on recent changes
* Changing the organization of select data elements as outlined in the crosswalk below:

| Prior file name(s) | New file name(s) | New file location | 
|----------------------------------------------------------------|--------------------------------------------------------------------------|-------------------| 
| boro.csv | by-boro.csv | Totals/ | 
| case-hosp-death.csv | data-by-day.csv | Trends/ | 
| tests-by-zcta | data-by-modzcta.csv | Totals/ | 
| boro/boroughs-case-hosp-death.csv | data-by-day.csv | Trends/ | 
| boroughs-by-age.csv, boroughs-by-race.csv, boroughs-by-sex.csv | group-data-by-boro.csv, group-case-by-boro.csv, group-hosp-by-boro,csv, group-deaths-by-boro.csv | Totals/ | 
| deaths/probable-confirmed-dod.csv | data-by-day.csv | Trends/ | 
| sydromic_data.csv | covid-like-illness.csv | Trends/ | 
| recent-4-week-citywide.csv | Similar data available in now-summary.csv | Latest/ | 
| recent-4-week-by-modzcta.csv | Similar data available in caserate-by-modzcta.csv, testrate-by-modzcta.csv, percentpositive-by-modzcta.csv | Trends/ | 

### 

***

# Key Technical Notes

## Public health reporting  
### Reporting lag 

Our data are updated either weekly on Thursday (at a 3-day lag or with data through the previous Saturday) or monthly (at a 14-day lag). For example, a 3-day lag means that the most recent data in the update are from three days before. These lags are due to standard delays (up to several days) in reporting a new test, case, hospitalization or death to the Health Department, and are a common limitation of surveillance data. Given the delay, our counts of what has happened in the most recent few days are artificially small. We delay publishing these data until more reports have come in and the data are more complete.

### Report date versus date of event 

Due to lags common with surveillance data, we receive reports of events (diagnoses, hospitalizations and deaths) that happened on past days. We publish trend data (e.g., case-hosp-death.csv) using date of event (date of diagnosis, date of hospitalization or date of death), not date of report. This approach may differ from the data published by other state and local health departments.

Publishing data by date of event better reflects when things actually happened (e.g., when a person went to the doctor to get tested), as opposed to when the Health Department learned about them. We strongly discourage data users from using daily changes to cumulative files as trend data – this represents information by report date and is prone to misuse and misinterpretation.  

### Differences between City and State values

Generally, the NYC Health Department and the New York State Department of Health will not have matching numbers for the same metrics, though they report the same general trends. Some reasons for this include:

- Different data sources for different metrics

- Different analytical and informatics processes

- Different uses of event date or report date (see above)

### Types of disease surveillance   

The Health Department conducts two main types of surveillance for COVID-19:    

- Syndromic surveillance   

- Reportable disease surveillance   

#### Syndromic surveillance   

We receive data from all 53 hospital emergency departments (EDs) in NYC about the types of illnesses people experience on a regular basis. This surveillance allows the Health Department to evaluate care-seeking trends at hospitals for influenza-like illness and pneumonia.    

The information on each patient is evaluated for descriptions that resemble influenza-like illness or pneumonia, or include the ICD-10-CM code (U07.1) for 2019 novel coronavirus disease. Influenza-like illness is defined as mention of either:

- Fever and cough      
- Fever and sore throat   
- Fever and shortness of breath or difficulty breathing 
- Influenza   

We exclude those who present with influenza-like illness and are subsequently assigned with only an ICD-10-CM code for influenza.

Pneumonia is defined as mention or diagnosis of pneumonia. Since the signs and symptoms of COVID-19 overlap with these categories that the Health Department tracks routinely, we are able to identify unusual spikes in people seeking care at hospitals. We are using this as a proxy measure to observe COVID-19-like disease in the population.   

- *Strengths*: The data show real-time, population-level trends of people seeking health care for COVID-like disease

- *Limitations*: The data do not represent patients with laboratory-confirmed COVID-19 

#### Reportable disease surveillance 

The Health Department receives electronic laboratory reports for a number of infectious diseases, including COVID-19, as required by law in the [NYC Health Code](https://www1.nyc.gov/site/doh/providers/reporting-and-services/notifiable-diseases-and-conditions-reporting-central.page). When a specimen is collected from a patient for SARS-CoV-2 laboratory testing, the laboratory must report all results, whether positive, negative, or inconclusive, to the Health Department. Limited demographic information on the person being tested is reported to the Health Department, including name, address, and date of birth. 

## Laboratory testing
### Types of COVID-19 laboratory tests

The COVID-19 testing landscape is continually changing. Please see the Health Department's [guidance on SARS-CoV-2 tests](https://www1.nyc.gov/assets/doh/downloads/pdf/covid/providers/covid-19-providers-testing-overview.pdf) for up to date information on the use and interpretation of tests. 

There are three main types of COVID-19 tests that are reported to the Health Department as part of reportable disease surveillance:

#### Diagnostic (viral) tests
- *Molecular tests*: The primary test for COVID-19 infection is the molecular test, which includes the polymerase chain reaction (PCR) test. Molecular tests work through direct detection of the virus’s genetic material, and typically involve collecting a nasal swab. After specimen collection, molecular tests are generally processed in large laboratories, and consequently, the results may take a few days to be delivered. These tests are highly accurate, and recommended for diagnosing current COVID-19 infection.   

- *Antigen tests*: This test detects proteins on the surface of the virus that are called antigens. The antigen test typically involves collecting a nasal swab. The results from an antigen test are delivered quickly ([turnaround as low as 15 minutes](https://www.cdc.gov/coronavirus/2019-ncov/lab/resources/antigen-tests-guidelines.html)), however, these tests are not as accurate as molecular tests, especially when the likelihood of someone having a COVID-19 infection is low.
 
 #### Serologic tests
- *Antibody tests*: Exposure to COVID-19 can be detected by measuring antibodies, which can reflect a person’s immune response to the virus. Antibodies are proteins produced by the body’s immune system that can be found in the blood. People can test positive for antibodies specific to COVID-19 after they have been exposed, sometimes when they no longer test positive for the virus itself. Therefore, an antibody test will not be accurate for someone with active or recent infection, but can identify people who likely had a previous COVID-19 infection. It is important to note that the science around COVID-19 antibody tests is evolving rapidly and there is still much uncertainty about what individual and population level antibody test results mean for the epidemiology of COVID-19. 

*Strengths*: This standard reporting system allows for rapid and detailed information to be transmitted routinely to the Health Department.     

*Limitations*:  

- Because of delays in reporting, the most recent data may be incomplete. Current data will be updated in the future as information on laboratory tests are reported to the Health Department. 

- Health Department recommendations for testing have changed throughout the COVID-19 outbreak. During the spring of 2020, the Health Department advised people with mild to moderate symptoms to stay at home and not seek testing to conserve testing supplies and personal protective equipment. Consequently, many cases in the community early in the outbreak were never diagnosed with a laboratory test and will not be included in these counts.    

- The testing landscape for COVID-19 is continually changing as new tests receive [emergency use authorization](https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/vitro-diagnostics-euas) from the Food and Drug Administration (FDA). For example, antigen testing started to become more widely available in NYC in October 2020. These changes in the types of tests should be considered when looking at trends across time. 

- Antibody testing started to become more widely available in NYC in April 2020. Cumulative data include all antibody tests with a specimen collection date after March 3, 2020, and data reported by week include tests conducted starting on April 5, 2020.

- The Health Department consistently receives electronic reports *only* for COVID-19 tests that are conducted in laboratories. Point-of-care and at-home tests may be conducted in a setting outside of a clinical laboratory; these settings often do not have the infrastructure for electronically reporting directly to the Health Department. While providers and facilities are required to report results from point-of-care and at-home tests to the Health Department within 24 hours, these data are incomplete.

- Most of the data in this repository include patients who reside in congregate facilities, such as correctional facilities and long-term care facilities. While data reported from these facilities may sometimes influence local trends, cases reported from these facilities do not necessarily represent community-based transmission. The only data that exclude patients in congregate facilities are in [pp-by-modzcta.csv](https://github.com/nychealth/coronavirus-data/tree/master/latest#pp-by-modzctacsv) and [last7days-by-modzcta.csv](https://github.com/nychealth/coronavirus-data/tree/master/latest#last7days-by-modzctacsv). 

- Because these data only provide information on people tested and not everyone who may have had COVID-19 in NYC, caution needs to be used when interpreting testing data. For example, people who are tested for antibodies may be more likely to test positive because people who were previously ill are preferentially seeking testing, in addition to the testing of persons with higher exposure (e.g., health care workers, first responders). Therefore, these data may not reflect antibody prevalence among all New Yorkers.  

- Increasing instances of screening programs further impact the generalizability of all testing data, as screening programs influence who and how many people are tested over time. Examples of screening programs in NYC include: employers screening their employees (e.g., hospitals), and long-term care facility screening of residents and employees. 

- These data are based on electronic laboratory reports, which often lack information on demographic and clinical characteristics of interest, such as race and ethnicity, co-occurring medical conditions, presence and onset date of COVID-19 symptoms, reason for testing, and occupation. 

### Calculation of percent positivity

**Citywide percent positivity** values are currently calculated as follows: 

| Value | Definition | 
|-------|------------| 
| Daily values | The numerator includes all people with positive results on each specimen collection date, and the denominator includes all people who received a test on each specimen collection date | 
| 7-day average | The numerator includes all people with positive results in the last 7 days, and the denominator includes all people who received a test in the last 7 days. If a person is tested more than one time, they are only counted once. If a person tests both positive and negative in the same 7-day period, the positive result is counted. | 
| 28-day average | The numerator includes all people with positive results in the last 28 days, and the denominator includes all people who received a test in the last 28 days. If a person is tested more than one time, they are only counted once. If a person tests both positive and negative in the same 28-day period, the positive result is counted. |

These values are inclusive of people who previously tested positive. These values are inclusive of persons who reside in long term care facilities and correctional facilities.

**Modified ZIP Code Tabulation Area (MODZCTA)-level percent positivity** values are currently calculated as follows: 

| Value | Definition | 
|-------|------------| 
| Daily values | Within each MODZCTA, the numerator includes all people with positive results on each specimen collection date, and the denominator includes all people who received a test on each specimen collection date | 
| 7-day average | Within each MODZCTA, the numerator includes all people with positive results in the last 7 days, and the denominator includes all people who received a test in the last 7 days. If a person is tested more than one time, they are only counted once. If a person tests both positive and negative in the same 7-day period, the positive result is counted. | 

These values exclude people who previously tested positive. These values exclude persons who reside in long term care facilities and correctional facilities.

## Counting COVID-19 cases, hospitalizations, and deaths
### Case definitions for COVID-19

Surveillance case definitions for all notifiable conditions are developed at the national level by the [Council of State and Territorial Epidemiologists (CSTE)](https://ndc.services.cdc.gov/). These standard definitions support public health officials in classifying and counting infections consistently across different states and local jurisdictions. The [criteria](https://ndc.services.cdc.gov/case-definitions/coronavirus-disease-2019-2020-08-05/) for reporting a person with COVID-19 infection (“case”) are based on laboratory test results and epidemiologic links, and include two classifications:

- *Confirmed COVID-19 case*: A person is classified as a confirmed COVID-19 case if they test positive with a molecular test

- *Probable COVID-19 case*: A person is classified as a probable COVID-19 case if they meet any of the following criteria with no positive molecular test on record: (a) test positive with an antigen test, (b) have symptoms and an exposure to a confirmed COVID-19 case, or (c) died and their cause of death is listed as COVID-19 or similar 

The [Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov/coronavirus/2019-ncov/hcp/duration-isolation.html) consider most people to be protected from getting COVID-19 again for up to 90 days after testing positive for the virus. For consistency, as of June 9, 2021, people who meet the definition of a confirmed or probable COVID-19 case >90 days after a previous positive test (date of first positive test) or probable COVID-19 onset date will be counted as a new case. Prior to June 9, 2021, new cases were counted ≥365 days after the first date of specimen collection or clinical diagnosis.

### Case reporting   

NYC COVID-19 data include people who live in NYC. Any person with a residence outside of NYC is not included.

### Reporting on hospitalization status  

The Health Department imports information on hospitalization status from a number of sources, including Regional Health Information Organizations, NYC public hospitals, non-public hospital systems, remote access to electronic health record systems, the Health Department’s electronic death registry system, and the Health Department's syndromic surveillance database that tracks daily hospital admissions from all 53 emergency departments across NYC. People who were hospitalized more than one time are only counted once.

Note that hospitalization information can be missing or incomplete from a number of facilities, which is a limitation for any analysis considering hospitalization status by geography (e.g., borough).  

With the November 9, 2020 update, we revised the definition of a COVID-19 hospitalization and removed people who were hospitalized more than 14 days before or after their COVID-19 diagnosis from our count. Starting October 6, 2022, we revised the definition of a COVID-19 hospitalization to prospectively include those diagnosed 14 days before through 3 days after their hospitalization. 

Hospitalizations are among confirmed or probable cases of COVID-19.

### Reporting on COVID-19 deaths  

COVID-19 deaths are reported from March 11, 2020 as this was the first date of death for a patient with confirmed COVID-19.   

Starting April 3, 2023, COVID-19 deaths are no longer classified as confirmed or probable. Deaths are counted as a COVID-19 death if: 

- the death certificate lists COVID-19 or an equivalent term as the underlying or a contributing cause of death, or 

- a case investigation for a confirmed, probable, or suspect COVID-19 case determined that COVID-19 was the cause of death or contributed to the death.

Prior to April 3, 2023, there were two classifications of COVID-19 deaths reported:   

- A death was classified as **confirmed** if the decedent was a NYC resident who had a positive molecular (PCR) test* for the virus that causes COVID-19 and did not die of external causes such as gunshot wounds or drug overdoses.   

- A death was classified as **probable** if the decedent was a NYC resident (or residency pending) who had no known positive molecular test for the virus that causes COVID-19 but the death certificate lists “COVID-19” or an equivalent as a cause of death.   

Starting in June 2020, people who died more than 60 days after their COVID-19 diagnosis and starting August 3, 2021, people who died more than 30 days after their COVID-19 diagnosis who did not have "COVID" or similar listed on their death certificate were removed from the death count. This was to address instances in which a person was diagnosed with COVID-19 and survived, but later died, likely of other causes.


**Differences between death counts between NYC and New York State:** Data on deaths reported by NYC are derived from the Health Department’s surveillance database and will be different from data reported by the New York State Department of Health. The State Department of Health reports data on deaths from:   

- The State Hospital Emergency Response Data System   
- Daily calls to hospitals and other facilities that are caring for patients, such as nursing homes   

The NYC Health Department reports data on deaths that reflect both:   

- Positive tests for COVID-19 confirmed by laboratories   
- Confirmations of a person’s death from the City’s Office of the Chief Medical Examiner and the Health Department's Bureau of Vital Statistics, which is responsible for the registration, analysis and reporting of all deaths in NYC 

### Changes to reported data   

The Health Department updates data for earlier dates after resolving testing and reporting delays. Reported data reflect what we know at the time of publishing on Github, not what occurred in real time. For example, we may find that a person who was originally reported to live in NYC no longer does. This person would be removed from our dataset after their address is updated, and our case count would decrease by one.    

### Rates vs. case counts   

The Health Department is reporting rates of cases, hospitalizations, and deaths in addition to counts. We report rates to give clear comparisons between different groups — such as borough, sex, or age — with differently sized populations. For example, we may report that the rate of confirmed COVID-19 cases is 100 per 100,000 population in NYC. That means for every 100,000 people living in NYC, there are 100 people diagnosed with COVID-19.    

### Rates per 100,000 people   

Rates for annual citywide-, borough-, ZIP code tabulation areas-, and demographic-specific categories were calculated using interpolated intercensal population estimates updated in 2020. These rates differ from previously reported rates based on the 2000 Census or previous versions of population estimates. The Health Department produced these population estimates based on estimates from the U.S. Census Bureau and NYC Department of City Planning. 

Please note that population estimates were updated on November 9, 2020 to reflect annual population estimates for all New Yorkers as of July 1, 2019. These estimates are prior to the COVID-19 outbreak, and therefore, do not represent any changes to NYC’s population as a result of COVID-related migration. 

Rates of cases, hospitalizations, and deaths for poverty and race/ethnicity groups were calculated using direct standardization for age at diagnosis, hospitalization, or death and weighting by [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf).   

## Demographic characteristics
### Geography: ZIP codes and ZCTAs  

We report information by geography using modified ZIP Code Tabulation Areas (MODZCTA). It can be challenging to map data that are reported by ZIP Code. A ZIP Code doesn’t actually refer to an area, but rather a collection of points that make up a mail delivery route. Furthermore, there are some buildings that have their own ZIP Code, and some non-residential areas with ZIP Codes.  

To deal with the challenges of ZIP Codes, the Health Department uses ZCTAs which solidify ZIP codes into units of area. Often, data reported by ZIP code are actually mapped by ZCTA. The ZCTA geography was developed by the U.S. Census Bureau.  

The modified ZCTA (MODZCTA) geography combines census blocks with smaller populations to allow more stable estimates of population size for rate calculation.  

Information by geography reflect people's MODZCTA of residence at the time of reporting, and not the location of testing, diagnosing, or hospitalization. 

### Poverty groups   

Neighborhood-level poverty groups were classified in a manner consistent with Health Department practices to [describe and monitor inequities in health in NYC](https://www1.nyc.gov/assets/doh/downloads/pdf/epi/epiresearch-SES-measure.pdf). Neighborhood poverty measures are defined as the percentage of people earning below the Federal Poverty Threshold (FPT) within a ZCTA, per the [American Community Survey 2014-2018](https://www.census.gov/newsroom/press-kits/2019/acs-5-year.html).

 The standard cut-points for defining categories of neighborhood-level poverty in NYC are:    

- Low: <10% of residents in ZCTA living below the FPT   
- Medium: 10% to <20%   
- High: 20% to <30%    
- Very high: ≥30% residents living below the FPT   

### Age groups  

The Health Department initially reported out data for the following age groups: 0-17, 18-44, 45-64, 65-74, and 75+ years. As of November 9, 2020, we updated the age groups to: 0-4, 5-12, 13-17, 18-24, 25-34, 35-44, 45-54, 55-64, 65-74, and 75+ years to provide more detail and granularity on age groups, especially with regard to children and young adults. For data on deaths, age groups 0-4, 5-12, and 13-17 are collapsed into 0-17 years due to low death counts in this population and to ensure protection of privacy. 

### Race and ethnicity  

Race and ethnicity information is often missing in reportable disease surveillance. Information on race/ethnicity typically comes from electronic laboratory reports and unfortunately, race/ethnicity data are often missing in these reports. For the COVID-19 response, the Health Department has electronically imported aggregated data from partners such as hospitals, hospital systems, or Regional Health Information Organizations to improve the completeness of race/ethnicity data for people who are hospitalized. However, health records may also be missing race/ethnicity information. Additionally, the Health Department often investigates or imports race/ethnicity information for people who have died. However, this information is often incomplete or not immediately available because it can take a few days for the information to be entered into the electronic death registration system. Race/ethnicity information is typically collected by funeral directors from next of kin of the decedent. 

The Health Department classifies race/ethnicity into the following mutually-exclusive categories: Asian/Pacific-Islander, Black/African-American, Hispanic/Latino, and White. Information on people identified as other categories, including Native American/Alaska Native or multi-racial, are not provided in files showing race/ethnicity data. The Hispanic/Latino category includes people of any race, and all other categories exclude those who identified as Hispanic/Latino.

Differences in health outcomes among racial and ethnic groups are due to long-term institutional and personal biases against people of color. There is no evidence that these health inequities are due to personal traits. Lasting racism and an inequitable distribution of resources needed for wellness cause these health inequities. These include quality jobs, housing, health care and food, among others. The greater impact of the COVID-19 pandemic on people of color shows how these inequities influence health outcomes. 

## Variants of the SARS-CoV-2 virus

Multiple [variants of the SARS-CoV-2 virus](https://www.cdc.gov/coronavirus/2019-ncov/transmission/variant.html) have been characterized in the US and globally. These variants involve mutations to the SARS-CoV-2 virus, and might make COVID-19 easier to spread, more severe, or more likely to reinfect people who have either had COVID-19 before or who have been vaccinated. 

### Surveillance for variants

Variants can be detected through [genomic sequencing](https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/variant-surveillance.html), a process that involves analyzing the virus's genetic material. Sequencing occurs on specimens collected for COVID-19 molecular laboratory testing, and determines which variant of the SARS-CoV-2 virus a particular person was infected with.

The City’s Public Health Laboratory (PHL) and Pandemic Response Laboratory (PRL) have been sequencing a subset of SARS-CoV-2 laboratory specimens to identify emerging variants in NYC. Since October 2020, the PHL has sequenced all laboratory specimens received that meet certain technical criteria (e.g., sufficient levels of virus in a sample). Starting in February 2021, the PRL sequenced randomly selected specimens that meet certain technical criteria. As of January 2022, PRL has closed and is no longer sequencing specimens. 

A small proportion of all confirmed COVID-19 cases are now being sequenced citywide. As such, all findings related to variant data are based on a small subset of all confirmed COVID-19 cases. Because patients who have specimens sequenced are likely to be different than those that do not, findings may not be representative of all confirmed COVID-19 cases citywide, and should be interpreted with caution. Additional specimens are being sequenced by the New York State Wadsworth Laboratory and university, hospital, and private laboratories, and reported to the Health Department. These include samples from NYC Health & Hospitals emergency departments, the Office of the Chief Medical Examiner, and other sources, which may bias data toward more severe cases. 

Laboratories have identified multiple variants which have emerged in NYC. The Health Department uses findings from the PHL and PRL, as well as other laboratories reporting findings to the Health Department in combination with epidemiologic surveillance systems, to better understand whether the variant might affect: 
* **Transmission**: Whether these variants increase transmission, making it easier to spread COVID-19
* **Re-infection**: Whether these variants are more likely to re-infect people who previously had COVID-19
* **Vaccine effectiveness**: Whether these variants are more likely to infect fully vaccinated people. *Some infections among fully vaccinated people are expected to occur in a very small proportion of vaccinated people, regardless of the spread of variants.*
* **Severity**: Whether these variants are more likely to result in hospitalization or death

### Variant classifications

The [CDC classifies variants]( https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/variant-surveillance/variant-info.html#Interest) into the following three categories:

* **Variants of interest**: Has specific genetic markers associated with changes to receptor binding, reduced neutralization by antibodies generated against previous infection or vaccination, reduced efficacy of treatments, potential diagnostic impact, or predicted increase in transmissibility or disease severity
* **Variants of concern**: Evidence of an increase in transmissibility, more severe disease (e.g.,  increased hospitalizations or deaths), significant reduction in neutralization by antibodies generated during previous infection or vaccination, reduced effectiveness of treatments or vaccines, or diagnostic detection failure
* **Variants of high consequence**: Clear evidence that prevention measures or medical countermeasures (MCMs) have significantly reduced effectiveness relative to previously circulating variants

Please see the [CDC’s definitions of SARS-CoV-2 variants](https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/variant-surveillance/variant-info.html) for more information. Details on the variants that have emerged in NYC, which are being actively monitored are available on the [“Variants” page of the Health Department’s COVID-19 Data webpage]( https://www1.nyc.gov/site/doh/covid/sdah-variants.page). 

The Health Department is continuing to investigate the emergence of variants of concern and variants of interest in NYC, using a combination laboratory and epidemiologic observations to characterize each variant. Some ongoing efforts include:
* Monitoring the number of hospitalizations and deaths that occur among patients with sequenced specimens that are caused by variants
* Identifying cases caused by variants where the person had a previous positive diagnostic test for COVID-19 more than 90 days earlier. These cases are investigated to determine if they are likely to represent a reinfection, and to determine if reinfection cases are more common in people who have been infected with one of the variants
* Matching data on cases caused by variants with the NYC Citywide Immunization Registry to identify if the person was fully immunized prior to testing positive for COVID-19

***   

## Repository contents 

### latest/ 

This folder contains files with data that focus on the most recent period of the outbreak. It includes daily 7-day cumulative percent positivity for the molecular test by MODZCTA, daily 28-day counts and rates of hospitalizations and deaths by MODZCTA, and trend data that cover the most recent 90 days. See this folder’s [Readme](https://github.com/nychealth/coronavirus-data/tree/master/latest#latest) for a detailed description of its contents.  

### totals/ 

This folder contains files with cumulative totals since the start of the COVID-19 outbreak in NYC, which the Health Department defines as the diagnosis of the first confirmed COVID-19 case on February 29, 2020. The Health Department recommends against interpreting daily changes to these files as one day’s worth of data, due to the difference between date of event and date of report. See this folder’s [Readme](https://github.com/nychealth/coronavirus-data/tree/master/totals#totals) for a detailed description of its contents. 

### trends/ 

This folder contains files with daily, weekly, and monthly data shown across time. Note that these trend data are published by date of event, not by date of report. The Health Department recommends against interpreting daily changes to these files as one day’s worth of data, due to the difference between date of event and date of report. See this folder’s [Readme](https://github.com/nychealth/coronavirus-data/tree/master/trends#trends) for a detailed description of its contents. 

### variants/ 

This folder contains files with data on SARS-CoV-2 variants. It includes information on the number and type of SARS-CoV-2 variants identified in NYC, over time and by MODZCTA. All tables containing variant data are updated weekly on Thursday (with data through two previous Saturdays). These files are based on a small subset of all confirmed COVID-19 cases; findings may not be representative of all confirmed COVID-19 cases citywide, and should be interpreted with caution. See this folder’s [Readme](https://github.com/nychealth/coronavirus-data/tree/master/variants#variants) for a detailed description of its contents.  

### Geography-resources/ 

This folder contains additional resources for data provided by MODZCTA geographies, inlcuding geographic files for MODZCTA. See this folder’s [Readme](https://github.com/nychealth/coronavirus-data/blob/master/Geography-resources/README.md) for a detailed description of its contents.

### archive/ 

This folder contains files that are no longer updated. 
