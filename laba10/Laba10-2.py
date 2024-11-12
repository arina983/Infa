with open('C:/Users/Ариша/OneDrive/Рабочий стол/lab10/file5.txt', encoding = "UTF-8") as file:
    text = file.read()
    words = text.split()
    if "Academy" in words:
        print("file5.txt")
        
with open('C:/Users/Ариша/OneDrive/Рабочий стол/lab10/file6.txt', encoding = "UTF-8") as filee:
    textt = filee.read()
    words = textt.split()
    if "Academy" in words:
         print("file6.txt")