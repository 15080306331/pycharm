import numpy as np  # 导入依赖
x = np.array([10, 20, 30, 40, 50, 60], dtype=np.int8)  # dtype是设置ndarray的类型
#  警示 numpy 的 ndarray 中的数据类型必须一样
y_1 = np.array([60, 70, 80, 90, 100, 110], dtype=np.int8)
# 上面是创建类似x 的 ndarray 数组 的一种方式
# 更加简便的方式
y_2 = np.arange(60, 120, 10)  # numpy 中的 arange 是一个类似range()的function(函数)
#  range 视觉列表
#  np.arange(起始位置， 结束为止， 步长)
print("x数组：", x)  # 展示数组 x
print("y_1数组：",  y_1)  # 展示数组 y_1
print("y_2数组：",  y_2)  # 展示数组 y_2
print("两个数组是否相等", y_1 == y_2)  # 展示两个数组是否相同




# 数值计算


# 相加
z = x + y_1  # x 与 y_1 的想加结果
print("x + y_1 的相加结果：", z)
z = x + y_2  # x 与 y_2 的相加结果
print("x * y_2 的相加结果", z)


# 相减
z = x - y_1  # x 与 y_1 的想减结果
print("x * y_1 的相减结果：", z)
z = x - y_2  # x 与 y_2 的相乘结果
print("x * y_2 的相减结果", z)


# 相乘
z = x * y_1  # x 与 y_1 的想乘结果
print("x * y_1 的相乘结果：", z)
z = x * y_2  # x 与 y_2 的相乘结果
print("x * y_2 的相乘结果", z)


# 相除
z = x / y_1  # x 与 y_1 的想除结果
print("x * y_1 的相除结果：", z)
z = x / y_2  # x 与 y_2 的相除结果
print("x * y_2 的相除结果", z)




# 特殊的字符操作
z = y_1 > y_2
print("y_1 > y_2 的布尔值：", z)
# ......
























































