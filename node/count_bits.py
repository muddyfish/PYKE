from nodes import Node

class CountBits(Node):
    char = "./"
    args = 2
    results = 1
    contents = 2000
            
    @Node.test_func([8,2], [[1, 3]])
    @Node.test_func([12, 3], [[0, 2, 1]])
    def count_bits(self, num: int, base: int):
        """Count the number of times each digit occurs in `base`"""
        counts = [0 for i in range(base)]
        
        while num != 0:
            num, remainder = divmod(num, base)
            counts[base-remainder-1] += 1
        return [counts]
