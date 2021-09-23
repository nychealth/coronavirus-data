# variants/ 

This folder contains files with data on SARS-CoV-2 variants. It includes information on the number and type of SARS-CoV-2 variants identified in NYC over time. All tables containing variant data are updated weekly on Thursday (with data through the previous Saturday). These files are based on a small subset of all confirmed COVID-19 cases; findings may not be representative of all confirmed COVID-19 cases citywide, and should be interpreted with caution. 

**8/26/2021: Important note**:
An increase in percent of lineages classified as  “other” for previously reported data is due to a recent Pangolin reclassification of some variants of concern and variants of interest, which especially impacted cases that had initially been classified as B.1.526 from March and April 2021. ([Pangolin](https://cov-lineages.org/resources/pangolin.html) is a web application used to assign  lineage designations to SARS-CoV-2 genome sequences.)

## Files 

### cases-sequenced.csv

This file contains counts of confirmed cases, stratified by whether a laboratory specimen was submitted to a NYC laboratory for genomic sequencing. Please see the technical notes for a description of the different [laboratories that perform sequencing in NYC](https://github.com/nychealth/coronavirus-data#variants-of-the-sars-cov-2-virus). 

People with confirmed COVID-19 are categorized based on: the date of collection of the sequenced specimen for those with sequencing and the date of diagnosis for those without sequencing. Data are aggregated by full-weeks starting each Sunday and ending on Saturday. For example, a person who was diagnosed with COVID-19 on Monday, May 3, 2021 would be categorized as diagnosed during the week ending May 8, 2021. 

Indicators include: 
| Variable Name | Definition | Timeframe |   
|---------------------|---------------|----------------| 
| WEEK_ENDING | Week-ending date | |       
| NOT_SEQUENCED | Number of confirmed cases *without* a specimen submitted to a NYC laboratory for sequencing | Full week preceding the week-ending date |       
| SEQUENCED | Number of confirmed cases *with* a specimen submitted to a NYC laboratory for sequencing | Full week preceding the week-ending date |     
| CASES | Number of confirmed cases citywide | Full week preceding the week-ending date|     
| PCT_SEQUENCED | Percentage of confirmed cases with a specimen submitted to a NYC laboratory for sequencing | Full week preceding the week-ending date |     
| INCOMPLETE | Used for display purposes only | |     

Note that sum of counts in this file may not match values in citywide tables because of records with missing data.

### variant-classification.csv

This file contains the cumulative percentage of confirmed cases across the most recent 4-week period, by SARS-CoV-2 variant. The variants specified in this file represent the most common ones identified in NYC on the date of posting, and will be updated based on emerging genomic sequencing and epidemiologic data.

Please see the technical notes for a description of the different [definitions of SARS-CoV-2 variants](https://github.com/nychealth/coronavirus-data#variants-of-the-sars-cov-2-virus).

Indicators include:
| Variable Name | Definition | Timeframe |   
|---------------------|---------------|----------------| 
| VARIANT | Genetic variant of SARS-CoV-2 | | 
| NAME | Variant label per [World Health Organization (WHO) nomenclature](https://www.who.int/en/activities/tracking-SARS-CoV-2-variants/) | | 
| COUNT | Number of confirmed cases by SARS-CoV-2 variant | Cumulative across most recent 4-week period | 
| TOTAL | Number of confirmed cases with a specimen submitted to a NYC laboratory for sequencing | Cumulative across most recent 4-week period | 
| PERCENT_IN_NYC | Percentage of confirmed cases by SARS-CoV-2 variant | Cumulative across most recent 4-week period | 

Note that sum of counts in this file may not match values in citywide tables because of records with missing data.

### variant-epi-data.csv

This file contains the counts and percentages of confirmed cases, by SARS-CoV-2 variant. The SARS-CoV-2 variant and measure of interest (count or percent) are indicated in each column heading. The variants specified in this file represent the most common ones identified in NYC on the date of posting, and will be updated based on emerging genomic sequencing and epidemiologic data.

Please see the technical notes for a description of the different [definitions of SARS-CoV-2 variants](https://github.com/nychealth/coronavirus-data#variants-of-the-sars-cov-2-virus).

People with confirmed COVID-19 are categorized based on the date of collection of the sequenced specimen, and are aggregated by full-weeks starting each Sunday and ending on Saturday. For example, a person whose specimen was sequenced on Monday, May 3, 2021 would be categorized as sequenced during the week ending May 8, 2021. 

Note that sum of counts in this file may not match values in citywide tables because of records with missing data.
