# Support scripts

## [git-export-all-file-versions](git-export-all-file-versions)

Used to pull out all historical copies of `case-hosp-death.csv`, so they can be assembled into the table `history.csv`.

## [generate-history.py](generate-history.py)

Aggregates the all historical copies of `case-hosp-death.csv` into the table `history.csv`.

## [update](update)

A script which does all the work of running the above scripts to update the historical data & then updating the notebooks.
