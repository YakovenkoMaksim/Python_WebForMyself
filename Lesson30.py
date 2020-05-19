# https://docs.python.org/3.8/library/

import os
# import random as r
# from random import randint, shuffle
# from random import *  # import all method

# print(os.getcwd())

# print(randint(1, 100))
# l = [1, 2, 3, 4, 5]
# shuffle(l)
# print(l)

# import os
# import os as my
#
# print(os.getcwd())
# print(my.getcwd())

import libs
from libs import get_len, get_count

print(get_count('hello', 'l'))
print(get_len('hello'))

f = libs.get_count
print(f('hello', 'l'))
