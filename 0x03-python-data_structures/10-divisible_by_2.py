#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [num % 2 == 0 for num in my_list]


list_result = divisible_by_2()


i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
