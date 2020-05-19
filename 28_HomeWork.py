"""
1. Дан массив, в котором среди прочих элементов есть слово "odd" (нечетный).
Определите, есть ли в списке число, которое является индексом элемента "odd".
Напишите функцию, которая будет возвращать True или False, соответсвенно.
"""

# Мой способ
# def odd_ball(arr):
#     arr2 = arr.copy()
#     for i in arr:
#         if type(i) != int:
#             arr.remove(i)
#     for j in arr2:
#         if j == arr2.index('odd'):
#             print(True)
#
# Способ из урока
# def odd_ball(arr):
#     return arr.index('odd') in arr
#
#
# print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"]))
# print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"]))
# print(odd_ball(["even", 10, "odd", 2, "even"]))


"""
2. Напишите функцию find_sum(n), где аргумент функции - это конечный элемент последовательности включительно. 
Функция должна вернуть сумму всех чисел последовательности, кратных 3 или 5. 
Попробуйте решить задачу двумя способами (один из способов в одну строчку кода).
"""

# def find_sum(n):
#     get_sum = 0
#     for i in range(n + 1):
#         if i % 3 == 0 or i % 5 == 0:
#             get_sum += i
#     return get_sum


# def find_sum(n):
#     return sum(i for i in range(n + 1) if i % 3 == 0 or i % 5 == 0)


# print(find_sum(5))  # return 8 (3 + 5)
# print(find_sum(10))  # return 33 (3 + 5 + 6 + 9 + 10)

"""
3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]
"""


# def get_names(names):
#     for i in names:
#         if len(i) > 4:
#             names.remove(i)
#     print(names)

# def get_names(names):
#     return [i for i in names if len(i) == 4]
#
#
# names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"]  # ["Ryan", "Mark", "John", "Paul"]
# print(get_names(names))
