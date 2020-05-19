"""
Дан список words. Составьте из него список слов-палиндромов.
Попробуйте это сделать двумя способами: произвольное решение и решение в одну строчку кода.
Дан список my_str со строками, часть из которых являются палиндромами. Составьте новый список строк-палиндромов.
"""

words = ['мадам', 'топот', 'test', 'madam', 'word']
# for i in words:
#     if i == i[::-1]:
#         continue
#     else:
#         words.remove(i)
# print(words)

# palindromes = [ word for word in words if word == word[::-1]]
# print(palindromes)


my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
palindromes = []
for word in my_str:
    word_r = word.replace(' ', '').lower()
    if word_r == word_r[::-1]:
        palindromes.append(word)
print(palindromes)
