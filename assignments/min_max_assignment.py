# Schreibe eine Funktion, die das größte Element einer Liste von Zahlen zurückgibt.

# def get_maximum(my_list):
#    return  # ???

# get_maximum([1]) -> 1
# get_maximum([1, 2, 3]) -> 3
# get_maximum([1, 2, -3]) -> 2

my_list = [1, 12, 127, 5]
print(sorted(my_list)[-1])
print(max(my_list))
print(min(my_list))
