import pandas as pd
import matplotlib.pyplot as plt

dat = pd.read_csv('../dataset/Salary_of_Developer.csv')
print(dat)

plt.boxplot(dat)
plt.ylabel("Lương (triệu đồng)")
plt.title("Boxplot thể hiện phân bổ mức lương Lập trình viên")
plt.show()

orange_square = dict(markerfacecolor='orange', marker='s')
plt.boxplot(dat, notch=True, flierprops=orange_square, vert=False)
plt.xlabel("Lương (triệu đồng)")
plt.title("Boxplot thể hiện phân bổ mức lương Lập trình viên")
plt.show()

plt.subplot(rows, columns, index)