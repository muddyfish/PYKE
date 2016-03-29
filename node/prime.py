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
    
    @Node.test_func([-5], [1])
    @Node.test_func([-1], [0])
    @Node.test_func([-8], [0])
    @Node.test_func([18], [[2,3,3]])
    def prime(self, a: Node.number):
        """If is_neg(a): return is_prime(a)
Else: return prime_factors(a)"""
        a = int(a)
        if a<0:
            return self.is_prime(-a)
        return self.prime_factors(a)
    
    def is_prime(self, a):
        if a in Prime.checked:
            return Prime.checked[a]
        for i in range(2, int(a**.5)+1):
            if a%i==0:
                Prime.checked[a] = 0
                return 0
        Prime.checked[a] = 1
        return 1
    
    def prime_factors(self, a):
        """Return prime factors of a"""
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