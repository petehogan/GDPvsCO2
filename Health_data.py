#now lets load some healthcare expenditure data

#from here https://apps.who.int/nha/database/ViewData/Indicators/en
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import sklearn as sk
import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

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
#Clear linear relationship between co2 and gdp, what about others?
plt.scatter(concat['Population (People)'],concat['Total CO2 Emissions Excluding Land-Use Change and Forestry (MtCO2)'])
plt.xlabel('population');plt.ylabel('co2');
plt.title('pop vs co2')
plt.show

#check just afghanistan
concat2 = pd.merge(CO2_sub_sect,GDP, on = ['Year','Country'])
afghan = concat[concat['Country'] == 'Afghanistan']
plt.scatter(afghan['GDP-USD (Million US$ (2005))'],afghan['Total CO2 Emissions Excluding Land-Use Change and Forestry (MtCO2)'])
plt.xlabel('afghan gdp');plt.ylabel('afghan co2');
plt.title('afghan gdp vs co2')
concat2

#now lets load some healthcare expenditure data
HEALTH = pd.read_csv('NHA.csv')
afghan_health= HEALTH[HEALTH['Countries'] == 'Afghanistan']
temp = afghan_health.T.drop(['Countries','Indicators',]); temp = temp.drop(temp.index[0]);
#print(temp)
columns = [];
for i in range(18):
    columns.append('Afghanistan')
    
temp['Country'] = columns
temp.reset_index(level=0, inplace=True)
temp.columns =['Year','Healthcare Expenditure in Millions of USD', 'Country']
temp['Year'] = pd.to_numeric(temp['Year'])
concat3 = pd.merge(afghan,temp, on =['Year','Country'])
concat3
plt.scatter(concat3['Healthcare Expenditure in Millions of USD'],
            concat3['Total CO2 Emissions Excluding Land-Use Change and Forestry (MtCO2)'])
plt.xlabel('afghan healthcare $ in millions USD');plt.ylabel('afghan total co2');
plt.show()
concat3

#linear regression with sklearn
X = DataFrame(np.c_[concat3['Population (People)'],concat3['GDP-USD (Million US$ (2005))'],concat3['Healthcare Expenditure in Millions of USD']],
                   columns =['Population','GDP','Healthcare Expenditure'])

Y = concat3['Total CO2 Emissions Excluding Land-Use Change and Forestry (MtCO2)'].values
Y
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.5)
lr = LinearRegression()
lr.fit(X_train, Y_train)
print('\n')
print('SCORE FOR Population, GDP, Healthcare Expenditure')
print('----------------------')
print(lr.score(X_test, Y_test))
#plt.scatter(X_test,Y_test)
Y_pred = lr.predict(X_test)
Y_pred

