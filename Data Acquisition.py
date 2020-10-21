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
GDP_full = pd.read_csv('CAIT Country Socio-Economic Data.csv')
GDP_full = GDP.dropna(thresh = 5)

#consider year 1960 and above
CO2 = CO2_country[CO2_country['Year'] > 1959].dropna()
GDP = GDP[GDP['Year'] > 1959]

# let concactenate the two so we can plot....
# select country, year, gdp-usd 2005, total co2 from gdp_Trim and co2_trim where co2_trim.year = gdp_trim.year
# and co2_trim.country = gdp_trim.country
concat = pd.merge(CO2,GDP,on = ['Year','Country'])
plt.scatter(concat['GDP-USD (Million US$ (2005))'],concat['Total CO2 Emissions Excluding Land-Use Change and Forestry (MtCO2)'])
plt.xlabel('GDP'); plt.ylabel('CO2');
plt.title('GDP vs CO2 Emissions')
plt.show()
concat
#Clear linear relationship between co2 and gdp, what about others?
plt.scatter(concat['Population (People)'],concat['Total CO2 Emissions Excluding Land-Use Change and Forestry (MtCO2)'])
plt.xlabel('population');plt.ylabel('co2');
plt.title('pop vs co2')
plt.show

#similar relationship between co2 and population..
