from datetime import date, datetime, timedelta
import locale

# date
# today = date.today()
# print(today)  # 2020-05-20
# print(today.day)  # 20
# print(today.month)  # 5
# print(today.year)  # 2020
# print(today.weekday())  # 2

# datetime
# now = datetime.now()
# print(now)  # 2020-05-20 22:33:28.645866
# print(now.day)  # 20
# print(now.month)  # 05
# print(now.year)  # 2020
#
# days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
# print(days[now.weekday()])  #ср

# locale.setlocale(locale.LC_ALL, 'ru_RU')
# now = datetime.now()
# print(now)
#
# print(now.strftime('%a'))
# print(now.strftime('%A'))
#
# print(f'Дата: {now.strftime("%A, %d %b %Y")}')
# print(f'Время: {now.strftime("%H:%M:%S")}')
#
# print(now.strftime('%c'))
# print(now.strftime('%x'))
# print(now.strftime('%X'))

# now = datetime.today()
# print(now.strftime('%c'))
# d1 = now + timedelta(days=1, hours=2, minutes=10)
# print(d1.strftime('%c'))
