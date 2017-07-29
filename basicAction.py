import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from select import *

print df
print df.mean()
print df.mean(1)

s = pd.Series([1,3,5,np.nan,6,8],index=dates).shift(2)
print s

print s.values

print df.sub(s,axis='index')

print df
print df.apply(np.cumsum)
print df.apply(lambda x:x.max()-x.min())

# hist plot
s = pd.Series(np.random.randint(0,7,size=100))
print s
print s.value_counts()

# str
s = pd.Series(['A','B','C','Aaba','Baca',np.nan,'CABA','dog','cat'])

print s
print s.str.lower()
