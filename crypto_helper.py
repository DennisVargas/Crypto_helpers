#!/usr/bin/python3
""" Provides a number of crypto helper functions """


def greatest_common_divisor(a, b):
    """[
    Summary:
    Returns the largest number which divides
    integers 'a' and 'b'. If 'b' is equal to 0 then
    'a' is returned. Arguments calculated as absolute value.
    Implements Euclid's algorithm;
    https://en.wikipedia.org/wiki/Euclidean_algorithm#Implementations]
    Arguments:
    a {[int]} -- [any integer positivie or negative]
    b {[int]} -- [any integer positive or negative]
    """
    a = abs(a)
    b = abs(b)
    while b != 0:
        temp_value = b
        b = a % b
        a = temp_value
    return a


def list_multiplicative_inverse_factors(a, n):
    """[
    Summary:
    Returns a list of all the values of 'x'
    that solve the equation 'ax mod n = 1'.]

    Arguments:
    a {[int]} -- [description]
    n {[int]} -- [description]
    """
    x_result = list()
    for x in range(1, n):
        b = x*a
        c = b % n
        print(a, "*", x, " mod ", n, " = ", c)
        if c == 1:
            print("SOLUTION FOUND!", x)
            x_result.append(x)
    print("number of factors:"+str(len(x_result)))
    print("list of factors:"+str(x_result))
    return x_result


def eulers_totient_coprime_list(n):
    list_of_coprimes = list()
    for i in range(0, n):
        gcd = greatest_common_divisor(i, n)
        if gcd == 1:
            list_of_coprimes.append(i)
    return list_of_coprimes
# if __name__ == '__main__':
