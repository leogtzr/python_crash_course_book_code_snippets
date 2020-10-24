import matplotlib.pyplot as plt

x = 1
y = 1

squares = []

while x < 30:
    # print(y)
    squares.append(y)
    x += 2
    y += x

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# Set chart title and label axes.


plt.show()
