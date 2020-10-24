import matplotlib.pyplot as plt

x = 1
y = 1

squares = []

# while x < 30:
#     # print(y)
#     squares.append(y)
#     x += 2
#     y += x

squares = [2**n for n in range(1, 30)]
fig, ax = plt.subplots()
ax.plot(squares)

plt.show()
