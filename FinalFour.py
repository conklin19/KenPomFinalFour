## Code Louisville ##
## Data 1 Final Project ##
## Adam Conklin ##
## Analyzing KenPom Data for NCAA Final Four Teams ##

import matplotlib as mp
import pandas as pd
import seaborn as sns
import numpy as np

##Requirement 1.2 Read-In local csv using pandas ###
df = pd.read_csv('assets\KPdata.csv')
FFdata = df  #create a copy of the dataframe for testing#

##Requirement 2.1 remove null values ###
##Delete 2020 because NO TOURNAMENT due to COVID-19##
###Delete the 4 rows where the 2020 Final Four teams woud have been###
FFdata = FFdata[FFdata.Year != 2020]  

#Requirement 1.1 create a dictionary ##
conf_abbrev = {
    "ACC": "Atlantic Coastal",
    "AMR": "American",
    "B10": "Big 10",
    "B12": "Big 12",
    "BGE": "Big East",
    "COL": "Colonial",
    "HOR": "Horizon",
    "MVC": "Missouri Valley",
    "P12": "Pac 12",
    "SEC": "Southeastern",
    "WCC": "West Coast",
}
print('The Conference dictionary is\n')
print(conf_abbrev)


## Create a dataframe of only the National Champions (Champion = 1) ##
champions = FFdata.loc[FFdata['Champion'] == 1]  
print('\n')
print('The list of champions from 2002-2021 are\n') 
print(champions) 

## Find the Final Four team with the highest kenpom rating ## 
maxKPvalue = float(FFdata[['KPvalue']].max())
top_team = FFdata.loc[FFdata['KPvalue'] ==maxKPvalue]
print('\n\n\n The highest kenpom rated Final Four Team is')
print(top_team)
print('\n')

##Requirement 3.2---- 5 basic Panda Calculations ##

## 1) Sum KP rank of all Final Four Teams.....should be 628 from Sheets verification ##
sum_rank = FFdata['KPrank'].sum()
print('The sum of the KenPom rank for all Final Four Teams is\n')
print(sum_rank)
print('\n')

## 2) Median of KP rank of all Final Four teams....should be 5 from Sheets verification ##
median_rank = FFdata['KPrank'].median()
print('The median KP rank for all Final Four Teams is)')
print(median_rank)
print('\n')

## 3) Mean (average) KP rank of all Final Four teams...should be 7.85###
mean_rank = FFdata['KPrank'].mean()
print('The average kenpom rank for all Final Four Teams is') 
print(mean_rank)
print('\n')










