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
concat
print(GDP_full)

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
plt.show()
concat2

#GDP for Brazil
concat3 = pd.merge(CO2_sub_sect,GDP, on = ['Year','Country'])
Chile = concat[concat['Country'] == 'Chile']
plt.scatter(Chile['GDP-USD (Million US$ (2005))'],Chile['Total CO2 Emissions Excluding Land-Use Change and Forestry (MtCO2)'])
plt.xlabel('Chile gdp');plt.ylabel('Chile co2');
plt.title('Chile gdp vs co2')
plt.show()
concat3

#GDP for USA
concat4 = pd.merge(CO2_sub_sect,GDP, on = ['Year','Country'])
USA = concat[concat['Country'] == 'United States']
plt.scatter(USA['GDP-USD (Million US$ (2005))'],USA['Total CO2 Emissions Excluding Land-Use Change and Forestry (MtCO2)'])
plt.xlabel('USA gdp');plt.ylabel('USA co2');
plt.title('USA gdp vs co2')
plt.show()
concat4

#now lets load some healthcare expenditure data for Afghanistan
HEALTH = pd.read_csv('NHA.csv')
afghan_health= HEALTH[HEALTH['Countries'] == 'Afghanistan']
temp = afghan_health.T.drop(['Countries','Indicators',]); temp = temp.drop(temp.index[0]);
columns = [];
for i in range(18):
    columns.append('Afghanistan')
temp['Country'] = columns
temp.reset_index(level=0, inplace=True)
temp.columns =['Year','Healthcare Expenditure in Millions of USD', 'Country']
temp['Year'] = pd.to_numeric(temp['Year'])
concat5 = pd.merge(afghan,temp, on =['Year','Country'])
concat5
plt.scatter(concat5['Healthcare Expenditure in Millions of USD'],
            concat5['Total CO2 Emissions Excluding Land-Use Change and Forestry (MtCO2)'])
plt.xlabel('afghan healthcare $ in millions USD');plt.ylabel('afghan total co2');
plt.show()

#now lets load some healthcare expenditure data for Chile
HEALTH = pd.read_csv('NHA.csv')
Chile_health= HEALTH[HEALTH['Countries'] == 'Chile']
temp = Chile_health.T.drop(['Countries','Indicators',]);temp = temp.drop(temp.index[0]);
columns = [];
for i in range(18):
    columns.append('Chile')
temp['Country'] = columns
temp.reset_index(level=0, inplace=True)
temp.columns =['Year','Healthcare Expenditure in Millions of USD', 'Country']
temp['Year'] = pd.to_numeric(temp['Year'])
concat6 = pd.merge(Chile,temp, on =['Year','Country'])
temp_string = concat6['Healthcare Expenditure in Millions of USD'] 
plt.scatter(concat6['Healthcare Expenditure in Millions of USD'],
            concat6['Total CO2 Emissions Excluding Land-Use Change and Forestry (MtCO2)'])
plt.xlabel('Chile healthcare $ in millions USD');plt.ylabel('Chile total co2');
plt.show()

#now lets load some healthcare expenditure data for USA
HEALTH = pd.read_csv('NHA.csv')
USA_health= HEALTH[HEALTH['Countries'] == 'United States of America']
temp = USA_health.T.drop(['Countries','Indicators',]); temp = temp.drop(temp.index[0]);
columns = [];
for i in range(18):
    columns.append('United States')
    
temp['Country'] = columns
temp.reset_index(level=0, inplace=True)
temp.columns =['Year','Healthcare Expenditure in Millions of USD', 'Country']
temp['Year'] = pd.to_numeric(temp['Year'])
    
concat7 = pd.merge(USA,temp, on =['Year','Country'])
temp_string = concat7['Healthcare Expenditure in Millions of USD'] 
temp_healthexp =[]
cols = np.shape(temp_string)[0]
for i in range(cols):
    temp_healthexp.append(temp_string[i].replace(',',''))

