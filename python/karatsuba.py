def karatsuba(first, second):
    a , b = split_number(first)
    c, d = split_number(second)
    n = get_number_bit(first)
    ac = a * c
    bd = b * d
    tmp = ((a + b) * (c + d)) - ac -bd
    result = (10**n) * ac + (10**(n/2))*tmp + bd
    return result



def split_number(num):
    num_bit = get_number_bit(num)
    first = str(num)[:num_bit /2]
    second = str(num)[num_bit/2:]
    return int(first), int(second)

def get_number_bit(num):
    return len(str(num))

if __name__ == '__main__':
    print karatsuba(49823261, 44269423) == 2205647016448403
