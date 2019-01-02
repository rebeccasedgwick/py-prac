# fibonacci basic
def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


# print sequence up to given value, n
def fibonacci_to_value(n):
    x, y = 0, 1
    while x <= n:
        print(x, end=" ")
        x, y = y, x + y


def fibonacci_to_value_2(n):
    for i in fibonacci():
        if i > n:
            return
        else:
            yield i


for i in fibonacci_to_value_2(20):
    print(i, end=" ")


# print sequence to a given length:
def fibonacci_len(len):
    x, y = 0, 1
    count = 0
    while count < len:
        print(x, end=" ")
        x, y = y, x + y
        count += 1


# print values in a given range
def fibonacci_in_range(start_num, end_num):
    for i in fibonacci():
        if i > end_num:
            return
        if i >= start_num:
            yield i


for i in fibonacci_in_range(10, 1000):
    print(i, end=" ")
