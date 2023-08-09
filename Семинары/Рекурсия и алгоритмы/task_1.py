"""Задача 1:Напишите функцию f, которая на вход принимает два числа a и b,
и возводит число a в целую степень b с помощью рекурсии.."""


# def my_f(a, b):
#     if b == 0:
#         return 1
#     return my_f(a, b - 1) * a


# def my_f(a, b):
#     return 1 if b == 0 else my_f(a, b - 1) * a

# # print(my_f(10, 1))
# a=10
# b=3
# print(my_f(a, b - 1) * a)

def my_f(a, b):
    return a if b == 0 else my_f(a, b - 1) + 1

# print(my_f(10, 1))
a=0
b=5
print(my_f(a, b))