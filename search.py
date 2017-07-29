import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from create import *

print df

# print df.head()
# print df.tail(3)

print df.index
print df.columns
print df.values

print df.describe()
print df.T

print df.sort_index(axis=0,ascending=False)

print df.sort_values('A',ascending=False)