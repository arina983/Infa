dictionary = {'1' : 'A,E,I,L,N,O,R,S,T,U',
              '2' : 'D,G',
              '3' : 'B,C,M,P',
              '4' : 'F,H,V,W,Y',
              '5' : 'K',
              '8' : 'J, X',
              '10' : 'Q, Z' }
n = input("Введите слово: ").upper()
result = 0

for i in n:
    for k in dictionary:
        if i in dictionary[k]: 
            result += int(k)
            break
    else:
        print("Error")    

print("Сумма очков за слово: ", result)

            