# 移动平均法
# 简单来说就是下一个元素的预测等于前 n个元素的平均值


def moving_average(data_array: list, n: int = 3):
    d = data_array[:n]
    while True:
        s = sum(d)
        elem = s / n
        d.pop(0)
        d.append(elem)
        yield elem  # 只有当调用 next的时候才会继续执行，否则停止在这里
