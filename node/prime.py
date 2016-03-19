#!/usr/bin/env python

from nodes import Node
from node.numeric_literal import NumericLiteral
import math

class Prime(Node):
    char = "P"
    args = 1
    results = 1
    checked = {0: False,
               1: False}
    factors = {0: [],
               1: []}
    contents = math.pi
    
    def prime(self, a: Node.number):
        a = int(a)
        if a<0:
            return self.is_prime(-a)
        return self.prime_factors(a)
    
    def is_prime(self, a):
        if a in Prime.checked:
            return Prime.checked[a]
        for i in range(2, int(a**.5)+1):
            if a%i==0:
                Prime.checked[a] = False
                return False
        Prime.checked[a] = True
        return True
    
    def prime_factors(self, a):
        if a in Prime.factors:
            return [Prime.factors[a]]
        if self.is_prime(a):
            return [[a]]
        factors = []
        for i in range(2, int(a**.5)+1):
            if a%i==0:
                factors.append(i)
                factors.extend(self.prime_factors(a//i)[0])
                break
        Prime.factors[a] = factors
        return [factors]