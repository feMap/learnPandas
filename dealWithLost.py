import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from select import *

df1 = df.reindex(index=dates[0:4],columns=list(df.columns) + ['E'])

df1.loc[dates[0]:dates[1],'E'] = 1

print df
print df1

print df1.dropna(how='any')

print df1.fillna(value=5)

print pd.isnull(df1)
