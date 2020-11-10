# NYC Coronavirus Disease 2019 (COVID-19) Data   

This repository contains data on Coronavirus Disease 2019 (COVID-19) in New York City (NYC). Tables are updated either daily (at a 3-day lag) or weekly on Thursday (with data through the previous Saturday).

You can view visualizations of these data on the [Health Department’s COVID-19 Data webpage](https://www1.nyc.gov/site/doh/covid/covid-19-data.page). Additional data related to COVID-19 are available via [NYC Open Data](https://data.cityofnewyork.us/browse?category=Health&q=covid). 

Data are preliminary and subject to change. Information on this page will change as data and documentation are updated.   

The Health Department classifies the start of the COVID-19 outbreak in NYC as the date of the first laboratory-confirmed case, February 29, 2020.  

** 

## Important: changes on November 9, 2020

In order to support an update to the [Health Department’s COVID-19 Data webpage](https://www1.nyc.gov/site/doh/covid/covid-19-data.page) on November 9, 2020, changes were made to this repository, including revisions to some key files, filenames, and locations. These changes include: 
* Adding daily 7-day cumulative percent positivity by modified ZIP code tabulation areas
* Adding test rate and percent positivity by age 
* Adding test result lag time 
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
| deaths/probable-confirmed-dod.csv | data-by-day.csv | Totals/ | 
| sydromic_data.csv | covid-like-illness.csv | Trends/ | 
| recent-4-week-citywide.csv | Similar data available in now-summary.csv | Latest/ | 
| recent-4-week-by-modzcta.csv | Similar data available in caserate-by-modzcta.csv, testrate-by-modzcta.csv, percentpositive-by-modzcta.csv | Trends/ | 

### Questions and custom requests 

- We will try to answer questions about the data in this repository as we are able to. If you have a question, please search the [Issues](https://github.com/nychealth/coronavirus-data/issues?q=) to see if it’s already been addressed. Please understand that we are responding to a pandemic and we might not be able to address all questions in a timely manner.  

- We are not able to accommodate custom data requests placed via Github.   

### 

***

## Key notes  
### Reporting lag 

Our data are published with a three-day lag, meaning that the most recent data in today's update are from three days before. This lag is due to the standard delays (up to several days) in reporting a new test, case, hospitalization or death to the Health Department, and is a common limitation of surveillance data. Given the delay, our counts of what has happened in the most recent few days are artificially small. We delay publishing these data until more reports have come in and the data are more complete.

### Report date versus date of event 

Due to lags common with surveillance data, we receive reports of events (diagnoses, hospitalizations and deaths) that happened on past days. We publish trend data (e.g., case-hosp-death.csv) using date of event (date of diagnosis, date of hospitalization or date of death), not date of report. This approach may differ from the data published by other state and local health departments.

Publishing data by date of event better reflects when things actually happened (e.g., when a person went to the doctor to get tested), as opposed to when the Health Department learned about them. We strongly discourage data users from using daily changes to cumulative files as trend data – this represents information by report date and is prone to misuse and misinterpretation.  

### Differences between City and State values

Generally, the NYC Health Department and the New York State Department of Health will not have matching numbers for the same metrics, though they report the same general trends. Some reasons for this include:

- Different data sources for different metrics

- Different analytical and informatics processes

- Different uses of event date or report date (see above)

### Types of surveillance   

The Health Department conducts two main types of surveillance for COVID-19:    

- Syndromic surveillance   

- Reportable disease surveillance   

#### Syndromic surveillance   

We receive data from all 53 hospital emergency departments (EDs) in NYC about the types of illnesses people experience on a regular basis. This surveillance allows the Health Department to evaluate care-seeking trends at hospitals for influenza-like illness and pneumonia.    

The information on each patient is evaluated for descriptions that resemble influenza-like illness or pneumonia. Influenza-like illness is defined as mention of either:   
- Fever and cough      
- Fever and sore throat   
- Fever and shortness of breath or difficulty breathing 
- Influenza   

Pneumonia is defined as mention or diagnosis of pneumonia. Since the signs and symptoms of COVID-19 overlap with these categories that the Health Department tracks routinely, we are able to identify unusual spikes in people seeking care at hospitals. We are using this as a proxy measure to observe COVID-19-like disease in the population.   

- *Strengths*:  The data show real-time, population-level trends of people seeking health care for COVID-like disease

- *Limitations*: The data do not represent patients with laboratory-confirmed COVID-19 

#### Reportable disease surveillance 

The Health Department receives electronic laboratory reports for a number of infectious diseases, including COVID-19, as required by law in the [NYC Health Code](https://www1.nyc.gov/site/doh/providers/reporting-and-services/notifiable-diseases-and-conditions-reporting-central.page). When a specimen is collected from a patient for SARS-CoV-2 laboratory testing, the laboratory must report all results, whether positive, negative, or inconclusive, to the Health Department. Limited demographic information on the person being tested is reported to the Health Department, including name, address, and date of birth. 
   
There are two main categories of COVID-19 tests that are reported to the Health Department: 

- *Virus (diagnostic) tests*: The primary test for COVID-19 infection is the polymerase chain reaction (PCR) test. The PCR test works through direct detection of viral RNA, and typically involves collecting a nasal swab. The [laboratory criteria](https://cdn.ymaws.com/www.cste.org/resource/resmgr/2020ps/Interim-20-ID-01_COVID-19.pdf) for reporting a person with confirmed COVID-19 infection (“case”) are based on the PCR test, and as such, all of the confirmed COVID-19 cases reported out by the Health Department represent people with positive PCR tests. 

- *Antibody tests*: Exposure to COVID-19 can be detected by measuring antibodies, which can reflect a person’s immune response to the virus. Antibodies are proteins produced by the body’s immune system that can be found in the blood. People can test positive for antibodies after they have been exposed, sometimes when they no longer test positive for the virus itself. It is important to note that the science around COVID-19 antibody tests is evolving rapidly and there is still much uncertainty about what individual and population level antibody test results mean for the epidemiology of COVID-19.   

*Strengths*: This standard reporting system allows for rapid and detailed information to be transmitted routinely to the Health Department.     

*Limitations*:  

- Because of delays in reporting, the most recent data may be incomplete. Current data will be updated in the future as information on laboratory tests are reported to the Health Department. 

- Health Department recommendations for testing have changed throughout the COVID-19 outbreak. During the spring of 2020, the Health Department advised people with mild to moderate symptoms to stay at home and not seek testing to conserve testing supplies and personal protective equipment. Consequently, many cases in the community early in the outbreak were never diagnosed with a laboratory test and will not be included in these counts.    

- Most of the data in this repository include patients who reside in congregate facilities, such as correctional facilities and long-term care facilities. While data reported from these facilities may sometimes influence local trends, cases reported from these facilities do not necessarily represent community-based transmission. The only data that exclude patients in congregate facilities are in pp-by-modzcta.csv. 

- Because these data only provide information on people tested and not everyone who may have had COVID-19 in NYC, caution needs to be used when interpreting both PCR and antibody data. For example, people who are tested for antibodies may be more likely to test positive because people who were previously ill are preferentially seeking testing, in addition to the testing of persons with higher exposure (e.g., health care workers, first responders). Therefore, these data may not reflect antibody prevalence among all New Yorkers.  

- Increasing instances of screening programs further impact the generalizability of both PCR and antibody data, as screening programs influence who and how many people are tested over time. Examples of screening programs in NYC include: employers screening their employees (e.g., hospitals), and long-term care facility screening of residents and employees. 

- These data are based on electronic laboratory reports, which often lack information on demographic and clinical characteristics of interest, such as race and ethnicity, co-occurring medical conditions, presence and onset date of COVID-19 symptoms, reason for testing, and occupation. 

- The Health Department consistently receives electronic reports only for COVID-19 tests that are conducted in laboratories. COVID-19 tests that are conducted at-home or at point-of-care (e.g., antigen tests) are not represented in routine reportable disease surveillance. 

***   

## Technical notes   

### Case reporting   

NYC COVID-19 data include people who live in NYC or who live in another country but are being treated in NYC. The data do not include people who live outside of NYC but in the United States.  

### Changes to reported data   

We update data for earlier dates after we resolve testing and reporting delays. Reported data reflect what we know at the time of publishing on Github, not what occurred in real time. For example, we may find that a person who was originally reported to live in NYC no longer does. This person would be removed from our dataset after their address is updated, and our case count would decrease by one.    

### Rates vs. case counts   

The Health Department is reporting rates of cases, hospitalizations, and deaths in addition to counts. We report rates to give clear comparisons between different groups — such as borough, sex, or age — with differently sized populations. For example, we may report that the rate of confirmed COVID-19 cases is 100 per 100,000 population in NYC. That means for every 100,000 people living in NYC, there are 100 people diagnosed with COVID-19.    

### Rates per 100,000 people   

Rates for annual citywide-, borough-, ZIP code tabulation areas-, and demographic-specific categories were calculated using interpolated intercensal population estimates updated in 2020. These rates differ from previously reported rates based on the 2000 Census or previous versions of population estimates. The Health Department produced these population estimates based on estimates from the U.S. Census Bureau and NYC Department of City Planning. 

Please note that population estimates were updated on November 9, 2020 to reflect annual population estimates for all New Yorkers as of July 1, 2019. These estimates are prior to the COVID-19 outbreak, and therefore, do not represent any changes to NYC’s population as a result of COVID-related migration. 

Rates of cases, hospitalizations, and deaths for poverty and race/ethnicity groups were calculated using direct standardization for age at diagnosis and weighting by [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf).   

### Geography: ZIP codes and ZCTAs  

We report information by geography using modified ZIP Code Tabulation Areas (modified ZCTA). It can be challenging to map data that are reported by ZIP Code. A ZIP Code doesn’t actually refer to an area, but rather a collection of points that make up a mail delivery route. Furthermore, there are some buildings that have their own ZIP Code, and some non-residential areas with ZIP Codes.  

To deal with the challenges of ZIP Codes, the Health Department uses ZCTAs which solidify ZIP codes into units of area. Often, data reported by ZIP code are actually mapped by ZCTA. The ZCTA geography was developed by the U.S. Census Bureau.  

The modified ZCTA (MODZCTA) geography combines census blocks with smaller populations to allow more stable estimates of population size for rate calculation.  

### Poverty groups   

Neighborhood-level poverty groups were classified in a manner consistent with Health Department practices to [describe and monitor inequities in health in NYC](https://www1.nyc.gov/assets/doh/downloads/pdf/epi/epiresearch-SES-measure.pdf). Neighborhood poverty measures are defined as the percentage of people earning below the Federal Poverty Threshold (FPT) within a ZCTA, per the [American Community Survey 2014-2018](https://www.census.gov/newsroom/press-kits/2019/acs-5-year.html).

 The standard cut-points for defining categories of neighborhood-level poverty in NYC are:    

- Low: <10% of residents in ZCTA living below the FPT   

- Medium: 10% to <20%   

- High: 20% to <30%    

- Very high: ≥30% residents living below the FPT   

### Age groups  

The Health Department initially reported out data for the following age groups: 0-17, 18-44, 45-64, 65-74, and 75+ years. As of November 9, 2020, we updated the age groups to: 0-4, 5-12, 13-17, 18-24, 25-34, 35-44, 45-54, 55-64, 65-74, and 75+ years to provide more detail and granularity on age groups, especially with regard to children and young adults. For data on deaths, age groups 0-4, 5-12, and 13-17 are collapsed into 0-17 years due to low death counts in this population and to ensure protection of privacy. 

### Reporting on hospitalization status  

The Health Department imports information on hospitalization status from a number of sources, including Regional Health Information Organizations, NYC public hospitals, non-public hospital systems, remote access to electronic health record systems, the Health Department’s electronic death registry system, and the Health Department's syndromic surveillance database that tracks daily hospital admissions from all 53 emergency departments across NYC.  

Note that hospitalization information can be missing or incomplete from a number of facilities, which is a limitation for any analysis considering hospitalization status by geography (e.g., borough).  

With the November 9, 2020 update, we revised the definition of a COVID-19 hospitalization and removed people who were hospitalized more than 14 days before or after their COVID-19 diagnosis from our count. 

### Reporting on COVID-19 deaths  

COVID-19 deaths are reported from March 11, 2020 as this was the first date of death for a patient with confirmed COVID-19.   

There are two classifications of COVID-19 deaths reported:   

- A death is classified as **confirmed** if the decedent was a NYC resident who had a positive laboratory test for the virus that causes COVID-19.   

- A death is classified as **probable** if the decedent was a NYC resident (or residency pending) who had no known positive laboratory test for the virus that causes COVID-19 but the death certificate lists “COVID-19” or an equivalent as a cause of death.   

As new information becomes available, some deaths previously classified as probable may be reclassified as confirmed. This may lead to a reduction in the number of probable deaths in daily reporting. 

Starting in June 2020, people who died more than 60 days after their COVID-19 diagnosis and who did not have "COVID" or similar listed on their death certificate have been removed from the death count. This is to address instances in which a person was diagnosed with COVID-19 and survived, but later died, likely of other causes. 

Differences between death counts between NYC and New York State: Data on deaths reported by NYC are derived from the Health Department’s surveillance database and will be different from data reported by the New York State Department of Health. The State Department of Health reports data on deaths from:   

- The State Hospital Emergency Response Data System   

- Daily calls to hospitals and other facilities that are caring for patients, such as nursing homes   

The NYC Health Department reports data on deaths that reflect both:   

- Positive tests for COVID-19 confirmed by laboratories   

- Confirmations of a person’s death from the City’s Office of the Chief Medical Examiner and the Health Department's Bureau of Vital Statistics, which is responsible for the registration, analysis and reporting of all deaths in NYC   

### Race and ethnicity  

Race and ethnicity information is often missing in reportable disease surveillance. Information on race/ethnicity typically comes from electronic laboratory reports and unfortunately, race/ethnicity data are often missing in these reports. For the COVID-19 response, the Health Department has electronically imported aggregated data from partners such as hospitals, hospital systems, or Regional Health Information Organizations to improve the completeness of race/ethnicity data for people who are hospitalized. However, health records may also be missing race/ethnicity information. Additionally, the Health Department often investigates or imports race/ethnicity information for people who have died. However, this information is often incomplete or not immediately available because it can take a few days for the information to be entered into the electronic death registration system. Race/ethnicity information is typically collected by funeral directors from next of kin of the decedent. 

Differences in health outcomes among racial and ethnic groups are due to long-term institutional and personal biases against people of color. There is no evidence that these health inequities are due to personal traits. Lasting racism and an inequitable distribution of resources needed for wellness cause these health inequities. These include quality jobs, housing, health care and food, among others. The greater impact of the COVID-19 pandemic on people of color shows how these inequities influence health outcomes. 

### Antibody testing 

This repository contains data on antibody tests, which are also referred to as serology tests because they are performed on a blood sample. Antibody testing started to become more widely available in NYC in April 2020. Cumulative data include all serology tests reported to the Health Department after March 3, 2020, and data reported by week include tests reported starting on April 5, 2020. For calcuations of the number and percentage of people with positive results, people are considered positive if they ever receive a positive antibody result, regardless of whether they have received negative results as well.

***   

## Repository contents 

### latest/ 

This folder contains files with data that focus on the most recent period of the outbreak. It includes daily 7-day cumulative percent positivity by MODZCTA, and trend data that covers the most recent 90 days. See this folder’s Readme for a detailed description of its contents.  

### totals/ 

This folder contains files with cumulative totals since the start of the COVID-19 outbreak in NYC, which the Health Department defines as the diagnosis of the first laboratory-confirmed case on February 29, 2020. Note that the Health Department recommends against interpreting daily changes to these files as one day’s worth of data, due to the difference between date of event and date of report. See this folder’s Readme for a detailed description of its contents. 

### trends/ 

This folder contains files with daily or weekly data shown across time. Note that these trend data are published by date of event, not by date of report. See this folder’s Readme for a detailed description of its contents. 

### Geography-resources/ 

This folder contains additional resources for data provided by modified ZIP Code Tabulation Area geographies, inlcuding geographic files for MODZCTA. For details please visit its [Readme](https://github.com/nychealth/coronavirus-data/blob/master/Geography-resources/README.md). 

### archive/ 

This folder contains files that are no longer updated. 
