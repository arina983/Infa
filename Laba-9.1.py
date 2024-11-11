def func(x):
    return x**2 / (10 + x**3)
a = -2
b = 5

for n in [10, 100, 1000]:
    h = (b - a) / n
    sum = (func(a)+func(b))/2
    for i in range(1,n):
        sum += func(a + i*h)
    result = sum * h
    print(f"N={n}, Интеграл: {result:.4f}")
