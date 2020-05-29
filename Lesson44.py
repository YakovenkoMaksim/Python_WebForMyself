# Regular expression operations
# https://docs.python.org/3.8/library/re.html?highlight=re#module-re
# https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%BD%D1%8B%D0%B5_%D0%B2%D1%8B%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F

import re


# s = 'Это просто строка текста. А это ещё одна строка текста.'
# pattern = 'строка'

# .search
# if re.search(pattern, s):
#     print('Matched')
# else:
#     print('No match')

# .match - ищет совпадение с начала строки
# print(re.match(pattern, s))

# .findall
# print(re.findall(pattern, s))

# .split
# print(re.split(r'\.', s, 1))


# s = '''Это просто строка текста.
# А это ещё одна строка текста.
# А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, ٣, 0, 10
# А это строка с разными символами: "!", "@", "-", "&", "?", "_"
# a\\b\tc
# test string'''


# pattern = '\w+'
# pattern = r'[а-яё]+'
# pattern = r'[0-9]+'
# pattern = r'\d+'
# pattern = r'[\da-]+'

# print(re.findall(pattern, s, flags=re.IGNORECASE))


def validate_email(email):
    return re.match(r'^.+@(\w+\.){0,2}[a-z]{2,6}$', email, re.IGNORECASE)


print(validate_email('mail@mail'))
print(validate_email('yakovenko12@mail.com'))
print(validate_email('mail@mail.co.ua'))
