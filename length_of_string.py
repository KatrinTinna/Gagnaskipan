def length_str(string: str):
    if len(string) == 0:
        return 0
    return 1 + length_str(string[1:])


def linear_search(a_list: list, value):
    if a_list == []:
        return False
    if a_list[0] == value:
        return True
    else:
        return linear_search(a_list[1:], value)


def count_instances(a_list: list, value):
    if a_list == []:
        return 0
    if a_list[0] == value:
        return 1 + count_instances(a_list[1:], value)
    else:
        return count_instances(a_list[1:], value)


def duplicates(a_list: list):
    if a_list == []:
        return False

    if linear_search(a_list[1:], a_list[0]):
        return True

    return duplicates(a_list[1:])


def remove_duplicates(a_list: list) -> list:
    if a_list == []:
        return []
    if linear_search(a_list[1:], a_list[0]):
        return remove_duplicates(a_list[1:])
    return [a_list[0]] + remove_duplicates(a_list[1:])


x = [1, 2, 3, 3, 4, 5]
print(remove_duplicates(x))


def binary_search(a_list: list, value):
    if a_list == []:
        return False
    elif value == a_list[(len(a_list) // 2)]:
        return True

    elif value < a_list[len(a_list) // 2]:
        return binary_search(a_list[: len(a_list) // 2], value)
    else:
        # Skoða þessa línu aðeins betur
        return binary_search(a_list[(len(a_list) // 2) + 1 :], value)


# x = [0, 1, 3, 4, 5, 6,7]
# for i in range(0, 10):
#     print(binary_search(x, i))
# # print([1, 2, 3][1 + 1 :])


def prefix(a_prefix: str, a_str: str):
    if a_str == "":
        return False
    elif a_prefix[0] == a_str[0]:
        return prefix(a_prefix[1:], a_str[1:])
    else:
        return False


def is_prefix(prefix, a_str):
    if len(prefix) == 0:
        return True
    if len(a_str) == 0:
        return False
    if prefix[0] != a_str[0]:
        return False
    return is_prefix(prefix[1:], a_str[1:])


def is_substring(substring: str, a_str: str):
    if len(substring) == 0:
        if len(a_str) == 0:
            return True
        else:
            return False
    if len(a_str) == 0:
        return False
    if is_prefix(substring, a_str):
        return True
    else:
        return is_substring(substring, a_str[1:])


def x_ish(a_str, x):
    if a_str == "":
        return False
    if len(x) == 0:
        return True
    if a_str[0] == x[0]:
        return x_ish(a_str, x[1:])
    else:
        # return x_ish(a_str[1:], x)
        return x_ish(a_str, x[1:])


print(x_ish("gagnaskipan", "gnAsk"))


def bar(n, m):
    if m == 0:
        return 1
    return n * bar(n, m - 1)


print(bar(2, 2))


def palindrome(a_str: str):
    if a_str == "":
        return True
    if a_str[0] == a_str[len(a_str) - 1]:
        return palindrome(a_str[1 : len(a_str) - 1])
    else:
        return False
