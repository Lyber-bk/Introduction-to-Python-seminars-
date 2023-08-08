


list_1 = [1, 2, 3, 3, 5]
k = 3
result = []
for num in list_1:
    if num == k:
        result.append(num)
print(len(result))

"""
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
"""
list_1 = [1, 12, 6, 7, 8, 15]
k = 11

result = list_1[0]
target = abs(k - result)

for num in list_1:
    distans = abs(num - k)
    if distans < target:
        result = num
        target = distans
print(result)


"""*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква 
имеет определенную ценность. В случае с английским алфавитом очки 
распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; 
B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; 
Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; 
Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость 
введенного пользователем слова. Будем считать, что на вход подается только одно слово, 
которое содержит либо только английские, либо только русские буквы.

*Пример:*

ноутбук
    12"""


k = 'ноутбук'

dic_Scrabble = {1: 'AEIOULNSTRАВЕИНОРСТ',
      2: 'DGДКЛМПУ',
      3: 'BCMPБГЁЬ',
      4: 'FHVWYЙЫ',
      5: 'KЖЗХЦЧ',
      8: 'JZШЭЮ',
      10: 'QZФЩЪ'}


word = k.upper()
print(sum([k for i in word for k, v in dic_Scrabble.items() if i in v]))



# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_en:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)
