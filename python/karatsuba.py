def karatsuba(first, second):
    """karatsuba"""
    first_1, first_2 = split_number(first)
    second_1, second_2 = split_number(second)
    num = get_number_bit(first)
    firsts = first_1 * second_1
    seconds = first_2 * second_2
    tmp = ((first_1 + first_2) * (second_1 + second_2)) - firsts - seconds
    return (10**num) * firsts + (10**(num/2))*tmp + seconds



def split_number(num):
    """spliting numbers into two parts"""
    num_bit = get_number_bit(num)
    first = str(num)[:num_bit /2]
    second = str(num)[num_bit/2:]
    return int(first), int(second)

def get_number_bit(num):
    """gets number range"""
    return len(str(num))

if __name__ == '__main__':
    print karatsuba(49823261, 44269423) == 49823261 * 44269423
