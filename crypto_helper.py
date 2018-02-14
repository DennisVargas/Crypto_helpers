#!/usr/bin/python3
""" 
Provides a number of crypto helper functions
"""

class CryptoHelper():
  """[
    Class holding helper functions]
  """
  def greatest_common_divisor(self,a,b):
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