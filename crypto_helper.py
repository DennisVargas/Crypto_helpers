#!/usr/bin/python3
""" 
a module which provides a number of crypto helper functions
"""

class CryptoHelper():
  """[Class holding helper functions]
  """
  def greatest_common_divisor(self,a,b):
    """[Summary:
          Returns the largest number which divides 
          integers 'a' and 'b'. If 'b' is equal to 0 then 
          'a' is returned. Arguments calculated as absolute value.]
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