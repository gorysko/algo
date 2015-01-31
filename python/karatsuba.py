"""Karatsuba algo implementation"""

__author__ = "gorysko@gmail.com"
__description__ = "Karatsuba multiplication implementation for pronetheus"

def karatsuba(first, second):
    """karatsuba algo"""
    if first < 10 or second < 10:
        return first * second
    num = max(get_range(first), get_range(second))
    num_2 = num / 2
    first_a, first_b = split_num(first)
    second_c, second_d = split_num(second)
    firsts = karatsuba(first_a, second_c)
    seconds = karatsuba(first_b, second_d)

    thirds = karatsuba((first_a + first_b), (second_d + second_c)) - \
        firsts - seconds
    return  ((10**(2*num_2))*firsts)+((10**num_2)*thirds) + seconds


def get_range(num):
    """Gets number range"""
    return len(str(num))

def split_num(num):
    """splits number into two parts"""
    num_range = int(round(get_range(num) / 2.0))
    num = str(num)
    return int(num[:num_range]), int(num[num_range:])
