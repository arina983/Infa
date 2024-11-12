col = 0
total_words = 0
with open('C:/Users/Ариша/OneDrive/Рабочий стол/lab10/file6.txt', encoding = "UTF-8") as file:
    text = file.read()
    words = text.split()
    total_words = len(words)
for word in words:
    if "e" in word:
        col += 1
result = (col / total_words) * 100        
print("Процент слов:" ,result, '')
