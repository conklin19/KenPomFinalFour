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
