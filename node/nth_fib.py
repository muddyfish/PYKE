from nodes import Node
from math import sqrt
import decimal
decimal.getcontext().prec = 100

class Fib(Node):
    char = ".b"
    args = 1
    results = 1
    
    root_5 = decimal.Decimal(5)**(1/decimal.Decimal(2))    
    
    @Node.test_func([0], [0])
    @Node.test_func([1], [1])
    @Node.test_func([2], [1])
    @Node.test_func([3], [2])
    @Node.test_func([4], [3])
    def func(self, n_th: int):
        """Returns the nth fibonacci number"""
        return int(((1+Fib.root_5)**n_th-(1-Fib.root_5)**n_th)/(2**n_th*Fib.root_5))