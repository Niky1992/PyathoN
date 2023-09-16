# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('Введите число N: '))
numbers = 0
num = 2
for i in range(N):
    if numbers != 1:
        num = num ** i
        if num <=N:
            print(num, end=' ')
            num = 2
        else:
            numbers = 1

