#!/usr/bin/env python

import datetime

import ephem

from nodes import Node


class Index(Node):
    char = "@"
    args = 2
    results = 1
    
    @Node.test_func(["tes", 1], ["e"])
    @Node.test_func([[1, 2, 3], -1], [3])
    def at(self, a: Node.indexable, b:int):
        """a[b]"""
        return[a[b % len(a)]]

    @Node.test_func([2, {1: 2,2: 3}], [3])
    @Node.test_func(["hello", {"hello":"world"}], ["world"])
    @Node.prefer
    def dict_at(self, a, b:dict):
        """return b[a]"""
        return[b[a]]
    
    @Node.test_func([1, [1,2,3]], [0])
    @Node.test_func([3, [1,2,3]], [2])
    @Node.test_func([4, [1,2,3]], [-1])
    @Node.test_func(["e", "hello"], [1])
    @Node.test_func(["?", "hello"], [-1])
    @Node.prefer
    def index(self, a, b: Node.indexable):
        """b.index(a)"""
        if isinstance(b, str):
            return b.find(a)
        try:
            return b.index(a)
        except ValueError:
            return -1
    
    @Node.test_func([2, 0], [3])
    @Node.test_func([1, 2], [5])
    def set_bit(self, a: int, b: int):
        """Set bit b in a"""
        return a | (2**b)

    def inf_at(self, inf: Node.infinite, nth: int):
        while nth != 0:
            next(inf)
            nth -= 1
        return next(inf)

    def inf_at_2(self, nth: int, inf: Node.infinite):
        return self.inf_at(inf, nth)

    @Node.prefer
    def get_distance_to_earth(self, time: Node.clock, object: str):
        """Gets the distance to the Earth from `object`"""
        new_time = datetime.datetime(*time.time_obj[:7])
        try:
            return getattr(ephem, object)(new_time).earth_distance
        except AttributeError:
            with open("astro_db.txt") as astro_db:
                name = ""
                line = astro_db.readline()
                while name.lower() != object.lower():
                    assert line.startswith("* ")
                    name, launch_date, updated_date = line[2:].split(":")
                    name = name[:-9]
                    if name.lower() != object.lower():
                        line = astro_db.readline()
                        while line[0] != "*" or line.startswith("* Good from "):
                            line = astro_db.readline()
                year = int(astro_db.readline()[-5:])
                while year < new_time.year:
                    astro_db.readline()
                    line = astro_db.readline()
                    line = line.split("  (")[0]
                    year = int(line[-4:])
                line = astro_db.readline()
            object = ephem.readdb(line)
            object.compute(new_time)
            return object.earth_distance
