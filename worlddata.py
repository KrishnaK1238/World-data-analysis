import pandas as pd
import numpy as np

w_data = pd.read_csv('world_data_2023.csv')
w_data.drop_duplicates(inplace = True)
for y in w_data['Co2_Emissions(tons)']:
    if ',' in str(y):
        w_data['Co2_Emissions(tons)']= w_data['Co2_Emissions(tons)'].str.replace(',','')
    else:
        pass
w_data.to_csv('world_data_2023.csv')