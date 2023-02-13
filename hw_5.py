# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (35)
# A = 2; B = 3 -> 8

firstNumber = int(input("Input first number: "))
powNumber = int(input("Input number for pow: "))

# def powNumbersResult(num, powNum):
#     print(pow(num, powNum))

def powNumbersResult(num, powNum):
    if powNum == 1:
        return(num)
    if powNum != 1:
        return(num * powNumbersResult(num, powNum - 1))

print(powNumbersResult(firstNumber, powNumber))


# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 22 
# 4

def sumNumbers(a, b):
    a += 1
    b -= 1
    if b > 0:
        return sumNumbers(a, b)
    else:
        return a
print(sumNumbers(2, 2))
