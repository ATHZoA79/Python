import matplotlib.pyplot as plt

# Pie chart
plt.title('')

x = [200, 300, 400 ,50]
explode = [0, 0, 0.1, 0]
labels = ['A', 'B', 'C', 'D']

plt.tight_layout()

plt.pie(x, labels=labels, explode=explode)
plt.show()