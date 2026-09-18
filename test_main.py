from main import *

# Feel free to expand and add your own tests here.
# Doing so won't impact the gradescope autograder tests (gradescope uses
# its own copy of this file so any changes you make here won't affect it).

# 5 pts
def test_quadratic_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(2)) == 4*2
    assert quadratic_multiply(BinaryNumber(6), BinaryNumber(7)) == 6*7
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(11)) == 3*11

# 5 pts
def test_subquadratic_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply(BinaryNumber(6), BinaryNumber(2)) == 6*2
    assert subquadratic_multiply(BinaryNumber(9), BinaryNumber(3)) == 9*3
    assert subquadratic_multiply(BinaryNumber(7), BinaryNumber(4)) == 7*4