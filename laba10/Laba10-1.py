winner = ""
max_score = 0

second_score = 0
second_place = ""

with open('C:/Users/Ариша/OneDrive/Рабочий стол/lab10/file4.txt', encoding = "utf-8") as file:
   
    for record in file:
        human = record.split()
        if int(human[-1]) > max_score:
            winner = human[0] + " " + human[1]
            max_score = int(human[-1])

        elif int(human[-1]) > second_score:
            second_place = human[0] + " " + human[1]
            second_score = int(human[-1])       

print("Победитель:", second_place, " ( Набранное количество баллов:", second_score, ')')