# Find the minimum value in a list of integers

def get_min_value(in_list):
    if len(in_list) == 0:
        return None

    if len(in_list) == 1:
        return in_list[0]

    min_value = in_list[0]
    for value in in_list:
        if value < min_value:
            min_value = value

    return min_value


def get_max_value(in_list):
    if len(in_list) == 0:
        return None

    if len(in_list) == 1:
        return in_list[0]

    max_value = in_list[0]
    for value in in_list:
        if value > max_value:
            max_value = value

    return max_value
