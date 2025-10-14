x = int(input("введите координату дома слоника: "))
number_of_steps = 0
if x % 5 == 0:
    number_of_steps = x // 5
else:
    number_of_steps = x // 5 + 1
print(number_of_steps)

