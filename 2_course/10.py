s = list(map(int,input('input sum: ').split('+')))
if len(s) > 100:
    print('ERROR')

i = 0
for j in range(len(s)):
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            temp = s[i]
            s[i] = s[i + 1]
            s[i + 1] = temp

print('+'.join(map(str, s)))