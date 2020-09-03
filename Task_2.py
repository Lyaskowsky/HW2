end_list = int(input('Введите количество элементов списка '))
some_list = []
while len(some_list) < end_list:
    element_list = int(input('Введите элемент '))
    some_list.append(element_list)
print('Сформированный список: ', some_list)

if len(some_list) % 2 == 0:
    for i in range(0, len(some_list), 2):
        some_list[i+1], some_list[i] = some_list[i], some_list[i+1]

else:
    for i in range(0, len(some_list)-1, 2):
        some_list[i+1], some_list[i] = some_list[i], some_list[i+1]

print('Отредактированный список: ', some_list)