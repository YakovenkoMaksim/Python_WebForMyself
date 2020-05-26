# Инкапсуляция
from classes import Person

# import classes

person1 = Person(name='John')
person1.print_info()

person2 = Person(name='Katy')
# person2.__age = 30
# print(person2.get_age())
# person2.set_age(25)
print(person2.age)
person2.age = 35
person2.print_info()
