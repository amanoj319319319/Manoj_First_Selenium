import pytest
import math

def test_sqrt_failure():
   num=36
   assert math.sqrt(num) == 6
   print ("test_sqrt_failure has passed")

def test_square_failure():
   num=7
   assert 7*7 == 48
   print ("test_square_failure has passed")

def test_equality_failure():
   assert 10 == 11
