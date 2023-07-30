import pandas as pd 
import json 

data_object = {
    'first': ['Andy', 'Bard', 'Charles'],
    'last': ['Alpha', 'Beta', 'Beta'],
    'email': ['a@yahoo.com', 'b@yahoo.com', 'c@yahoo.com']
}

df = pd.DataFrame(data_object)

filtered = (df['last'] != 'Beta')
# print("====Filtered====\n", filtered)
# print("====Filtered is True====\n", df[filtered])
# print("====Filtered Email====\n", df.loc[filtered, 'email'])