import matplotlib.pyplot as plt

x_label = []
for i in range(1, 9):
    x_label.append(i)
# print(x_label)

data_1 = [709,419,405,684,847,901,970,30]
data_2 = [213,645,64,707,493,254,834,927]
data_3 = [563,555,146,201,177,510,504,985]
labels = ['data_1', 'data_2', 'data_3']

# plt.pie(data_2)
plt.stackplot(x_label, data_1, data_2, data_3, labels=labels)
plt.legend(loc='upper left')
plt.show()