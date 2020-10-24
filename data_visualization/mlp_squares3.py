import matplotlib.pyplot as plt
from math import sin

x = 1
y = 1

squares = []

# while x < 30:
#     # print(y)
#     squares.append(y)
#     x += 2
#     y += x

squares = [sin(n) for n in range(1, 100)]
fig, ax = plt.subplots()
ax.plot(squares)

plt.show()
