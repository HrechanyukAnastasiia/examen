#6
a = int(input("Введіть перше число діапазону:"))
b = int(input("Введіть друге число діапазону:"))
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=" ")