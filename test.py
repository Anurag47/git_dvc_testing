import pandas as pd
import os

d = {'col1':[1,2,3,4,5],'col2':['a','b','c','d','e']}   
df = pd.DataFrame(data=d)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
df.to_csv(os.path.join(data_dir,'test.csv'),index=False)