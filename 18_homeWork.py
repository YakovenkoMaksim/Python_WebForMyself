"""
1. Дан список. Получите новый список, в котором каждое значение будет удвоено:
[1, 2, 3] --> [2, 4, 6]
"""
#  Вариант 1 - Мой
# list = [1, 2, 3, 4, 5, 6]
# x = 0
# for i in list:
#     list[x] = i * 2
#     x += 1
# print(list)

#  Вариант 2 - меньше, удобнее
# list = [1, 2, 3, 4, 5, 6]
# list2 = [i * 2 for i in list]
# print(list2)


"""
2. Дан список. Возведите в квадрат каждый из его элементов и получит сумму всех полученных квадратов:
[1, 2, 3] --> 14 --> 1^2 + 2^2 + 3^2 = 14
"""

# list = [1, 2, 3]
# x = 0
# sum = 0
# for i in list:
#     list[x] = i ** 2
#     sum += list[x]
#     x += 1
# print(sum)

"""
3. Игорь любит кататься на велосипеде. Он знает, что при этом важно не допустить обезвоживания и пьет 0,5 литра воды в час. 
Вам дается время в часах, и вам нужно вернуть количество литров, которые Игорь выпьет, с округлением до наименьшего значения.
time1 = 3 --> litres = 1
time2 = 6.7 --> litres = 3
time3 = 11.8 --> litres = 5
"""
# bottle = 0.5
# time1 = 3
# time2 = 6.7
# time3 = 11.8
#
# print(int(time1 * bottle))
# print(int(time2 * bottle))
# print(int(time3 * bottle))

# import math
# time = [3, 6.7, 11.8]
# bottle = 0.5
# litres = []
#
# for i in time:
#     litres.append(math.floor(i * bottle))
# print(litres)



"""
4. Дана строка 'Hello world'. Проверьте, если в этой строке есть символ пробела - " ", 
тогда преобразуйте строку к верхнему регистру, если же нет, тогда к нижнему.
***************
s = 'Hello world'
if stm:
	pass
else:
	pass
"""

# s = 'Hello world'
# if s.find(' '):
#     print(s.upper())
# else:
#     print(s.lower())

# s = 'Hello world'
# if ' ' in s:
#     s = s.upper()
# else:
#     s = s.lower()
#
# print(s)