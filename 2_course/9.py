name = input("введите имя пользователя: ")
if len(name) > 100 :
    print("ошибка! имя пользователя не может быть более 100 символов")

symbol = set(name)
symbols = len(symbol)

if symbols %2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")