import numpy as np
import matplotlib.pyplot as plt

# Дано:
m = 0.1  
k = 20 
A = 0.05  
omega = np.sqrt(k / m) 
phi_0 = 0.703 
T = 2 * np.pi / omega  

t = np.linspace(0, 2 * T, 1000)

E_pot = 0.5 * k * A**2 * np.cos(omega * t + phi_0)**2

E_max = 0.5 * k * A**2

plt.figure(figsize=(11, 6))
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.grid(alpha=0.5)
plt.plot(t, E_pot, label=r'$E_{\text{пот}}(t) = \frac{1}{2} k A^2 \cos^2(\omega t + \varphi_0)$', color='orange')

# Ограничение осей
plt.xlim(0, 2 * T)  
plt.ylim(0, E_max)
plt.title('График зависимости потенциальной энергии от времени')
plt.xlabel('t, секунд')
plt.ylabel('E, Дж')
plt.grid(True)
plt.legend()

plt.show()
