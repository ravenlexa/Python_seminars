"""Напишите программу, в которой пользователь будет задавать две строки,
а программа - определять количество вхождений одной строки в другую."""

"""text = 'Напишите программу, в которой пользователь будет задавать две строки,' \
       'а программа - определять количество вхождений одной строки в другую.'

search = input('Введите искомую букву: ')

count = 0

for char in text:
    if search == char:
        count += 1

print(f'В заданном тексте буква "{search}" встречается {count} раз')"""

"""text = 'Напишите программу, в которой пользователь будет задавать две строки,' \
       'а программа - определять количество вхождений одной строки в другую.'

search = input('Введите искомую букву: ')
text = text.split(search)
print(text)
print(len(text) - 1)"""

text = 'Напишите программу, в которой пользователь будет задавать две строки,' \
       'а программа - определять количество вхождений одной строки в другую.'

search = input('Введите искомое буквосочетание: ')

count = 0

for i in range(len(text)):
    if search.lower() == text[i:i + len(search)].lower():  # Срез
        count += 1

print(f'В заданном тексте буква "{search}" встречается {count} раз')
