from collections import deque
from itertools import count, cycle

import lang_ast


class InfiniteList(object):
    def __init__(self):
        self._iter = None
        self.filters = []
        self.prepends = deque()

    def __repr__(self):
        rtn = ""
        for func, args, kwargs in self.filters:
            rtn += "<%s(*%s, **%s)>" % (func.__name__, args, kwargs)
        return rtn

    def __str__(self):
        while 1:
            print(next(self))
 
    def __iter__(self):
        return self

    def __next__(self):
        if self.prepends:
            return self.prepends.popleft()
        while 1:
            try:
                i = next(self._iter)
                for func, args, kwargs in self.filters:
                    i = func(i, *args, **kwargs)
                return i
            except RemovedError:
                pass

    def __getitem__(self, item):
        if isinstance(item, int):
            for i in range(item+1): rtn = next(self)
            return rtn
        return [next(self) for i in range(item.stop)]

    def modify(self, func, *args, **kwargs):
        self.filters.append((func, args, kwargs))
        return self

    def filter(self, i, ast):
        rtn = ast.run([i])
        if all(rtn):
            return i
        raise RemovedError

    def modify_code(self, i, code):
        ast = lang_ast.AST()
        ast.setup(code)
        rtn = ast.run([i])
        return rtn[0]

    def modify_filter(self, i, code):
        ast = lang_ast.AST()
        ast.setup(code)
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

    def node_map(self, i, combined):
        node, *args = combined
        rtn = node([i, *args])
        if len(rtn) == 1:
            rtn = rtn[0]
        return rtn

    def node_left_map(self, i, combined):
        node, *args = combined
        rtn = node([*args, i])
        if len(rtn) == 1:
            rtn = rtn[0]
        return rtn

    def prepend(self, value):
        self.prepends.appendleft(value)


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


class DummyList(InfiniteList):
    def __init__(self, iterator):
        super().__init__()
        self._iter = iterator

    def __repr__(self):
        return "<DummyList>"+super().__repr__()


class ModifyList(InfiniteList):
    def __init__(self, base: InfiniteList, code: str):
        super().__init__()
        self.base = base
        self.code = code
        self._iter = iter(base)
        self.modify(self.modify_code, code)

    def __repr__(self):
        rtn = "<modify({})>".format(repr(self.code))
        for func, args, kwargs in self.filters[1:]:
            rtn += "<%s(*%s, **%s)>" % (func.__name__, args, kwargs)
        return repr(self.base)+rtn


class FilterList(InfiniteList):
    def __init__(self, base: InfiniteList, code: str):
        super().__init__()
        self.base = base
        self.code = code
        self._iter = iter(base)
        self.modify(self.modify_filter, code)

    def __repr__(self):
        rtn = "<filter({})>".format(repr(self.code))
        for func, args, kwargs in self.filters[1:]:
            rtn += "<%s(*%s, **%s)>" % (func.__name__, args, kwargs)
        return repr(self.base)+rtn


class RemovedError(Exception):
    pass
