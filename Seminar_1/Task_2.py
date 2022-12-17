"""2. Напишите программу, которая на вход принимает 5 чисел
и находит максимальное из них.
Примеры:
- 1, 4, 8, 7, 5 -> 8
- 78, 55, 36, 90, 2 -> 90"""
import random

"""number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))
number4 = int(input('Введите четвертое число: '))
number5 = int(input('Введите пятое число: '))
MAX = 0
if MAX < number1:
    MAX = number1
if MAX < number2:
    MAX = number2
if MAX < number3:
    MAX = number3
if MAX < number4:
    MAX = number4
if MAX < number5:
    MAX = number5
print(MAX)"""

"""my_list = [0, 0, 0, 0, 0]

for i in range(len(my_list)):
    my_list[i] = int(input('Введите число: '))
print(my_list)

MAX = my_list[0]

for i in range(len(my_list)):
    if MAX < my_list[i]:
        MAX = my_list[i]
print(MAX)"""


"""my_list = []

for i in range(5):
    my_list.append(int(input('Введите число: ')))

print(my_list)

MAX = my_list[0]

for i in my_list:
    if i > MAX:
        MAX = i
print(MAX)"""

my_list = []

for i in range(5):
    my_list.append(random.randint(0, 100))

print(*my_list)

MAX = my_list[0]

for i in my_list:
    if i > MAX:
        MAX = i
print(MAX)





