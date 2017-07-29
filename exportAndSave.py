# coding: utf-8

import numpy as np
import pandas as pd

ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))

df = pd.DataFrame(np.random.randn(1000,4),index=ts.index,columns=['A','B','C','D'])


# csv
df.to_csv('foo.csv')
print pd.read_csv('foo.csv')

# hdf5
df.to_hdf('foo.h5','df')
print pd.read_hdf('foo.h5','df')

# excel
df.to_excel('foo.xlsx',sheet_name='Sheet1')
print pd.read_excel('foo.xlsx','Sheet1',index_col=None,na_values=['NA'])
