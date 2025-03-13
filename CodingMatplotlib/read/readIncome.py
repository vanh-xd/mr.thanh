import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../dataset/Income.csv')
print(df)

plt.scatter('Income', 'Expenditure', data =df, color = 'darkgreen')
plt.xlabel('Income', fontweight = 'bold')
plt.ylabel('Expenditure', fontweight = 'bold')
plt.show()

dat = np.random.normal(12, 2, 400)
plt.hist(dat, color='darkgreen', edgecolor='orange')
plt.xlabel('Lương')
plt.ylabel('Tần suất')
plt.show()
