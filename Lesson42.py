# def hello():
#     return 'Hello, I\'m func "hello"'
#
#
# def super_func(func):
#     print('Hello, I\'m super_func "hello"')
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return 'Hello, I\'m func "hello"'
#
#
# test = hello
# print(test())


# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper()
#
#
# @my_decorator
# def func_test():
#     print('Hello, I\'m func "func_test"')


# test = my_decorator(func_test)
# test()


def make_title(fn):
    def wraped():
        title = fn()
        title = title.capitalize()
        title = title.replace(',', '')
        return title

    return wraped


@make_title
def hi():
    return 'hello, world '


print(hi())