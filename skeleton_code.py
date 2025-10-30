# Task 1: Flatten a list
def task1(input_list: list) -> list:
    # implement your code here
    ...

# Task 2: Convert hex string to decimal number
def task2(s: str) -> int:
    # implement your code here
    ...

# You can use these 2 functions in task 3!
from math import gcd, lcm

# Task 3: Dealing with fractions
class Fraction:
    
    def __init__(self, numer: int = 1, denom: int = 1):
        self.numer: int = numer
        self.denom: int = denom
        
    # Task 3.1: fraction addition
    def __add__(self, other):
        # implement your code here
        ...
        
    # Task 3.2: fraction subtraction
    def __sub__(self, other):
        # implement your code here
        ...
        
    # Task 3.3: fraction multiplication
    def __mul__(self, other):
        # implement your code here
        ...
        
    # Task 3.4: fraction division
    def __truediv__(self, other):
        # implement your code here
        ...

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom
    
    # this is the meaning of "inverted in some way"
    def __ne__(self, other):
        return not self == other
    
    # for print()
    def __str__(self):
        return f"{self.numer}/{self.denom}"

###################
# Separation Line #
###################

if __name__ == "__main__":
    # Task 1 test cases
    assert task1([[1,2], [3,4], [5,6,7]]) == [1,2,3,4,5,6,7], "Your task 1 implementation is wrong!"
    
    # Task 2 test cases
    assert task2("dEADbEef") == 3735928559, "Your task 2 implementation is wrong!"
    assert task2("iloveict") == 236, "Your task 2 implementation is wrong!"
    
    # Task 3 test cases
    a = Fraction(1, 2)
    b = Fraction(2, 3)
    assert a + b == Fraction(7, 6), "Your task 3.1 implementation is wrong!"
    assert b - a == Fraction(1, 6), "Your task 3.2 implementation is wrong!"
    assert a * b == Fraction(1, 3), "Your task 3.3 implementation is wrong!"
    assert a / b == Fraction(3, 4), "Your task 3.4 implementation is wrong!"
    
    print("Epic, you passed all given testcases!")