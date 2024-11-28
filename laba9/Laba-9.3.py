import math

n = int(input("Введите количество сокровищ: "))
treasure_map = []

print("Координаты сокровищ: ")

for i in range(n):
    x, y = map(int, input().split())
    treasure_map.append([x, y])

print("Координаты Саши: ")    
alex_x, alex_y = map(int, input().split())

closest_treasure = treasure_map[0]  
min_distance = math.sqrt((closest_treasure[0] - alex_x)**2 + (closest_treasure[1] - alex_y)**2) 

for treasure in treasure_map:
    distance = math.sqrt((treasure[0] - alex_x)**2 + (treasure[1] - alex_y)**2)
    if distance < min_distance:
        min_distance = distance
        closest_treasure = treasure


print(f"Координаты ближайшего сокровища: {closest_treasure}")

