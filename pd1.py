# %%
import pandas as pd
import numpy as np
data = pd.read_csv('earthquakes.csv', sep=',')
data.head()


# %%
len(data[(data['type'] == 'explosion') & (data['magType'] == 'ml')])
# %%
alas = data.title.str.contains("Alaska")
split_dis = data[alas].title.str.split(" ", expand=True)
dis = dis[split_dis[3].str.len() < 5]
data.iloc[dis.index].mag.mean()


# %%
quar = pd.to_datetime(data.time, unit='ms')
data['quarter'] = quar.dt.quarter
pd.pivot_table(data, values='mag', index=['quarter'],
               aggfunc=np.mean)
