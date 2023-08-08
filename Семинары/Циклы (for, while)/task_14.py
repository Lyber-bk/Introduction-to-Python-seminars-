"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
Дополнительное задание:
Найти ошибку в коде урока https://github.com/SciWake/Python_07/blob/main/Lesson_2/Task_13.py
"""

N = int(input('N = '))
k = 1
while k <= N:
    print(k)
    k*=2

