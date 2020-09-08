# ARIMA 模型
# 将非平稳数据采用差分方法变得平稳，然后再进行计算

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa import stattools
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import adfuller


def test_stationary(var):
    var.plot()
    data = np.array(var["production"].values)
    return adfuller(data)


df = pd.read_csv("production.csv", index_col="year")
df_diff = df.diff()
df_diff.dropna(inplace=True)
r = test_stationary(df_diff)


# 白噪声检验, 除了采取 QQ图和 DW检验，还可以直接用库方法检验(LB检验)
print(u'差分序列的白噪声检验结果：', acorr_ljungbox(df_diff, lags=1))
# 打印结果的第一个是 LB统计量，第二个是 LB p值，p值下降到 0.05置信度以下时，可以认为出现显著的自回归关系
# plt.show()

pmax = int(len(df_diff) / 10)  # 一般阶数不超过 length /10
qmax = int(len(df_diff) / 10)
bic_matrix = []
for p in range(pmax+1):
    temp = []
    for q in range(qmax+1):
        try:
            temp.append(ARIMA(df_diff, (p, 1, q)).fit().bic)
        except Exception:
            temp.append(None)
        bic_matrix.append(temp)

bic_matrix = pd.DataFrame(bic_matrix)
p, q = bic_matrix.stack().idxmin()   # 先使用stack 展平， 然后使用 idxmin 找出最小值的位置
print(u'BIC 最小的p值 和 q 值：%s,%s' % (p, q))
model = ARIMA(df_diff, (p, 1, q)).fit()
model.summary2()
model.forecast(10)  # 预测 10步后的数据
