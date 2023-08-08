"""Дан список чисел. Определите, сколько в нем
встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4]

Output: 6
"""

numbers = [1, 2, 3, 1, 1, 5, 20, 20, 30]

# Вариант 1
result = []
for num in numbers:
    if num not in result:
        result.append(num)
print(len(result))





"""Напишите программу для печати всех уникальных значений в словаре."""

list_1 = [{"V": "S001", "V12": "S0012"}, {"V": "S002"}, {"VI": "S001"},
          {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# Вариант 1 
"""Так делать плохо! Получаем ключ (key) в цикле (for key in dict_item)
а потом этот ключ (key) используем для получения значений словаря (dict_item[key])."""
unique_kyes = set()
for dict_item in list_1:
    for key in dict_item:
        unique_kyes.add(dict_item[key])  # Получаем значение по ключу и кладём в множество
print(unique_kyes)


# Вариант 1.1 - Modified
unique_kyes = set()
for dict_item in list_1:
    for value_dict in dict_item.values():  # Сразу получи значения словаря, а не его ключ
        unique_kyes.add(value_dict)  # Кладём значение без обрашения по ключу (dict_item[key])
print(unique_kyes)


# Вариант 2
unique_kyes = set()
for dict_item in list_1:
    unique_kyes.update(dict_item.values())
print(unique_kyes)