concat7['Healthcare Expenditure in Millions of USD'] = temp_healthexp
plt.scatter(concat7['Healthcare Expenditure in Millions of USD'],
            concat7['Total CO2 Emissions Excluding Land-Use Change and Forestry (MtCO2)'])
plt.xlabel('USA healthcare $ in millions USD');plt.ylabel('USA total co2');
plt.show()

#linear regression for Afghanistan
X = DataFrame(np.c_[concat5['Population (People)'],concat5['GDP-USD (Million US$ (2005))'],concat5['Healthcare Expenditure in Millions of USD']],
                   columns =['Population','GDP','Healthcare Expenditure'])
X2=X.to_numpy()
Y = concat5['Total CO2 Emissions Excluding Land-Use Change and Forestry (MtCO2)'].values
X_train, X_test, Y_train, Y_test = train_test_split(X2, Y, test_size = 0.5)
print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)
lr = LinearRegression(fit_intercept=False)
lr.fit(X_train, Y_train)
y=lr.predict(X_test)
predicted=plt.plot(X_test[:,1],y,'r.',label='Predicted')
Training=plt.plot(X_train[:,1], Y_train, 'k.',label='Training')
plt.xlabel('GDP (Millions US$)')
plt.ylabel('CO2 Emissions (Mt CO2)')
plt.title('Training and Predicted Values for CO2 Emissions vs GDP for Afghanistan')
plt.legend()
plt.show()
print('\n')
print('SCORE FOR Population, GDP, Healthcare Expenditure')
print('----------------------')
print(lr.score(X_test, Y_test))

#linear regression for Chile
X = DataFrame(np.c_[concat6['Population (People)'],concat6['GDP-USD (Million US$ (2005))'],concat6['Healthcare Expenditure in Millions of USD']],
                   columns =['Population','GDP','Healthcare Expenditure'])
X2=X.to_numpy() 
Y = concat6['Total CO2 Emissions Excluding Land-Use Change and Forestry (MtCO2)'].values
X_train, X_test, Y_train, Y_test = train_test_split(X2, Y, test_size = 0.5)
print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)
lr = LinearRegression()
lr.fit(X_train, Y_train)
y=lr.predict(X_test)
predicted=plt.plot(X_test[:,1],y,'r.',label='Predicted')
Training=plt.plot(X_train[:,1], Y_train, 'k.',label='Training')
plt.xlabel('GDP (Millions US$)')
plt.ylabel('CO2 Emissions (Mt CO2)')
plt.title('Training and Predicted Values for CO2 Emissions vs GDP for Chile')
plt.legend()
plt.show()
print('\n')
print('SCORE FOR Population, GDP, Healthcare Expenditure')
print('----------------------')
print(lr.score(X_test, Y_test))

#linear regression for USA Healthcare
X = DataFrame(np.c_[concat7['Population (People)'],concat7['GDP-USD (Million US$ (2005))'],concat7['Healthcare Expenditure in Millions of USD']],
                   columns =['Population','GDP','Healthcare Expenditure'])
X2=X.to_numpy() 
Y = concat7['Total CO2 Emissions Excluding Land-Use Change and Forestry (MtCO2)'].values
X_train, X_test, Y_train, Y_test = train_test_split(X2, Y, test_size = 0.5)
print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)
lr = LinearRegression()
lr.fit(X_train, Y_train)
y=lr.predict(X_test)
predicted=plt.plot(X_test[:,1],y,'r.',label='Predicted')
Training=plt.plot(X_train[:,1], Y_train, 'k.',label='Training')
plt.xlabel('GDP (Millions US$)')
plt.ylabel('CO2 Emissions (Mt CO2)')
plt.title('Training and Predicted Values for CO2 Emissions vs GDP for US')
plt.legend()
plt.show()
print('\n')
print('SCORE FOR Population, GDP, Healthcare Expenditure')
print('----------------------')
print(lr.score(X_test, Y_test))


