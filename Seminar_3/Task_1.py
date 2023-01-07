'''Задайте список. Напишите программу, которая определит,
присутствует ли в заданном списке строк некое число.'''

# my_list = ['12jffjk', 'ghfjgh12kkk', 'kfjgkfg12', '455kkk44']
#
# for i in my_list:
#     if i.count('34'):
#         print('есть')
#         break
#     else:
#         print('нет')

my_list = ['12jffjk', 'ghfjgh12kkk', 'kfjgkfg12', '455kkk44']
num = input('Введите число: ')
for i in range(len(my_list)):
    if num in my_list[i]:
        print(f'Число {num} есть в строке {my_list[i]}  у которой индекс {i}')
        break
else:
    print('Такого числа нет!')
