n, h = map(int, input("введите количество друзей и высоту забора: ").split())
a = list(map(int, input("введите рост каждого человека: ").split()))
sum = 0
for i in range(n):
    if a[i] > h:
        l = 2
    else:
        l = 1
    sum += l
print(sum)
