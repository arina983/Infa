n, k = map(int, input("Введите n и k ").split())
scores = list(map(int, input().split()))
pass_score = scores[k-1]
count = 0
for i in scores:
    if i >= pass_score and i > 0:
        count += 1
print(count)