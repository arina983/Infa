with open('C:/Users/Ариша/OneDrive/Рабочий стол/lab10/file3.txt',  encoding = "UTF-8") as file:
    original_text = file.read()

new_text = input("Введите текст: ")

with open('C:/Users/Ариша/OneDrive/Рабочий стол/lab10/file3.txt', 'w', encoding = "UTF-8") as file:
    middle_text = len(original_text) // 2
    file.write(original_text[:middle_text])
    file.write(new_text)
    file.write(original_text[middle_text:])

