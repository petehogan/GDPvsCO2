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
summary_afghan.head()

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
summary_chile.head()

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
data = [average_gdp_delta, average_pop_delta, average_exp_delta,0]
summary_usa = pd.DataFrame(columns = ['gdp delta','pop delta','exp delta','is_developing'])
summary_usa.loc[0] = data
summary_usa.head()
