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


