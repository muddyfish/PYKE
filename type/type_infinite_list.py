from itertools import count, cycle

class InfiniteList(object):
    def __init__(self):
        self._iter = None
        self.filters = []

    def __repr__(self):
        rtn = ""
        for func, args, kwargs in self.filters:
            rtn += "<%s(*%s, **%s)>" % (func.__name__, args, kwargs)
        return rtn

    def __str__(self):
        while 1:
            print(next(self))

    def __next__(self):
        while 1:
            try:
                i = next(self._iter)
                for func, args, kwargs in self.filters:
                    i = func(i, *args, **kwargs)
                return i
            except RemovedError:
                pass

    def modify(self, func, *args, **kwargs):
        self.filters.append((func, args, kwargs))
        return self

    def filter(self, i, ast):
        rtn = ast.run([i])
        if all(rtn):
            return i
        raise RemovedError

    def not_filter(self, i, ast):
        rtn = ast.run([i])
        if not any(rtn):
            return i
        raise RemovedError

    def every(self, i, every, count):
        if next(count) % every:
            raise RemovedError
        return i

    def not_every(self, i, every, count):
        if next(count) % every:
            return i
        raise RemovedError

    def ast_map(self, i, ast):
        rtn = ast.run([i])
        if len(rtn) == 1:
            rtn = rtn[0]
        return rtn

    def node_map(self, i, node):
        rtn = node([i])
        if len(rtn) == 1:
            rtn = rtn[0]
        return rtn


class CountList(InfiniteList):
    def __init__(self):
        super(CountList, self).__init__()
        self._iter = count()

    def __repr__(self):
        return "<CountList>"+super(CountList, self).__repr__()


class CycleList(InfiniteList):
    def __init__(self, lst):
        super(CountList, self).__init__()
        self._iter = cycle(lst)

    def __repr__(self):
        return "<CycleList>"+super(CountList, self).__repr__()


class IntegerList(InfiniteList):
    def __init__(self):
        super(IntegerList, self).__init__()
        self._iter = self.integers()

    def __repr__(self):
        return "<IntegerList>"+super(IntegerList, self).__repr__()

    def integers(self):
        i = 0
        yield i
        while 1:
            i += 1
            yield i
            yield -i


class NegativeList(InfiniteList):
    def __init__(self):
        super(NegativeList, self).__init__()
        self._iter = self.negatives()

    def __repr__(self):
        return "<NegativeList>"+super(NegativeList, self).__repr__()

    def negatives(self):
        i = 0
        while 1:
            yield i
            i -= 1


class RemovedError(Exception):
    pass
