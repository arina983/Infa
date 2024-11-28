dictionary = { '1' : '.,?!:',
               '2' : 'a b c',
               '3' : 'd e f',
               '4' : 'g h i',
               '5' : 'j k l',
               '6' : 'm n o',
               '7' : 'p q r s',
               '8' : 't u v',
               '9' : 'w x y z',
               '0' : ' ' }

for k in dictionary:
     print(k, ":", dictionary[k])

n = input("Введите текст: ").lower()
result = ""

for i in n:
    for k in dictionary:
        if i in dictionary[k]:
          result += k
          break
    else:
        pass
print(result)

