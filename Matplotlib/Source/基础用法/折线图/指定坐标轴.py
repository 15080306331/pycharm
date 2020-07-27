import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-1000,1000)
y_tow_order = x**2
y_three_order = x**3
# y_four_order = x**4


plt.figure(num=1, figsize=(5, 5))  # 绘制二次函数,保存
plt.plot(x, y_tow_order)
plt.savefig(
    "E:/code/python/PyCharm-Data-analysis/Matplotlib/image/Specify_the_axis/Specify_the_axis/function/Quadratic_function.png"
)


plt.figure(num=2, figsize=(5, 5))  # 绘制三次函数,保存
plt.plot(x, y_three_order)
plt.savefig(
    "E:/code/python/PyCharm-Data-analysis/Matplotlib/image/Specify_the_axis/Specify_the_axis/function/Cubic_function.png"
)


plt.figure(num=3, figsize=(5, 5))
plt.plot(x, y_tow_order)
plt.plot(x, y_three_order)
plt.savefig(
    "E:/code/python/PyCharm-Data-analysis/Matplotlib/image/Specify_the_axis/Specify_the_axis/function/Quadratic_function&Cubic_function.png"
)


plt.show()