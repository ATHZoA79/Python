import pandas as pd 
import json

data_object = {
    'first': ['Andy', 'Bard', 'Charles'],
    'last': ['Alpha', 'Beta', 'Ch'],
    'email': ['a@yahoo.com', 'b@yahoo.com', 'c@yahoo.com']
}

# print(json.dumps(data_object, indent=4))
# print(pd.DataFrame(data_object))
data_frame = pd.DataFrame(data_object)
# print(data_frame[['first', 'email']])
# print(data_frame.loc[[1,2], ['last', 'first']])