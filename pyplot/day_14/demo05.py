import pandas as pd 
import os.path as path
import matplotlib.pyplot as plt

data = pd.read_csv('pyplot\day_14\play.csv')
current_path = path.curdir
print(current_path)

# print(data)
# plt.plot(data['year'], data['usa'], label='USA')
# plt.plot(data['year'], data['tw'], label='Taiwan')

labels = {
    'usa': 'USA',
    'tw': 'Taiwan',
    'jp': 'Japan',
    'hk': 'HongKong'
}
for country in data:
    if country in labels:
        plt.plot(data['year'], data[country], marker='*', label=labels[country])

plt.legend()
plt.show()