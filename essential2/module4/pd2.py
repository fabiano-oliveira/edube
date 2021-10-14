import pandas as pd 
import json
import io

content = { 'data': 'key=XkrSa, age=58, key=aKeot, age=64, key=1errg, age=12' } 
print(content)

df = pd.DataFrame([content])
sage = df['data'].str.extractall(r"age=(?P<age>\d+)").astype(int)

print(sage.head())
print(df.head())
print(df['data'])

x = sage.loc[sage['age'] > 60]
print(x)