
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import sklearn as sk
import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

##note, use the data files from this repository, not the CAIT website, these are cleaned a bit(removed non ascii chars)
CO2_sub_sect = pd.read_csv('CAIT Country CO2 Emissions-Energy Sub-Sector.csv')
CO2_sub_sect.dropna()
#import co2 by country, drop rows with NAN values
CO2_country = pd.read_csv('CAIT Country CO2 Emissions.csv')
CO2_country  = CO2_country.dropna()

#import co2 by country, drop rows with NAN values
CO2_country = pd.read_csv('CAIT Country CO2 Emissions.csv')
CO2_country  = CO2_country.dropna()

#import gdp, drop rows with more than one NAN value
GDP_full = pd.read_csv('CAIT Country Socio-Economic Data.csv')
GDP_full = GDP_full.dropna(thresh = 5)

#consider year 1960 and above
CO2 = CO2_country[CO2_country['Year'] > 1959].dropna()
GDP = GDP_full[GDP_full['Year'] > 1959]

# let concactenate the two so we can plot....
# select country, year, gdp-usd 2005, total co2 from gdp_Trim and co2_trim where co2_trim.year = gdp_trim.year
# and co2_trim.country = gdp_trim.country

concat = pd.merge(CO2,GDP,on = ['Year','Country'])
plt.scatter(concat['GDP-USD (Million US$ (2005))'],concat['Total CO2 Emissions Excluding Land-Use Change and Forestry (MtCO2)'])
plt.xlabel('GDP'); plt.ylabel('CO2');
plt.title('GDP vs CO2 Emissions')
plt.show()
#concat
#print(GDP_full)



##create concat dfs in loop
countries = GDP['Country'].values
countries = np.unique(countries)
country_dict={}
for i in range(countries.size):
    country_name = countries[i]
    push_back = concat[concat['Country'] == country_name]
    country_dict[country_name] = push_back
    
 #sample how to plot scatters in loop...
sample = ['Afghanistan','Chile','United States']
for i in range(3):
    temp_country = sample[i]
    plt.scatter(country_dict[temp_country]['GDP-USD (Million US$ (2005))'],country_dict[temp_country]['Total CO2 Emissions Excluding Land-Use Change and Forestry (MtCO2)'])
    plt.xlabel('gdp');plt.ylabel('co2');
    plt.title(temp_country)
    plt.show()


#this is problematic, idea: loop through the health country names and check if they match any gdp country names, if so continue, if not drop the row from health
HEALTH = pd.read_csv('NHA.csv')
#HEALTH = HEALTH.drop(HEALTH.index[0])
HEALTH = HEALTH.sort_values(by=['Countries'])
countries_fromhealth = HEALTH['Countries'].values
#print(countries_fromhealth.size)
num_matches= 0
ismatch = False
for i in range(countries_fromhealth.size):
    ismatch = False
    for j in range(countries.size):
        if(countries[j] == countries_fromhealth[i]):
            num_matches = num_matches +1
            countries_fromhealth[i] = countries[j]
            ismatch = True
    if(ismatch == False):
        HEALTH.drop(HEALTH.index[HEALTH['Countries']==countries_fromhealth[i]], axis=0,inplace=True)
        print('dropped')
        
    