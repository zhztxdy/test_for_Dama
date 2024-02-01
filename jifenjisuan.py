import math
from scipy.integrate import quad

# 定义函数 f(x)
def f(x):
    return 3.775 - (3.775 - 3.75)*x

# 定义积分区间 [a, b]
a = 0
b = 1

# 计算旋转体积
result, _ = quad(lambda x: math.pi * f(x)**2, a, b)

# 输出结果
print("旋转体积的值为：", result)