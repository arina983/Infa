n = int(input("Введите количество вопросов и ответов: "))
v = input("Введите вопрос или ответ(Q или A): ")
result = ""
for p in v:
    if p == "Q":
        result = "-"
    elif p == "A":
        result = "+"      
print(result)          
