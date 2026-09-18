"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def quadratic_multiply(x, y):
    if isinstance(x, BinaryNumber):
        x = x.binary_vec
    if isinstance(y, BinaryNumber):
        y = y.binary_vec
    if len(x) == 1:
        return int(x[0]) * int(y[0])
    length = max(len(x), len(y))
    size = 1
    while size < length: #making lengths equal to a power of 2 for easier splitting
        size *= 2
    x = [0] * (size - len(x)) + x
    y = [0] * (size - len(y)) + y 
    xl = x[:len(x)//2]
    xr = x[len(x)//2:]
    yl = y[:len(y)//2]
    yr = y[len(y)//2:]
    p1 = quadratic_multiply(xl, yl)
    p2 = quadratic_multiply(xl, yr)
    p3 = quadratic_multiply(xr, yl)
    p4 = quadratic_multiply(xr, yr)
    return p1 * (2 ** len(x)) + (p2 + p3) * (2 ** (len(x) // 2)) + p4
    
def subquadratic_multiply(x, y):
    if isinstance(x, BinaryNumber):
        x = x.binary_vec
    if isinstance(y, BinaryNumber):
        y = y.binary_vec
    if len(x) == 1:
        return int(x[0]) * int(y[0])
    length = max(len(x), len(y))
    size = 1
    while size < length: #making lengths equal to a power of 2 for easier splitting
        size *= 2
    x = ['0'] * (size - len(x)) + x
    y = ['0'] * (size - len(y)) + y 
    xl = x[:len(x)//2]
    xr = x[len(x)//2:]
    yl = y[:len(y)//2]
    yr = y[len(y)//2:]
    p1 = quadratic_multiply(xl, yl)
    p2 = quadratic_multiply(xr, yr)
    sum_x = BinaryNumber(int(''.join(xl), 2) + int(''.join(xr), 2))
    sum_y = BinaryNumber(int(''.join(yl), 2) + int(''.join(yr), 2))
    p3 = subquadratic_multiply(sum_x, sum_y)
    return (p1 * (2 ** len(x))) + (p3 - p1 - p2) * (2 ** (len(x) // 2)) + p2

def time_multiply(x, y, f):
    start = time.time()
    f(x, y)
    return (time.time() - start)*1000
    
def compare_multiply(x, y):
    return time_multiply(x, y, quadratic_multiply(x, y) - subquadratic_multiply(x, y))
    
    

