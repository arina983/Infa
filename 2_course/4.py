n = int(input("input n: "))
count = 0
for _ in range(n):
    s = input("input s: ")

    if "++" in s:
        count += 1
    elif "--" in s:
        count -= 1

print(count)
