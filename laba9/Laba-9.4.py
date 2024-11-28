menu = [
["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
]
while True:
    print("\nВыберите действие:")
    print("1. Показать меню")
    print("2. Найти блюдо")
    print("3. Добавить блюдо")
    print("4. Изменить цену блюда")

    choice = input("Введите номер действия: ")

    if choice == '1':
        print("Меню:")
        for dish in menu:
            print(dish[0], "-", dish[2], "руб.")
            print('Ингридиенты: ', ", ".join(dish[1]))
        break 

    elif choice == '2':
        dish_name = input("Введите название блюда: ") 
        
        for dish in menu:
            if dish[0] == dish_name:
                print(f"Название блюда: {dish_name}")
                print(f"Цена: {dish[2]} руб.")
                break

    elif choice == '3':
        name = input("Введите название блюда: ")
        price = int(input("Введите цену блюда: "))
        ingridients = input("Введите инридиенты, разделяя их запятой").split(",")
        menu.append([name, ingridients, price])
        print(f"Блюдо '{name}' добавлено в меню.")
    
    elif choice == '4':
        name = input("Введите название блюда: ")
        for i, dish in enumerate(menu):
            if dish[0] == name:
                new_price = int(input("Введите новую цену блюда: "))
                menu[i][2] = new_price
                break
        print(f"Цена блюда '{name}' изменена на '{new_price}' руб.")
                
