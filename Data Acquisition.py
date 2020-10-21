import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

##note, use the data files from this repository, not the CAIT website, these are cleaned a bit(removed non ascii chars)

CO2_sub_sect = pd.read_csv('CAIT Country CO2 Emissions-Energy Sub-Sector.csv')
CO2_sub_sect.dropna()

#import co2 by country, drop rows with NAN values
CO2_country = pd.read_csv('CAIT Country CO2 Emissions.csv')
CO2_country  = CO2_country.dropna()

#import gdp, drop rows with more than one NAN value
GDP = pd.read_csv('CAIT Country Socio-Economic Data.csv')
GDP = GDP.dropna(thresh = 5)

#consider year 1960 and above
CO2_trim = CO2_country[CO2_country['Year'] > 1959].dropna()
GDP_trim = GDP[GDP['Year'] > 1959]
