from utils.my_util import *
import pandas as pd
import numpy as np

#  read data

df = pd.read_csv(r"C:/Users/user/Desktop/tfx_wav/data/TXF_daily.csv")  # 下次記得修改路徑
df = df.rename(columns={'Unnamed: 0': 'time'})

# claen data
date = np.array(df['time'])
weekday = pd.Series(list(map(lambda x: d2weekd(x), date)))
df = pd.concat([df, weekday], axis=1)
df = df.rename(columns={0: 'wd'})
df = df.iloc[4:, :]  # 純一到五的資料
df = df.iloc[:5070]
close = np.array(df['Close'])

# sign dic
vector14_sign = []
for i in range(0, int(len(df) / 10)):
    tmp = list(close[(0 + 10 * i):(10 + 10 * i - 1)])
    if close[9 + 10 * i:10 + 10 * i] - close[8 + 10 * i:9 + 10 * i] > 0:
        tmp.append(1)
        vector14_sign.append(tmp)
    else:
        tmp.append(0)
        vector14_sign.append(tmp)

# create db
hist_db = []

for i in range(len(vector14_sign)):
    direction = str(vector14_sign[i][9])
    vec_wav = reshape_dif_vec(diff_vec(vector14_sign[i][:9]))
    hist_db.append(
        {"direction": "{}".format(direction), "vec_wav": vec_wav}
    )

# predict
tmp = np.array(db_sim_search([17485, 17323.64, 17227.18, 17219.94, 16982.11, 16858.77, 16661.36, 16826.27, 16375.4], hist_db))

qq = list(np.where(tmp > 0.8)[0])
print(len(qq))
count = 0
for i in qq:
    count += int(hist_db[i]['direction'])
print("pred: {}".format(count/len(qq)))
# print("real: "+hist_db[1]['direction'])
print('=======================')
print(qq)