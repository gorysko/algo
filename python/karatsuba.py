COUNTER = 0

def karatsuba(first, second):
    """karatsuba algo"""
    num = max(get_range(first), get_range(second))
    num_2 = num / 2
    if get_range(first) < 3 or get_range(second) < 3:
        return first * second
    first_a, first_b = split_num(first)
    second_c, second_d = split_num(second)
    firsts = karatsuba(first_a, second_c)
    seconds = karatsuba(first_b, second_d)
    thirds = karatsuba(first_a, second_d) + \
        karatsuba(first_b, second_c)
    return  ((10**num)*firsts)+((10**num_2)*thirds) + seconds



def get_range(num):
    """Gets number range"""
    return len(str(num))

def split_num(num):
    """splits number into two parts"""
    num_range = int(round(get_range(num) / 2.0))
    num = str(num)
    return int(num[:num_range]), int(num[num_range:])

if __name__ == '__main__':
    print karatsuba(49823261, 44269423)
    print 2205647016448403
