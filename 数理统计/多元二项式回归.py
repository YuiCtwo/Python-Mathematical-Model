# sklearn 里面支持的回归方法
# # 建立贝叶斯岭回归模型
# br_model = BayesianRidge()
# # 弹性网络回归模型
# etc_model = ElasticNet()
# # 支持向量机回归
# svr_model = SVR()
# # 梯度增强回归模型对象
# gbr_model = GradientBoostingRegressor()

# 这和我们的多元二项式回归没啥联系
# 多元二项式回归方法
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pandas as pd

quadratic_model = PolynomialFeatures(degree=2)
# 简单解释一下这个的几个常用的参数
# degree: 最高次数
# interaction_only: 是否只含有交叉项，官方解释如下:
# if an input sample is two dimensional and of the form[a, b],
# the degree-2 polynomial features are[1, a, b, a ^ 2, ab, b ^ 2]
# interaction_only=true, 就表示拟合模型为交叉模型(interaction)
# interaction_only=false(默认) 就表示拟合模型是完全二次模型

origin_df = pd.read_csv("test2.csv")
# dataframe获取多列数据的方法
X = origin_df[["x_data1", "x_data2", "x_data3"]].values
Y = origin_df["y_data"].values
# 转换为线性多参数的回归问题，多了各种交叉项的值
x_poly = quadratic_model.fit_transform(X)

# 下面和线性回归一样
liner_model = LinearRegression()
liner_model.fit(x_poly, Y)
print(quadratic_model.get_feature_names())
# 回归系数与前面的名字上面的对应
print("回归系数:", liner_model.coef_)
# 截距为多项式常数项
print("截距:", liner_model.intercept_)

# Pipeline 封装简化代码
# from sklearn.linear_model import LinearRegression
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import StandardScaler
#
# poly_reg = Pipeline(degree)([ #这里将三个处理步骤进行了封装，将数据传入poly_reg之后，将会智能地沿着该管道进行处理
#     ("poly",PolynomialFeatures(degree=degree))，
#     ("std_scaler",StandardScaler())，
#     ("lin_reg",LinearRegression())
# ])