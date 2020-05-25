# f = open('test/index.html', 'r', encoding='utf-8')
# text = f.read()
# # print(f.encoding)
# f.close()
# print(text)

# f = open('test/index.html', 'a', encoding='utf-8')
# f.write('Новая строка\n')
# f.close()

# lines = ['Новая строка 1', 'Новая строка 2']
# f = open('test/index.html', 'a', encoding='utf-8')
# for i in lines:
#     f.write(i + '\n')
# f.close()

# lines = ['Новая строка 1', 'Новая строка 2']
# f = open('test/index.html', 'a', encoding='utf-8')
# f.writelines(f'{i}\n' for i in lines)
# f.close()

# f = open('test/index.html', 'r', encoding='utf-8')
# for line in f:
#     print(line, end='')
# f.close()

# lines = ['Новая строка 1', 'Новая строка 2']
# f = open('test/text.txt', 'w', encoding='utf-8')
# f.writelines(f'{i}\n' for i in lines)
# f.close()
