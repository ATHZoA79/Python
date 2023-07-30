import pandas as pd

data = pd.read_csv('C:\Anthony\Pandas\day_11\data_table_1.csv', encoding='utf-8')

pd.set_option('display.unicode.east_asian_width', True)
# print(data.head(6))

# print(data.value_counts('年度'))
print(data.loc[0:(data.shape[0]-2), ['月份']])

print(data.shape)