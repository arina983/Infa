import matplotlib.pyplot as plt
import math
import numpy as np

# Дано:
A = 0.5  # амплитуда, мкКл
beta = 10  # коэффициент затухания, 1/с (увеличен для наглядности)
omega = 10 * math.pi  # частота, рад/с (уменьшена для наглядности)
T = 2 * math.pi / omega  # период колебаний, с

# Время (от 0 до 10 периодов)
t = np.linspace(0, 10 * T, 1000)

# Уравнение затухающих колебаний
q = A * np.exp(-beta * t) * np.cos(omega * t)

# Построение графика
plt.figure(figsize=(11, 6))
ax = plt.gca()
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['top'].set_color('none')
ax.grid(alpha=0.5)
plt.plot(t, q, label='$q(t) = 0.5 e^{-10 t} \cos(10 \pi t)$', color='red')

# Ограничение осей
plt.xlim(0, 10 * T)  # График до 10 периодов в секундах
plt.ylim(-0.5, 0.5)  # Увеличен диапазон оси y для наглядности
plt.title('График зависимости заряда от времени')
plt.xlabel('t, секунд')  # Время в секундах
plt.ylabel('q, мкКл')
plt.grid(True)
plt.legend()
plt.show()