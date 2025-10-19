n = input('введите число n: ')
count = 0
for i in range(len(n)):
    if n[i] == '7' or n[i] == '4':
        count += 1

count_str = str(count)
for i in count_str:
    if i != '4' and i != '7':
        print('NO')
        break
else:
    if count > 0:
        print('YES')
    else:
        print('NO')