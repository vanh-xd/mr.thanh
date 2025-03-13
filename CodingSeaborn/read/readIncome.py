import pandas as pd
import seaborn as sns
import ssl

dat = pd.read_csv('../dataset/Income.csv')
print(dat)

sns.relplot(x='Income', y='Expenditure', data=dat, kind = 'scatter')

sns.regplot(x='Income', y='Expenditure', data=dat)

flights_long = sns.load_dataset("flights")
flights = flights_long.pivot("month", "year", "passengers")

sns.jointplot(x='Income', y='Expenditure', data=dat, color = 'orange')

sns.pairplot(df[['Income', 'Expenditure']])