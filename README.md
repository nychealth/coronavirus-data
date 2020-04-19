# NYC Coronavirus (COVID-19) data
This repository contains data on coronavirus (COVID-19) in New York City (NYC), updated daily. Data are assembled by the NYC Department of Health and Mental Hygiene (DOHMH) Incident Command System for COVID-19 Response (Surveillance and Epidemiology Branch in collaboration with Public Information Office Branch). You can view these data on [the Department of Health's website](https://www1.nyc.gov/site/doh/covid/covid-19-data.page). Note that data are  being collected in real-time and are preliminary and subject to change as COVID-19 response continues. 


## Files

### summary.csv
This file contains summary information, including when the dataset was "cut" - the cut-off date and time for data included in this update. 

Estimated hospitalization counts reflect the total number of people ever admitted to a hospital, not currently admitted.

### case-hosp-death.csv
This file includes daily counts of new confirmed cases, hospitalizations, and deaths. 
- Cases are by date of diagnosis
- Hospitalizations are by date of admission 
- Deaths are by date of death

Because of delays in reporting, the most recent data may be incomplete. Data shown currently will be updated in the future as new cases, hospitalizations, and deaths are reported.

### boro.csv
This contains rates of confirmed cases, by NYC borough of residence. Rates are:
- Cumulative since the start of the outbreak
- Age adjusted according to [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf)
- Per 100,000 people in the borough

### by-age.csv
This contains age-specific  rates of confirmed cases, hospitalizations, and deaths. 

### by-sex.csv
This contains rates of confirmed cases, hospitalizations, and deaths.

### tests-by-zcta.csv
This file includes the cumulative count of New York City residents by ZIP code of residence who:
- Were ever tested for COVID-19 (SARS-CoV-2) 
- Tested positive
The cumulative counts are as of the date of extraction from the NYC Health Department's disease surveillance database.

### probable-confirmed-dod.csv
This file includes deaths, by date of interest, for both confirmed COVID-19 deaths, and for probable COVID-19 deaths. Only deaths that occurred on or after March 11 are included (March 11 was the first date of death for a confirmed death). 
- A death is classified as confirmed if the decedent was a New York City resident who had a positive SARS CoV-2 (COVID-19) laboratory test. 
- A death is classified as probable if the decedent was a New York City resident (NYC resident or residency pending) who had no known positive laboratory test for SARS-CoV-2 (COVID-19) but the death certificate lists as a cause of death “COVID-19” or an equivalent. 

As new information becomes available, some deaths previously classified as probable may be reclassified as laboratory-confirmed.



## Technical Notes
This section may change as data and documentation are updated.

### Estimated number of COVID-19 patients ever hospitalized
At this time, NYC DOHMH does not have the ability to robustly quantify the number of people currently admitted to a hospital given intense resource and time constraints on hospital reporting systems. Therefore, we have estimated the number of individuals diagnosed with COVID-19 who have ever been hospitalized by matching the list of key fields from known cases that are reported by laboratories to the NYC DOHMH Bureau of Communicable Disease surveillance database to other sources of hospital admission information. These other sources include:
- The NYC DOHMH syndromic surveillance database that tracks daily hospital admissions from all 53 emergency departments across NYC  
- The New York State Department of Health Hospital Emergency Response Data System (HERDS). 

### Rates per 100,000 people
Annual citywide, borough-specific, and demographic specific intercensal population estimates from 2018 were developed by NYC DOHMH on the basis of the US Census Bureau’s Population Estimates Program, as of November 2019. 

Rates of cases at the borough-level were calculated using direct standardization for age at diagnosis and weighting by [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf). 