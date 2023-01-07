my_str = '3*x**2 - 12x + 6 = 0'
my_str = my_str[:-4].replace(' ', '').replace('*x**2', '').replace('*x', '').replace('-', '+-').split('+')
my_list = []
for i in my_str:
    if i.startswith('x'):
        my_list.append(1)
    elif i.startswith('-x'):
        my_list.append(-1)
    else:
        my_list.append((i[0]))

print(my_str)
print(my_list)
