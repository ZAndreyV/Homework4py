
# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# from random import randint
#
# n = int(input("Enter length of the list1: "))
# m = int(input("Enter length of the list2: "))
# list1 = [randint(1, 50) for _ in range(n)]
# list2 = [randint(1, 50) for _ in range(m)]
# list_sorted1 = set(list1)
# list_sorted2 = set(list2)
# res = sorted(list_sorted1.intersection(list_sorted2))
# print(res)
#
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом,
# у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.


# from random import randint
# N = int(input("Enter amount of bushes: "))
# # amount = input("Enter the number of berries on the bushes by a space: ").split()
# # garden_bed = list(map(int, amount))
# garden_bed = [randint(1, 10) for _ in range(N)]
# print(garden_bed)
#
# sum_of_three = list()
# for i in range(len(garden_bed) - 1):
#     sum_of_three.append(garden_bed[i - 1] + garden_bed[i] + garden_bed[i + 1])
# garden_bed.append(sum_of_three[- 2] + garden_bed[- 1] + garden_bed[0])
# print(max(sum_of_three))



