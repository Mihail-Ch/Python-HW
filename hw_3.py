# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N].
# Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел A.
# Последняя строка содержит число X

from random import randint


# array = []
# number = int(input("Input number: "))

# def createArray(num):
#     for i in range(num):
#         array.append(randint(1,num))
#     print(f"---Array: {array}")

# createArray(number)

# numContains = int(input("Input number X: "))

# def numberContains(num):
#     count = 0
#     for i in array:  
#      if i == numContains:
#         # array.__contains__(i)
#         count += 1
#     print(f"---Count repeat number in array: {count}")

# numberContains(numContains)

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# def nearbyNumber(num):
#     maxNum = max(array)
#     nearbyForMax = maxNum - 1
#     for i in array:
#         if i == nearbyForMax:
#             print(f"---MAX number in Array: {maxNum}")
#             print(f"---Nearby number for MAX in Array: {i}")
#             break
#         else:
#             nearbyForMax -= 1

# nearbyNumber(numContains)

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.

dictionaryAlphabet = [
    {
        1: ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"],
        2: ["D", "G", "Д", "К", "Л", "М", "П", "У"],
        3: ["B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я"],
        4: ["F", "H", "V", "W", "Y", "Й", "Ы"],
        5: ["K", "Ж", "З", "Х", "Ц", "Ч"],
        8: ["J", "X", "Ш", "Э", "Ю"],
        10: ["Q", "Z", "Ф", "Щ", "Ъ"]
     }
    ]

string = "ноут@234  бук"
coins = 0
# Перебираем массив
for dict in dictionaryAlphabet:
    # Разбираем на кортежи и получаем ключи и значения
    for (key, value) in dict.items():
        # Записываем значения в отдельную переменную
        some = set(value)
        # Записываем ключ для подсчета очков
        newKey = key
        # Перебираем слово
        for i in string.upper():
            # Если есть совапдения прибавляем очки по ключу
            if some.__contains__(i):
                coins += newKey
                
                
print(coins)
