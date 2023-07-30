import pandas as pd 

data_object = {
    'first': ['Andy', 'Bard', 'Charles'],
    'last': ['Alpha', 'Beta', 'Beta'],
    'payment': [52000, 69000, 28000],
    'email': ['a@yahoo.com', 'b@yahoo.com', 'c@yahoo.com']
}

df = pd.DataFrame(data_object)
pd.set_option('display.unicode.east_asian_width', True)

filter_by_pay = (df['payment']>=40000)

# print(df.loc[~filter_by_pay])
print(df.rename(columns={
    'first': '名',
    'last': '姓',
    'payment': '薪資',
    'email': '電子郵件'
}))
# print(df.loc[:,['payment']].sum())

def upper_email(email):
    return email.upper()

df['email'] = df['email'].apply(upper_email)
print("===============\n",df)