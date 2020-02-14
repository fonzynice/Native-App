# def square_digits(num):
#     num_to_string = str(num)  # change int to string
#     string_to_list = list(num_to_string)   # change string to list
#     for new_num in string_to_list:
#         sqr = int(new_num) ** 2   # change each list element to int
#         print(sqr, end='')
#
# square_digits(9119)


# def sq(num):
#     words = list(str(num)) # split the text
#     for word in words:  # for each word in the line:
#         print(int(word)**2, end="") # print the word
#
# num = 9119
# sq(num)num

num_list = [1, 2, 3]


# def square_sum(numbers):
#     return sum(map(lambda x: x ** 2, numbers))
#
#
# result = square_sum(num_list)
# print(result)


def add(a, b):
    return a + b


def sum_str(a, b):
    return int(a) + int(b)


# result = sum_str(5, 3)
# print(str(result))


def multiply(a, b):
    return a * b


t = [1, 2, 3, 4, 5, 6]


# l = list(filter(lambda x: (x % 2 == 0), t))
# print(l)


def divisible_by(numbers, divisor):
    return list(filter(lambda x: x % divisor == 0, numbers))


# results = divisible_by([1, 2, 3, 4, 5, 6], 2)
# print(results)


# b = 2
# my_list = [1, 2, 3]


def check(a, x):
    if list(filter(lambda a: a == x, a)):
        return True
    else:
        return False


# results = check([1, 2, 3], 2)
# print(results)


def reverse_seq(n):
    # l = list(map(lambda x: x, range(1,6)))
    # return list(reversed(l))
    # return list(reversed([x for x in range(1, n + 1)]))
    my_list = [x for x in range(1, n+1)]
    return list(reversed(my_list))


# result = reverse_seq(5)
# print(result)


def no_space(x):
    """Remove all whitespace in the string"""
    return x.replace(" ", "")



result = no_space('my name is Bond')
print(result)