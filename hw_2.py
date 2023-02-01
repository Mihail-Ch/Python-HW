# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

#number = input("Input number: ")

def sumNumber(a):
    numberSum = 0
    for i in str(a):
        if i != ".":
            numberSum += int(i)
    print(numberSum)

#sumNumber(number)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# numberN = int(input("Input number: "))

def proizNumber(a):
    result = 1
    if a == 0 or a < 0:
        print(f"Number {a} less then zero")
    else:   
        for i in range(1, a + 1):
            result *= i
            print(result)

# proizNumber(numberN)


# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
num = int(input("Input number: "))

def listSequence(a):
    sequence = [round((1+1/i)**i, 2) for i in range(1, a+1)]
    print(f'Последовательность: {sequence}\nСумма: {round(sum(sequence), 3)}')

listSequence(num)


# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.

from random import randint

array = []
for i in range(10):
    array.append(randint (-10,10))
print(array)

def getNumber(numbers):
    count = 0 
    for element in numbers:
        count += 1
    return count
print('Number of elements: ', getNumber(array))

x = int(input('Enter  position of first element: '))
y = int(input('Enter position of second element: '))

for i in range(len(array)):
     mult = array[x -1]*array[y - 1]
print(f'Mult of elements: {array[x - 1]} * {array[y - 1]} =', mult)



#Реализуйте алгоритм перемешивания списка.

import random

def repeatList(a):
    lst = a
    lstCount = len(lst)
    for i in range(lstCount):
        index = random.randint(0, lstCount - 1)
        temp = lst[i]
        lst[i] = lst[index]
        lst[index] = temp
    print(lst)

a = [1, 4, 3, 4, 5, 0, 7, 8, 90]

repeatList(a)