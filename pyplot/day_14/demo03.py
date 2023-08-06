import pandas as pd
import matplotlib.pyplot as plt 

x_label = []
for i in range(1, 9):
    x_label.append(i)
data_1 = [709,419,405,684,847,901,970,30]

plt.hist(data_1, bins=1000, density=1, edgecolor='r')
# bins 切分數量，以切分範圍資料統計為一個數據
plt.axvline(500, 0, 100, color='g')
# axvline 直線， axhline 橫線

plt.legend()
plt.show()