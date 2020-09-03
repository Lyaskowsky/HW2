n = int(input('Введите чисел Вы будете добавлять в список? '))
my_list = [7, 5, 3, 3, 2]
max_el = max(my_list)
number = 1

while number <= n:
    some_int = int(input('Введите число для добавления в рейтинг '))
    if some_int > max_el:
            my_list.insert(0, some_int)
    elif some_int in my_list:
            my_list.insert(my_list.index(some_int),some_int)
    else:
            my_list.append(some_int)

    number += 1
my_list.sort()
my_list.reverse()
print(my_list)
