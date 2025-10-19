n = int(input("Введите количество сыгранных партий: "))
s = input("Введите победителя по партии: ")
count_A = 0
count_D = 0
for i in range(len(s)):
    if s[i] == 'A':
        count_A += 1
    elif s[i] == 'D':
        count_D += 1
if count_A > count_D:
    print('Anton')
elif count_D > count_A:
    print('Danik')
elif count_A == count_D:
    print('Friendship')
