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

