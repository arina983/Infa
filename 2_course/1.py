weight = int(input("введите вес арбуза: "))
if weight < 0 :
    print("весь должен быть положительным!")
elif weight % 2 == 0 :
    print("YES")
else:
    print("NO")
