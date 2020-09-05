from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 多元线性回归分析
# 尝试分析体温和心率之间的关系
origin_df = pd.read_csv("test.csv")
df = pd.DataFrame(origin_df, columns=["Temperature", "HeartRate"])
print(df.head())
# 绘制一个散点图
plt.scatter(df["Temperature"], df["HeartRate"])
plt.xlabel("Temperature")
plt.ylabel("Heart Rate")
print("相关系数:\n", df.corr())

# reshape如果行数 =-1的话可以使我们的数组所改的列数自动按照数组的大小形成新的数组
#因为 model需要二维的数组来进行拟合但是这里只有一个特征所以需要 reshape 来转换为二维数组

temperature_data = list(df["Temperature"].values)
temperature_data = np.array([temperature_data]).reshape(-1, 1)
reg = LinearRegression()
reg.fit(temperature_data, df["HeartRate"])
print("回归系数:", reg.coef_)
print("截距:", reg.intercept_)
y_predict = reg.predict(temperature_data)
# 绘图
plt.plot(df["Temperature"], y_predict, color="black", linewidth=3, label="prediction")
plt.legend(loc="best")

# R方决定系数评估模型精准度
score = reg.score(temperature_data, df["HeartRate"])
print(score)  # R方很低，加上前面的相关系数很小，可以认为 2者不存在明显的线性相关性
plt.show()
