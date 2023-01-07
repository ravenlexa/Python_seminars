'''3. Напишите программу, которая определит позицию второго вхождения
строки в списке либо сообщит, что её нет.

*Пример:*

- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
- список: [], ищем: "123", ответ: -1 '''
# my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# print(f'Ответ: {my_list.count("qwe")}')


# my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# index_list = []
# print(my_list)
# search = input('Введите искомый элемент: ')
#
# for i in range(len(my_list)):
#     if search == my_list[i]:
#         index_list.append(i)
# else:
#     if len(index_list) < 2:
#         print('Второго вхождения нет')
#     else:
#         print(f'Индекс второго вхождения {index_list[1]}')


my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
print(my_list)
search = input('Введите искомый элемент: ')
count = 0
for i in range(len(my_list)):
    if my_list[i] == search:
        count += 1
        if count == 2:
            print(f'Индекс второго вхождения {i}')
            break
else:
    print('-1')
