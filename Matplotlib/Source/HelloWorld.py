import numpy as np
import matplotlib.pyplot
import matplotlib.pyplot as plt
x = np.arange(-1000, 1000)
y_tow_order = x**2
y_three_order = x**3
plt.figure(num=1, figsize=(10, 10), dpi=80)
plt.plot(x, y_tow_order)
plt.figure(num=2, figsize=(10, 10), dpi=80)
plt.plot(x, y_three_order)
plt.figure(num=3, figsize=(10, 10), dpi=80)
plt.plot(x, y_tow_order0)
plt.plot(x, y_three_order)
plt.show()
