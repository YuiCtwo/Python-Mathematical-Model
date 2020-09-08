# ARMA 模型的应用对象应为平稳序列

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.gofplots import qqplot
from statsmodels.tsa import stattools
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARMA
import math


def test_stationary(var):
    var.plot()
    data = np.array(var["production"].values)
    return adfuller(data)


df = pd.read_csv("production.csv", index_col="year")
df_original = pd.read_csv("production.csv", index_col="year")
# ------------------------第一步进行平稳性检验
# test_stationary(df)
# 第一次验证后发现数据并不平稳，需要我们首先进行平稳性处理

# ------------------------第二步平稳性处理
# 取 log再进行平稳性检验
# 对数据的一列进行处理, pd 使用 apply方法
# axis=1，表示每次取一行数据进行处理，按行处理
# 方法名为单独的方法名，可以处理传入的 x数据
# x为每一行的数据，做为方法的参数 1 x中的数据可以用【x.列名】来获取
# 参数 2等为方法需要的其他参数，不需要可以不写
df["production"] = df.apply(lambda x: np.log(x["production"]), axis=1)
# test_stationary(df)
# 还是不行，再进行差分处理
df["production"] = df["production"].diff()
df["production"].dropna(inplace=True)  # 删去 NaN的值
# 再进行检验k, 还是不行，再做一次差分处理
df["production"] = df["production"].diff()
df.dropna(inplace=True)
# result = test_stationary(df)
# print(result)
# plt.show()
# 根据检验可以认为是平稳的了

# ------------------------第三步模拟定阶和拟合
# 常用的有根据 ACF和 PACF结果的观察来定阶和暴力定阶
# 由于阶数一般不会很大，在数据量也不大的情况下，暴力定阶是个不错的选择。
# 暴力定阶通过遍历可能的阶数，找到 aic, bic, hqic最小的值，作为最优阶数
order = stattools.arma_order_select_ic(df["production"].values, max_ar=3, max_ma=3,
                                       ic=["aic", "bic", "hqic"])
bic_min = order.bic_min_order
print(order.bic_min_order)
# 拟合
model = ARMA(df, bic_min).fit()

# ----------------------第四步白噪声检验
# QQ图检验，DW检验
resid = model.resid
# fig = plt.figure(figsize=(6, 6))
# ax = fig.add_subplot(111)
# fig = qqplot(resid, line="q", ax=ax, fit=True)
# plt.show()

# DW检验，如果值接近 2，认为系列不存在一阶相关性
# print(sm.stats.durbin_watson(resid.values))

# --------------------------第五步预测
predictions = model.predict(start=0, end=50)  # 预测值补充没有的数据
print(predictions.index)
predictions.index = predictions.index + 1954
# 绘制预测序列和原序列进行对比
# plt.figure(figsize=(24, 8))
# plt.plot(df, color="blue", label="Original")
# plt.ylim((-0.3, 0.3))
# plt.plot(predictions, color="red", label="Predictions")
# plt.legend(loc="best")
# plt.show()

# ---------------------------第六步将平稳化序列还原为原序列

predict = {}
# 二阶还原 f(x) = p(x) - f(x-2) + 2*f(x-1)
for i, v in enumerate(predictions):
    if i < 1:
        pass
    try:
        predict[i+1954] = v - df_original["production"].values[i-1] + 2*df_original["production"].values[i]
    except IndexError or KeyError:
        pass
# predict_log = predictions.sub(df.shift(2))
# predict_log = predict_log.add(df.shift(1))
# predict_log = predict_log.add(df.shift(1))
predict[1998] = predictions[1998] + 2*df_original["production"][1997] - df_original["production"][1996]
for k in predict:
    predict[k] = math.exp(predict[k])

print(predict)