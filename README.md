# Income vs SAT Scores
This analysis uses SAT data from New York City Schools to determine the effect of median household income in an area on the SAT scores. The way the analysis was done is:
- Obtain data relating scores to the school's DBN (District Borough Number)
- Convert the DBN into a ZIP code, using the school's address
- Use Census data to find the median household income for that ZIP code

## Datasets
Here are the datasets used in this analysis:
- [2012-2013 School Locations](https://data.cityofnewyork.us/Education/2012-2013-School-Locations/emnd-d8ba)
- [Median Income By ZIP Code - US Census](https://data.census.gov/table?q=income&t=Income+and+Poverty&g=0400000US36$8600000&tid=ACSST5Y2021.S1901)
- [2012 New York City Schools Average SAT Scores](https://www.kaggle.com/datasets/new-york-city/new-york-city-sat-results)

## Results
Each point represents a school. The results of this analysis is here:

![Income on Math](results/math.png)

![Income on Reading](results/reading.png)

![Income on Total](results/score.png)

## Conclusions
There is a seemingly weak positive correlation between income and SAT scores for all aspects of the SAT (math, reading, total).
