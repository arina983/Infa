k, n, w = list(map(int, input("введите: ").split()))

dollars = 0
for i in range(w):
    dollars += (1 + i) * k

total = dollars - n
if total < 0:
    total = 0
print(total)
