"""9. По данному целому неотрицательному n вычислите значение n!.
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
Решить задачу используя цикл while"""
# from time import sleep


# ВАРИАНТ 1 -- 1 * 2 * 3 * 4
n = int(input("n = "))
i = 1
fact = 1

while i <= n:
    fact *= i
    i += 1

print(f'{n}! = {fact}')


# ВАРИАНТ 2 -- 4 * 3 * 2 * 1
# n = int(input("n = "))
# fact = 1
# while n > 1:
#     fact *= n
#     n -= 1
# print(fact)