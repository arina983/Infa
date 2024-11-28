import random

s = int(input("Введите желаемую длину пароля: "))
a = input("нужны ли заглавные буквы?(да\нет)") == "да"
b = input("нужны ли строчные буквы?(да\нет)") == "да"
c = input("нужны ли цифры?(да\нет)") == "да"
d = input("нужны ли специальные символы?(да\нет)") == "да"

r = ""

if a :
     r += "QWERTYUIOPASDFGHJKLZXCVBNM"
if b : 
    r +=  "qwertyuiopasdfghjklzxcvbnm"
if c: 
    r +=  "0123456789"
if d:    
    r += "!@#$%^&*()_+<>?/:;"
if not r:
    print("Ошибка")
else:
    password = ''.join(random.choice(r) for _ in range(s))
    print("Сгенерированный пароль: ", password)

