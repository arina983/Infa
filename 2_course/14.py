n = int(input("Введите количество цветов: "))
if n > 50 or n < 1:
    print("введите корректное количество камней")
s = list(input("введите цвета: "))

min_col = 0
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        min_col += 1
print(min_col)


