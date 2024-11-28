i = input("Введите 2 слова: ") 
words = i.split()
if len(words) == 2:
    print (words[1] + " " + words[0])
else:
    print("Фраза должна состоять из 2 слов")
    