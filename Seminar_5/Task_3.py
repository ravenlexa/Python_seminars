from random import randint as RI

my_list = [RI(1, 20) for i in range(20)]
print(my_list)
new_list = []
for i in range(len(my_list)):
    current = my_list[i]
    sub_list = [current]
    for j in range(i + 1, len(my_list)):
        if current + 1 == my_list[j]:
            sub_list.append(my_list[j])
            current += 1
    if len(sub_list) >= 2:
        new_list.append(sub_list)
print(new_list)
