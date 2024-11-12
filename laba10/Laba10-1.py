winner = ""
max_score = 0

second_place = ""
second_score = 0


with open('C:/Users/Ариша/OneDrive/Рабочий стол/lab10/file4.txt', encoding = "UTF-8") as file:
    record = file.readline()
    while record:
        human = record.split()
        if int(human[-1]) > max_score:
            winner = human[0] + " " + human[1]
            max_score = int(human[-1])
            record = file.readline()
        elif int(human[-1]) > second_score:
            second_place = human[0] + " " + human[1]
            second_score = int(human[-1])
            record = file.readline()
            

print("Призер:", second_place, " ( Набранное количество баллов:", second_score, ')')
           
