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

### testing.csv
This file includes counts of New York City residents with specimens collected for SARS-CoV-2 testing by day, the subsets who tested positive as confirmed COVID-19 cases, were ever hospitalized, and who died, as of the date of extraction from the NYC Health Department's disease surveillance database. For each date of extraction, results for all specimen collection dates are appended to the bottom of the dataset. Lags between specimen collection date and report dates of cases, hospitalizations, and deaths can be assessed by comparing counts for the same specimen collection date across multiple data extract dates.

### tests-by-zcta.csv
This file includes the cumulative count of New York City residents by ZIP code of residence who:
- Were ever tested for COVID-19 (SARS-CoV-2) 
- Tested positive
The cumulative counts are as of the date of extraction from the NYC Health Department's disease surveillance database.

## Technical Notes
This section may change as data and documentation are updated.

### Estimated number of COVID-19 patients ever hospitalized
At this time, NYC DOHMH does not have the ability to robustly quantify the number of people currently admitted to a hospital given intense resource and time constraints on hospital reporting systems. Therefore, we have estimated the number of individuals diagnosed with COVID-19 who have ever been hospitalized by matching the list of key fields from known cases that are reported by laboratories to the NYC DOHMH Bureau of Communicable Disease surveillance database to other sources of hospital admission information. These other sources include:
- The NYC DOHMH syndromic surveillance database that tracks daily hospital admissions from all 53 emergency departments across NYC  
- The New York State Department of Health Hospital Emergency Response Data System (HERDS). 

### Rates per 100,000 people
Annual citywide, borough-specific, and demographic specific intercensal population estimates from 2018 were developed by NYC DOHMH on the basis of the US Census Bureau’s Population Estimates Program, as of November 2019. 

Rates of cases at the borough-level were calculated using direct standardization for age at diagnosis and weighting by [the US 2000 standard population](https://www.cdc.gov/nchs/data/statnt/statnt20.pdf). 