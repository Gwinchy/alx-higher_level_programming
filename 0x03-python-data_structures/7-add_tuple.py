#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)  # Extend tuple_a to at least 2 elements
    b = tuple_b + (0, 0)  # Extend tuple_b to at least 2 elements
    return (a[0] + b[0], a[1] + b[1])
