from nodes import Node

class Chr(Node):
    char = ".C"
    args = 1
    results = 1

    def chr(self, num:int):
        """chr(int)"""
        rtn = []
        while num > 256:
            num, new = divmod(num, 256)
            rtn.append(chr(new))
        rtn.append(chr(num))
        return "".join(rtn[::-1])

    def map_chr(self, lst:Node.sequence):
        """map(chr, list)"""
        return "".join(chr(i)for i in lst)