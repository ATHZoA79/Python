import matplotlib.pyplot as plt 

x = [1, 2, 3, 4]
y = [120, 95, 73, 162]

plt.title("Report")
plt.rc('axes', titlesize=20)
plt.rc('axes', labelsize=16)
plt.xlabel('X Label')
plt.plot(x, y)
# plt.plot_date(x, y)
# plt.pie(x, y)
plt.show()