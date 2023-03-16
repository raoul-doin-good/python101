from min_max import get_min_value


def sort_two_elements(two_elements):
    if two_elements[0] > two_elements[1]:
        temp = two_elements[0]
        two_elements[0] = two_elements[1]
        two_elements[1] = temp
    return two_elements


def sort_list(in_list):
    end = len(in_list) - 1
    while end > 0:
        position = 0
        while position != end:
            in_list[position:position +
                    2] = sort_two_elements(in_list[position:position+2])
            position += 1
        end -= 1

    return in_list


def sort_list2(in_list):
    out_list = []
    while len(in_list) > 0:
        min_value = get_min_value(in_list)
        out_list.append(min_value)
        in_list.remove(min_value)
    return out_list


def sort_by_list(in_list, positions):
    out_list = in_list[:]
    position = 0
    while position < len(in_list):
        out_list[positions[position]] = in_list[position]
        position += 1
    return out_list
