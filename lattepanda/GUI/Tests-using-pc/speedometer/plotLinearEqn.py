import matplotlib.pyplot as plt
import numpy as np

x = [0, 220]
y = [224, -42]

X = [arc for arc in range(0, 221, 1)]
# Y = [speed for speed in range(224, -43, -1)]
Y = []


def linear_equation(X):
    for x in X:
        Y.append(((-133.0 / 110.0) * x) + 224.0)


linear_equation(X)

# print(X)
# print(Y)

# print(x)
# print(y)


plt.title("A linear relationship between the Arc(degrees) and the speed(km/h)")
plt.text(142, 160, "Y=(-1.21)X + 224", fontsize=18, horizontalalignment='center',
         verticalalignment='center', bbox=dict(facecolor='blue', alpha=0.5))

plt.ylabel("Arc in Degrees")
plt.xlabel("Speed in km/h")

# plt.plot(X, Y, "r+")
plt.plot(x, y)

plt.show()
