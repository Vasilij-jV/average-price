import matplotlib.pyplot as plt

# Создаем данные для графика
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Строим график
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')
plt.grid(True)
plt.show()