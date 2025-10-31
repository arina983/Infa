import matplotlib.pyplot as plt
import math
import numpy as np

A = 0.5  
beta = 10
omega = 10 * math.pi  
T = 2 * math.pi / omega 

t = np.linspace(0, 10 * T, 1000)

q = A * np.exp(-beta * t) * np.cos(omega * t)

plt.figure(figsize=(11, 6))
ax = plt.gca()
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['top'].set_color('none')
ax.grid(alpha=0.5)
plt.plot(t, q, label='$q(t) = 0.5 e^{-10 t} \cos(10 \pi t)$', color='red')

plt.xlim(0, 10 * T) 
plt.ylim(-0.5, 0.5) 
plt.title('График зависимости заряда от времени')
plt.xlabel('t, секунд') 
plt.ylabel('q, мкКл')
plt.grid(True)
plt.legend()

plt.show()
