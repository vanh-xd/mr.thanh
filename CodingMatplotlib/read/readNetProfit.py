from matplotlib import pyplot as plt
import pandas as pd

plt.rcParams['figure.figsize'] = (10,8)
plt.rcParams['figure.dpi'] = 200
plt.rcParams['font.size'] = 13
#plt.rcParams['savefig.dpi'] = 200
# plt.rcParams['legend.fontsize'] = 'large'
# plt.rcParams['figure.titlesize'] = 'medium'
# plt.rcParams["legend.loc"] = 'best'

df = pd.read_csv('../dataset/netProfit.csv')
print(df)
plt.plot('Year', 'VNM', data = df)
plt.plot('Year', 'VIC', data = df)
plt.plot('Year', 'PNJ', data = df)
plt.plot('Year', 'VCB', data = df)
plt.show()

plt.plot('Year', 'VNM', data = df,color='b', linestyle = '-', marker='o')
plt.plot('Year', 'PNJ', data = df,color='g', linestyle = '--', marker='s')
plt.plot('Year', 'VCB', data = df,color='FF0000', linestyle = ':', marker='+')
plt.plot('Year', 'VIC', data = df,color='orange', linestyle = '-.', marker='*')
plt.title("Lợi nhuận của VNM, PNJ, VCB, VIC từ 2010 đến 2020", fontweight='bold')
plt.xlabel("Năm", fontweight='bold')
plt.ylabel("Lợi nhuận", fontweight='bold')
plt.legend()
plt.show()