n = int(input("Введите n строк: "))
for _ in range(n):
    words = input("Введите слова: ")

    if len(words) > 10:
        abbrev = words[0] + str(len(words) - 2) + words[-1]
        print(abbrev)
    else:
        print(words)