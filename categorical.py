# coding: utf-8

import numpy as pd
import pandas as pd

df = pd.DataFrame({'id':[1,2,3,4,5,6],'raw_grade':['a','b','b','a','e','e']})

df['grade'] = df['raw_grade'].astype('category')

print df

print df['grade']

df['grade'].cat.categories = ['very bad','good','very good']

print df['grade']

df['grade'] = df['grade'].cat.set_categories(['very bad','bad','medium','good','very good'])

print df['grade']

# 新版本的pandas中采用的sort_values而不是sort
# 排序按照的是Categorical的顺序而不是字典中的顺序
print df.sort_values('grade')

print df.groupby('grade').size()