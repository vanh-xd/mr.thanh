import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../dataset/PVD_Asset.csv')
print(df)

plt.bar("Year", "Liabilities", data=df)
plt.title("Nợ của PVD qua các năm")
plt.xlabel("Năm")
plt.ylabel("Nợ")
plt.show()

plt.barh('Year', 'Equity', data=df)
plt.title("Vốn của PVD qua các năm")
plt.xlabel("Vốn")
plt.ylabel("Năm")
plt.show()

plt.bar('Year', 'Liabilities', data=df, color='orange', label="Nợ")
plt.bar('Year', 'Equity', data=df, bottom='Liabilities', color='darkgreen', label="Vốn")
plt.title("Tài sản của PVD từ 2010-2020")
plt.xlabel("Năm")
plt.ylabel("Tỷ đồng")
plt.legend()
plt.show()

