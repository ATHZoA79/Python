import matplotlib.pyplot as plt

x = [13, 14, 15, 16, 17]
y = [9510,50,4005,971,8524]

plt.plot(x, y, label='line-1')
plt.xlabel('X_Label')
plt.ylabel('Y_Label')
plt.title('Demo01')
plt.legend()
plt.xticks(x)
plt.show()