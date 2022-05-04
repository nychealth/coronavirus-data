### nyc_alert_levels.csv    
This file tracks NYC’s Alert Level to help communities and individuals make informed decisions about what COVID precautions and safety measures should be taken. The alert levels range from low to very high based on guidelines set by the [CDC](https://www.cdc.gov/coronavirus/2019-ncov/science/community-levels.html). 

#### A combination of three metrics are used to determine the alert level: 
* New confirmed and probable cases per 100,000 people in the last seven days (7-day total)
* New admissions with COVID-19 per 100,000 people in the last seven days (7-day total)
* Percent of inpatient beds occupied by COVID-19 patients (7-day average)

Data on new COVID-19 cases serve as an early warning indicator of potential increases in healthcare system strain in the event of a COVID-19 surge. 
These data are also available in the [/latest folder of the coronavirus-data](https://github.com/nychealth/coronavirus-data/blob/master/latest/7day-transmission-rate.csv) of this repository. Newly reported COVID-19 admissions and the percent of inpatient beds occupied represent the current strain on the healthcare system. These data come from NYS’s Health Electronic Response Data System (HERDS) and can be accessed [from the State’s data portal](https://health.data.ny.gov/Health/New-York-State-Statewide-COVID-19-Hospitalizations/jw46-jpb7). 

Generally, the NYC Health Department (NYC DOH) and the New York State Department of Health will not have matching numbers for metrics, though they report the same general trends. Alert level admission rates, sourced from NYS HERDS, may not match hospitalization rates shown in the /latest or /trends folders of this repository.

Some reasons for this include:
* Different data sources. NYS uses a self-reported hospital survey to report admissions whereas NYC uses data from a combination of sources, including Regional Health Information Organizations, hospital electronic health records, syndromic surveillance, and death registries.
* Different analytical and informatics processes
* Different uses of event date or report date. NYC publishes trend data (e.g., case-hosp-death.csv) using date of event (date of diagnosis, date of hospitalization or date of death), not date of report. This approach differs from the data published by NYS which is by date of report.
* NYS admissions data include non-NYC residents hospitalized at NYC hospitals
* Alert level trends compare this week to last week whereas the summary table on the [COVID-19 data page](https://www1.nyc.gov/site/doh/covid/covid-19-data.page) compares last week to last month. 

| Variable Name | Definition | 
|------------------|----------------------------------------------------------------------------------------------------|
| last_update_date | Date of data's most recent update |    
| nyc_case_rate__7_day_total | NYC confirmed and probable cases per 100,000 people in the last seven days|     
| nyc_total_new_covid_admissions_per_100k_last_7_days | Newly reported admissions with COVID-19 per 100,000 people in the last seven days |      
| nyc_percent_staffed_inpatient_beds_occupied_by_COVID_patients_7_day_avg | Percent of inpatient beds occupied by COVID-19 patients  (7-day average)|    
| nyc_alert_level | Current NYC alert level status |
| nyc_case_rate__7_day_total__status | The seven day trend for cases per 100,000 people |
| nyc_total_new_covid_admissions_per_100k_last_7_days__status	| The seven day trend for new admissions with COVID-19 per 100,000 people |
| nyc_percent_staffed_inpatient_beds_occupied_by_COVID_patients_7_day_avg__status | The seven day trend for the percent of inpatient beds occupied by COVID-19 patients 
