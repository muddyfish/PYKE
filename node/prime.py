#!/usr/bin/env python

from nodes import Node
from node.sort import Sort
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
        has_newline = False
        for j, row in enumerate(seq):
            try:
                for i in row:
                    if isinstance(i, str) and "\n" in i:
                        has_newline = True
                        max_len = max(max_len, max(map(len, i.split("\n"))))
                    else:
                        max_len = max(max_len, len(str(i)))
                    pad |= (not isinstance(i,str)) or len(i)!=1
            except TypeError:
                seq[j] = [row]
        max_len += pad
        for row in seq:
            self.print_aligned(row, max_len, has_newline)
    
    def print_aligned(self, seq, max_len = None, has_newline = False):
        if max_len is None:
            max_len = 0
            for i in seq:
                if isinstance(i, str) and "\n" in i:
                    max_len = max(max_len, max(map(len, i.split("\n"))))
                    has_newline = True
                else:
                    max_len = max(max_len, len(str(i)))
            max_len += 1
        if has_newline:
            seq = zip(*[str(i).split("\n") for i in seq])
        else:
            seq = [seq]
        for j in seq:
            first = True
            for i in j:
                adjusted = str(i)
                if not first: adjusted = adjusted.rjust(max_len)
                print(adjusted,end="")
                first = False
            print()
        
    @Node.test_func(["HELLO"], [1])
    @Node.test_func(["World7"], [1])
    @Node.test_func(["@"], [0])
    def is_alpha_num(self, string:str):
        """Is a string alphanumeric?"""
        return int(string.isalnum())
    
    
    @Node.test_func([{1:1, "2":2}], [[1, '2']])
    def sort_values(self, dic:dict):
        """Return the keys of the dictionary in a list sorted by their values"""
        value_sort = Sort.sort_list(dic.values())
        sort = sorted(dic, key = lambda x:value_sort.index(dic[x]))
        return [sort]
    