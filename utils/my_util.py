import numpy as np
import datetime
from datetime import datetime


def d2weekd(date):
    d = {0: '一', 1: '二', 2: "三", 3: "四", 4: "五", 5: "六", 6: '日'}
    return d[datetime.strptime('{}'.format(date), "%Y-%m-%d").weekday()]


def tangent_vc(df, colname):
    y = list(df["{}".format(colname)].diff().dropna())
    x = np.ones((1, len(y))).tolist()[0]
    return [x, y]


def reshape_db(data):  # [ [x1,x2...],[y1,y2...] ] to [[x1,y1],[x2,y2]....[xn,yn]]
    res = []
    for i in range(500):
        tmp = [data[0][i], data[1][i]]
        res.append(tmp)
    return np.array(res)


def cos_sim(v1, v2):  # v1 v2 須為np.array
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def wav_sim(wav1, wav2):
    res = 0
    for i in range(len(wav1)):
        tmp = cos_sim(wav1[i], wav2[i])
        res += tmp
    return res / len(wav1)

