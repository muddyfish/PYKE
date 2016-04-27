#!/usr/bin/env python

from nodes import Node
import math

class Prime(Node):
    char = "P"
    args = 1
    results = 1
    checked = {0: 0,
               1: 0}
    factors = {0: [],
               1: []}
    contents = math.pi
    
    @Node.test_func([-5], [1])
    @Node.test_func([-1], [0])
    @Node.test_func([-8], [0])
    @Node.test_func([18], [[2,3,3]])
    def prime(self, a: int):
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
    
    def print_grid(self, seq: Node.sequence):
        """Print a 2D grid with padding equal to the maximum length
Or print a 1D list with padding equal to the maximum length"""
        self.results = 0
        if len(seq) == 0:
            print()
            return
        if not isinstance(seq[0], Node.sequence):
            return self.print_aligned(seq)
        max_len = 0
        pad = 0
        for j, row in enumerate(seq):
            try:
                for i in row:
                    max_len = max(max_len, len(str(i)))
                    pad |= (not isinstance(i,str)) or len(i)!=1
            except TypeError:
                seq[j] = [row]
        max_len += pad
        for row in seq:
            self.print_aligned(row, max_len)
    
    def print_aligned(self, seq, max_len = None):
        if max_len is None:
            max_len = max(len(str(i))for i in seq)+1
        first = True
        for i in seq:
            print(str(i).rjust(max_len)[first:],end="")
            first = False
        print()