#9
def sort(strings):
    a = []
    for string in strings:
        if string == "Python":
            return string
    return a
b = input("Введіть рядок: ").split(' ')
res = sort(b)
print(res)
