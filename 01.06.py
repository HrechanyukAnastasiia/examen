#5
def string(s):
    s = s.lower()
    s = s.replace(" ", "")
    if s == s[::-1]:
        print("Слово є паліндромом")
    else:
        print("Не є паліндромом")
a = input("Введіть рядок:")
string(a)