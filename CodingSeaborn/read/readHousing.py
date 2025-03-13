import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../dataset/Housing.csv')
dat = df.sample(400)
sns.scatterplot(x = 'housing_median_age', y = 'median_house_value',
                data = dat, hue = 'ocean_proximity', size = 'median_income')

dat = df.sample(500)
sns.catplot(x = 'ocean_proximity', y = 'median_house_value', data = dat)

dat = df.sample(500)
sns.catplot(x = 'ocean_proximity', y = 'median_house_value', data = dat, kind = 'box')

dat = df.sample(500)
sns.catplot(x = 'ocean_proximity', y = 'median_house_value', data = dat, kind = 'point')

np.random.seed(0)
dat = np.random.normal(12,2,400)
sns.displot(dat)
plt.xlabel('Salary')
sns.displot(dat, kde = True, color = 'r')
plt.xlabel('Salary')