#8
def string(strings):
    return [string.capitalize() for string in strings if string[0].isupper()]
input_strings = input("Введіть рядок:").split()
result = string(input_strings)
print(f"Список рядків, які починаються з великої літери: {result}")