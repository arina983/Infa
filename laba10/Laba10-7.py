import random

with open('C:/Users/Ариша/OneDrive/Рабочий стол/lab10/file5.txt', encoding = "utf-8") as file:
    text = file.read()
words = text.split()
password = []

while len(password) < 2:
    for word in words:
        if len(word) >= 3:
            password.append(word)
            if len(password) == 2:
                break

password = random.choice(words) + random.choice(words)

while len(password) < 8 or len(password) > 10:
    password = random.choice(words) + random.choice(words)

print("Сгенерированный пароль: " , password)
