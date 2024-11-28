n = int(input("Введите количество рядов в кинотеатре: "))
m = int(input("Введите количество мест в ряду: "))

seats = []
print("Введите информацию о занятости места(0- свободно, 1 - занято): ")
for _ in range(n):
   row_str = input() 
   row = list(map(int, row_str.split()))
   seats.append(row)

k = int(input("Введите количество человек: "))

found_row = 0
for i in range(n):
   free_seats = 0
   for j in range(m):
      if seats[i][j] == 0:
         free_seats +=1
         if free_seats == k:
            found_row = i + 1
            break
      else:
         free_seats = 0
   if found_row != 0:
      break    
       
print(found_row)