#Lets attempt to classify developing countries based on some known options, afhganistan and chile, ill add a categorical column
#to each of these
#concat6.head()
#concat7.head()
#maybe try taking average change in gdp, population, and healthcare to create one qualifying vector for each country
df = concat5
df['shifted_column_gdp'] = df['GDP-USD (Million US$ (2005))'].shift(1)
df['difference_gdp'] = df['GDP-USD (Million US$ (2005))'] - df['shifted_column_gdp']
df['difference_gdp'] = df['difference_gdp'].abs()
average_gdp_delta = df['difference_gdp'].mean()
df['shifted_column_pop'] = df['Population (People)'].shift(1)
df['difference_pop'] = df['Population (People)'] - df['shifted_column_pop']
df['difference_pop'] = df['difference_pop'].abs()
average_pop_delta = df['difference_pop'].mean()
df['Healthcare Expenditure in Millions of USD'] = df['Healthcare Expenditure in Millions of USD'].astype(str).astype(int)
df['shifted_column_exp'] = df['Healthcare Expenditure in Millions of USD'].shift(1)
df['difference_exp'] = df['Healthcare Expenditure in Millions of USD'] - df['shifted_column_exp']
df['difference_exp'] = df['difference_exp'].abs()
average_exp_delta = df['difference_exp'].mean()
data = [average_gdp_delta, average_pop_delta, average_exp_delta,0]
summary_afghan = pd.DataFrame(columns = ['gdp delta','pop delta','exp delta','is_developing'])
summary_afghan.loc[0] = data
print(summary_afghan.head())

df = concat6
df['shifted_column_gdp'] = df['GDP-USD (Million US$ (2005))'].shift(1)
df['difference_gdp'] = df['GDP-USD (Million US$ (2005))'] - df['shifted_column_gdp']
df['difference_gdp'] = df['difference_gdp'].abs()
average_gdp_delta = df['difference_gdp'].mean()
df['shifted_column_pop'] = df['Population (People)'].shift(1)
df['difference_pop'] = df['Population (People)'] - df['shifted_column_pop']
df['difference_pop'] = df['difference_pop'].abs()
average_pop_delta = df['difference_pop'].mean()
df['Healthcare Expenditure in Millions of USD'] = df['Healthcare Expenditure in Millions of USD'].astype(str).astype(int)
df['shifted_column_exp'] = df['Healthcare Expenditure in Millions of USD'].shift(1)
df['difference_exp'] = df['Healthcare Expenditure in Millions of USD'] - df['shifted_column_exp']
df['difference_exp'] = df['difference_exp'].abs()
average_exp_delta = df['difference_exp'].mean()
data = [average_gdp_delta, average_pop_delta, average_exp_delta,0]
summary_chile = pd.DataFrame(columns = ['gdp delta','pop delta','exp delta','is_developing'])
summary_chile.loc[0] = data
print(summary_chile.head())

df = concat7
df['shifted_column_gdp'] = df['GDP-USD (Million US$ (2005))'].shift(1)
df['difference_gdp'] = df['GDP-USD (Million US$ (2005))'] - df['shifted_column_gdp']
df['difference_gdp'] = df['difference_gdp'].abs()
average_gdp_delta = df['difference_gdp'].mean()
df['shifted_column_pop'] = df['Population (People)'].shift(1)
df['difference_pop'] = df['Population (People)'] - df['shifted_column_pop']
df['difference_pop'] = df['difference_pop'].abs()
average_pop_delta = df['difference_pop'].mean()
df['Healthcare Expenditure in Millions of USD'] = df['Healthcare Expenditure in Millions of USD'].astype(str).astype(int)
df['shifted_column_exp'] = df['Healthcare Expenditure in Millions of USD'].shift(1)
df['difference_exp'] = df['Healthcare Expenditure in Millions of USD'] - df['shifted_column_exp']
df['difference_exp'] = df['difference_exp'].abs()
average_exp_delta = df['difference_exp'].mean()
data = [average_gdp_delta, average_pop_delta, average_exp_delta,1]
summary_usa = pd.DataFrame(columns = ['gdp delta','pop delta','exp delta','is_developing'])
summary_usa.loc[0] = data
summary_usa.head()
