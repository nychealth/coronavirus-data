### nyc_alert_levels.csv    
This file tracks NYC’s Alert Level to help communities and individuals make informed decisions about what COVID precautions and safety measures should be taken. The alert levels range from low to very high based on guidelines set by the [CDC](https://www.cdc.gov/coronavirus/2019-ncov/science/community-levels.html). 

#### A combination of three metrics are used to determine the alert level: 
* New confirmed and probable cases per 100,000 people in the last seven days (7-day total)
* New admissions with COVID-19 per 100,000 people in the last seven days (7-day total)
* Percent of inpatient beds occupied by COVID-19 patients (7-day average)

Data on new COVID-19 cases serve as an early warning indicator of potential increases in healthcare system strain in the event of a COVID-19 surge. 
These data are also available in the [/latest folder of the coronavirus-data]( coronavirus-data/7day-transmission-rate.csv at master · nychealth/coronavirus-data (github.com) GitHub repository. New COVID-19 admissions and the percent of inpatient beds occupied represent the current strain on the healthcare system. These data come from NYS’s Health Electronic Response Data System (HERDS) and can be accessed [from the State’s data portal](https://health.data.ny.gov/Health/New-York-State-Statewide-COVID-19-Hospitalizations/jw46-jpb7).

| Variable Name | Definition | 
|------------------|----------------------------------------------------------------------------------------------------|
| last_update_date | Date of data's most recent update |    
| nyc_case_rate__7_day_total | NYC confirmed and probable cases per 100,000 people in the last seven days|     
| nyc_total_new_covid_admissions_per_100k_last_7_days | New admissions with COVID-19 per 100,000 people in the last seven days |      
| nyc_percent_staffed_inpatient_beds_occupied_by_COVID_patients_7_day_avg | Percent of inpatient beds occupied by COVID-19 patients  (7-day average)|    
| nyc_alert_level | Current NYC alert level status |
| nyc_case_rate__7_day_total__status | The seven day trend for cases per 100,000 people |
| nyc_total_new_covid_admissions_per_100k_last_7_days__status	| The seven day trend for new admissions with COVID-19 per 100,000 people |
| nyc_percent_staffed_inpatient_beds_occupied_by_COVID_patients_7_day_avg__status | The seven day trend for the percent of inpatient beds occupied by COVID-19 patients |
