import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from create import *

# print df['A']
# print df.A

# print df[0:3]
# print df['20130103':'20130106']

# print dates[0]
# print df.loc[dates[0]]

# print df.loc[dates[1:3],['A','B']]

# print df.loc[dates[0],'A']
# print df.at[dates[0],'A']

# print df.iloc[3:5]
# print df.iloc[3:5,0:2]
# print df.iloc[[1,2,4],[0,2]]

# print df.iloc[1,1]
# print df.iat[1,1]

# BULL
# print df[df.A > 0]
# print df[df > 0]

df2 = df.copy()
df2['E'] = ['one','one','two','three','four','three']

# print df2

# isin function to filter the data
# print df2[df2['E'].isin(['two','four'])] 

s1 = pd.Series([1,2,3,4,5,6],index=pd.date_range('20130102',periods=6))
# print s1

df['F'] = s1

# print df

df.at[dates[0],'A'] = 0
df.iat[0,1] = 0
df.loc[:,'D'] = np.array(5*len(df))

# print df

df2 = df.copy()
df2[df2 > 0] = -df2

# print df2


