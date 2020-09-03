some_str = input('Введите строку из нескольких слов ')
some_str = some_str.split()
print(some_str)
n = 0
for new_str in some_str:
    n = n + 1
    print(n, '.', new_str[:10])