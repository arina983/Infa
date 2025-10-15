s = input('введите слово: ')
if len(s) < 1 or len(s) > 100:
    print('некорректная длина слова')

lower_letter = 0
upper_letter = 0
for char in s:
    if char.isupper():
        upper_letter += 1
    else:
        lower_letter += 1

if lower_letter > upper_letter:
    print(s.lower())
else:
    print(s.upper())