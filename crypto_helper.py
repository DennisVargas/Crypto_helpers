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
    a {[int]} -- [any integer positive or negative]
    b {[int]} -- [any integer positive or negative]
    """
    a = abs(a)
    b = abs(b)
    while b != 0:
        temp_value = b
        b = a % b
        a = temp_value
    return a


def multiplicative_inverse_factors(a_value, m_modulus):
    """[Summary: Returns a list of all the values of 'x'
        that solve the equation 'ax mod n = 1'.]

    Arguments:
    a_value {[int]} -- [description]
    m_modulus {[int]} -- [description]
    """
    mult_inverse_list = list()
    for test_mult_inverse in range(1, m_modulus):
        b_product = test_mult_inverse*a_value
        mod_result = b_product % m_modulus
        print(a_value, "*", test_mult_inverse, " mod ", m_modulus,
              " = ", mod_result)
        if mod_result == 1:
            print("SOLUTION FOUND!", test_mult_inverse)
            mult_inverse_list.append(test_mult_inverse)
    # print("number of factors:"+str(len(x_result)))
    # print("list of factors:"+str(x_result))
    return mult_inverse_list


def eulers_totient_coprime_list(n_limit):
    """[returns a list of the coprimes from 1...n_limit.
        A number is coprime to n_limit when
        greatest_common_divisor ("iterator in range", n_limit) returns 1]

    Arguments:
        n_limit {[int]} -- [limit at which the function stops
                            counting and searching coprimes]

    Returns:
        [list] -- [list of the values co-prime to the  n_limit]
    """
    list_of_coprimes = list()
    for i in range(0, n_limit):
        gcd = greatest_common_divisor(i, n_limit)
        if gcd == 1:
            list_of_coprimes.append(i)
    return list_of_coprimes


def set_multiplicative_inverse_to_n(a_values, m_modulus):
    """[iterates through a set of a_values and returns a dictionary
         of the solutions for "a_value*x_value mod n_limit".
         i.e. {a_value:[multiplicative inverse to n]} ]

    Arguments:
        a_values {[list]} -- [list holding the values
                                which will be tested for multiplicative
                                inverse values to n]
        n {[int]} -- [value ]

    Returns:
        [dictionary] -- [a_value: ]
    """
    mult_inverse_dict = dict()
    for a_value in a_values:
        mult_inverse_dict.update({a_value:
                                  multiplicative_inverse_factors(a_value,
                                                                 m_modulus)})
    return mult_inverse_dict


# if __name__ == '__main__':
#     COPRIME_LIST = eulers_totient_coprime_list(16)
#     print(COPRIME_LIST)
#     print(set_multiplicative_inverse_to_n(COPRIME_LIST, 16))
