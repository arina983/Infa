import matplotlib.pyplot as plt
import math
import numpy as np

# Дано:
A = 0.5  # амплитуда, мкКл
beta = 0.1  # коэффициент затухания, 1/с
omega = 100000 * math.pi  # частота, рад/с
T = 2 * math.pi / omega  # период колебаний, с

# Время (от 0 до 2 периодов)
t = np.linspace(0, 10 * T, 10000)

# Уравнение затухающих колебаний
q = A * np.exp(-beta * t) * np.cos(omega * t)

# Построение графика
plt.figure(figsize=(11, 6))
ax = plt.gca()
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['top'].set_color('none')
ax.grid(alpha=0.5)
plt.plot(t, q, label='$q(t) = 0.5 e^{-0.1 t} \cos(10^4 \pi t)$', color='red')

# Ограничение осей
plt.xlim(0, 10 * T)  # График до двух периодов в секундах

plt.title('График зависимости заряда от времени')
plt.xlabel('t, секунд')  # Время в секундах
plt.ylabel('q, мкКл')
plt.grid(True)
plt.legend()
plt.show()