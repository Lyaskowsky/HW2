
number_month = int(input('Введите номер месяца '))
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if number_month in winter:
    print('Введенный номер месяца относится ко времени года - Зима')
if number_month in spring:
    print('Введенный номер месяца относится ко времени года - Весна')
if number_month in summer:
        print('Введенный номер месяца относится ко времени года - Лето')
if number_month in autumn:
        print('Введенный номер месяца относится ко времени года - Осень')


time_year = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}

user_answer = int(input('Введите номер месяца '))
for key in time_year.keys():
    if user_answer in time_year[key]:
        print('Введенный номер месяца относится ко времени года:', key)