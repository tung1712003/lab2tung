
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 20)
y = 2*x

fig = plt.figure(figsize=(12, 7))
plt.plot(x, y, alpha=0.5, label='y = 2x',
		color='red', linestyle='-',
		linewidth=1, marker='+',
		markersize=10, markerfacecolor='blue',
		markeredgecolor='blue')

plt.title('Linear Equation PLot')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.grid(alpha=.6, linestyle='--')
plt.legend()
plt.show()
