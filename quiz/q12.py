my_list = []
value01 = 1

while len(my_list) < 5:
    value01 *= 2
    my_list.append(value01)
    my_list.append(value01 * 2)
    del my_list[0]

print(my_list)
