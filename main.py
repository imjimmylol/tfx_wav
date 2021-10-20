import pandas as pd
import numpy as np
from utils.my_util import *

#  read data

df = pd.read_csv(r"C:/Users/user/Desktop/v3/data/TXF_daily.csv")
df = df.rename(columns={'Unnamed: 0': 'time'})

# claen data
date = np.array(df['time'])
weekday = pd.Series(list(map(lambda x: d2weekd(x), date)))
df = pd.concat([df, weekday], axis=1)
df = df.rename(columns={0: 'wd'})
df = df.iloc[4:, :] # 純一到五的資料
df = df.iloc[:5070]
close = np.array(df['Close'])

# sign dic
vector14_sign = []
for i in range(0, int(len(df)/10)):
  tmp = list(close[(0+10*i):(10+10*i-1)])
  if close[9+10*i:10+10*i] - close[8+10*i:9+10*i] > 0:
    tmp.append(1)
    vector14_sign.append(tmp)
  else:
    tmp.append(0)
    vector14_sign.append(tmp)

# db
hist_db = []

for i in range(0, int(len(df)/10)):
  direction = str(vector14_sign[i][9])
  hist_db.append({"direction": "{}".format(direction), "vec_wav": reshape_db(tangent_vc(df, "Close"))[0+10*i:10+10*i]})


