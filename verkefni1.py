import random


# Power
def power(base: int, power: int) -> int:
    ret_val = 1
    for i in range(power):
        ret_val *= base
    return ret_val


# The time complexity is O(n)
# N in regard to the time complexity is the value of power


# Multiplication of positive integers.
def mult(num1: int, num2: int) -> int:
    ret_val = 0
    for i in range(num2):
        ret_val += num1
    return ret_val


# The time complexity is O(n)
# N in regard to the time complexity is the value of the num2


# Random number insertion
def num_insert(size: int) -> list:
    lis = [0] * size
    # counter = 0
    for i in range(size):
        rand_num = random.randint(1, 6)
        lis[i] = rand_num
        # lis[counter] = rand_num
        # counter += 1
    return lis


# The time complexity is O(n)
# N in regard to the time complexity is the value of the size of the list.


# Print list
def print_list(lis: list) -> None:
    length = len(lis)
    counter = 0
    for i in lis:
        if counter != length - 1:
            print(f"{i}, ", end="")
        else:
            print(i)
        counter += 1


# The time complexity is O(n)
# N in regard to the time complexity is the size of the list.


# Increase numbers at random index.
def increase_index(a_list: list) -> list:
    max_num = len(a_list)

    index_to_change = random.randint(0, max_num - 1)
    print(index_to_change)
    a_list[index_to_change] += 1
    return a_list


# The time complexity is O(1)


# Switch items in list
def switch_normal(index: int, list: list) -> list:
    index -= 1
    length = len(list)
    if index + 1 != length:
        # first_to_change = list[index]
        # list[index] = list[index + 1]
        # list[index + 1] = first_to_change
        list[index], list[index + 1] = list[index + 1], list[index]
    else:
        first_to_change = list[index]
        second_to_change = list[0]
        list[0] = first_to_change
        list[index] = second_to_change
    return list


# The time complexity is O(1)


def switch_random(list: list) -> list:
    length = len(list)
    random_num1 = random.randint(0, length - 1)
    random_num2 = random.randint(0, length - 1)
    # first_to_change = list[random_num1]
    # list[random_num1] = list[random_num2]
    # list[random_num2] = first_to_change
    list[random_num1], list[random_num2] = list[random_num2], list[random_num1]
    return list


# The time complexity is O(1)


# Ordered insertion
def order_insert(a_list: list) -> list:
    random_num = random.randint(1, 6)
    print(random_num)
    sorted_list = sorted(a_list)
    for i, value in enumerate(sorted_list):
        if value <= random_num and sorted_list[i + 1] >= random_num:
            sorted_list.insert(i + 1, random_num)
            return sorted_list


# The time complexity is O(n)


# Combined insertion and ordering
def make_random_list():
    my_list = []
    for i in range(8):
        num = random.randint(0, 20)
        my_list.append(num)
    return my_list


def combine_order(my_list):
    new_ordered_list = []
    lowest_curr_value = 0
    lowest_value = 0
    counter = 0
    for i in my_list:
        lowest_curr_value = i
        if counter == 0:
            for i in my_list:
                if i <= lowest_curr_value:
                    lowest_value = i

        else:
            for i in my_list:
                if lowest_value <= i:
                    lowest_curr_value = i
        new_ordered_list.append(lowest_curr_value)
    return new_ordered_list


my_list = make_random_list()
print(my_list)
new_ordered_list = combine_order(my_list)
print(new_ordered_list)


my_list = [1, 2, 5, 6]

# my_list = num_insert(3)
# print_list(my_list)
# a_list = increase_index(my_list)
print(my_list)
# index = int(input())
# list = order_insert(my_list)
list = switch_random(my_list)
print(list)
