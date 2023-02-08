# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.


from random import randint

# arrayUserFirst = []
# arrayUserSecond = []
# userFirst = int(input("Input number for firstUser: "))
# userSecond = int(input("Input number for secondUser: "))

def createArray(num, forArray):
    for i in range(num):
        forArray.append(randint(1,num)) 
        

# def printArray(userArray):
#     if userArray == arrayUserFirst:
#         print(f"Array for userFirst: {userArray}")
#     else:
#         print(f"Array for userSecond: {userArray}")

# def jointSet(firstArray, secondArray):
#     joint = set(firstArray)
#     print(joint.intersection(secondArray))
    

# createArray(userFirst, arrayUserFirst)
# createArray(userSecond, arrayUserSecond)
# printArray(arrayUserFirst)
# printArray(arrayUserSecond)
# jointSet(arrayUserFirst,arrayUserSecond)


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло a ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

berryArray = []
inputBush = int(input("Input bush number: "))

createArray(inputBush, berryArray)
print(berryArray)

numberBush = int(input(f"Input number bush not more count bushes: "))
allBerryWithBush = 0

def countStrawberryBush(numBush):
    bushIndex = numBush - 1
    lenghArray = len(berryArray)
    leftBush = berryArray[bushIndex - 1]
    if leftBush < 0:
        leftBush = berryArray[lenghArray - 1]
    middleBush = berryArray[bushIndex]
    if numBush == lenghArray:
        rightBush = berryArray[0]
    else:
        rightBush = berryArray[bushIndex + 1]
    allBerryWithBush = leftBush + middleBush + rightBush
    print(f"---Right bush {rightBush} 🫐 \n-----Input bush {middleBush} 🫐\n---Left bush {leftBush} 🫐")
    print(f"Number of berries 🫐  on three 🌳🌳🌳 bushes: {allBerryWithBush}")
    

countStrawberryBush(numberBush)