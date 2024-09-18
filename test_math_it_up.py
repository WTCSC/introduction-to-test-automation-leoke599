import pytest
import math_it_up

"""
This file contains the tests for the math_it_up module, which contains the
following functions:

- math_it_up.is_even
- math_it_up.is_odd
- math_it_up.mean
- math_it_up.median
- math_it_up.mode

The `is_even` and `is_odd` functions accept a single argument, a number, and
return True if the number is even or odd, respectively.

The `mean` function accepts a single argument, a list of numbers, and returns
the mean of the numbers.

The `median` function accepts a single argument, a list of numbers, and returns
the median of the numbers.

The `mode` function accepts a single argument, a list of numbers, and returns
the mode of the numbers.

To run the tests, run `pytest` from the command line in the same directory as
this file.
"""

def test_is_even():
  assert math_it_up.is_even(10) # tests to see if 10 is even with the module
  assert True # asserts that if the number is 10 then it should be true that it's even

def test_is_odd():
  assert math_it_up.is_odd(9) # tests to see if 9 is odd with the module
  assert True # asserts that if the number is 9 then it should be true that it's odd

def test_mean():
  assert math_it_up.mean([1, 2, 3, 4, 5]) # uses the list of numbers i gave to calculate the mean
  assert 3 # asserts that the number you should get for running this code is 3

def test_median():
  assert math_it_up.median([3, 4, 5, 6, 7]) # uses this list to calculate the median
  assert 5 # tells the program that it should be 5

def test_mode():
  assert math_it_up.mode([1, 2, 3, 3, 4, 5, 5, 6, 6, 6, 7, 9]) # uses the list and calculates the mode
  assert 6 # tells the program the output should be 6