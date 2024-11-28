s = input("Введите информацию с табло: ")
a = s.split("-")
team1 = a[0].strip()
team2 = a[1].split()[0].strip()

score = a[1].split()[1].split(":")
sc1 = int(score[0])
sc2 = int(score[1])

if sc1 > sc2:
    print(team1)
elif sc1 < sc2:
    print(team2)
else:
    print("Ничья")

