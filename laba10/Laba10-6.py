with open('C:/Users/Ариша/OneDrive/Рабочий стол/lab10/file1.txt', encoding = "utf-8") as file:
  text = file.read()
  
words = text.split()
decrypted_words = []

for word in words:
    decrypted_word = word[::-1]
    decrypted_words.append(decrypted_word)

decrypted_massage = " ".join(decrypted_words)
print(decrypted_massage)