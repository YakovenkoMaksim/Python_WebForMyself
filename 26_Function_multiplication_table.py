# multiplication table
def multi_table(a, b):
    for i in range(1, 10):
        for j in range(a, b):
            print(f'{i} * {j} = {i * j}\t', end='')
        print('')
    else:
        print('Done')


print('Таблица умножения\n')

multi_table(1, 8)