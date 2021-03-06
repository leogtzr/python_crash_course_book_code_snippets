import matplotlib.pyplot as plt

x = 1
y = 1

squares = []

while x < 10:
    # print(y)
    squares.append(y)
    x += 2
    y += x

plt.style.use('seaborn')

fig, ax = plt.subplots()

# Scatter values:
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

ax.scatter(x_values, y_values, s=200)
ax.plot([1, 2, 3, 4, 5], squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square numers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
