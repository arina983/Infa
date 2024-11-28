s = input("Введите трехстишие: ")
b = s.split('/')
if len(b) == 3:
    a1,a2,a3=b[0],b[1],b[2]
    if len(a1) == 5 and len(a3) == 5 and len(a2) == 7:
        print("Хайку!")
    else:
     print("Не Хайку.")
else:    
    print("Должно быть 3 строки")




