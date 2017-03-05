#!/usr/bin/env python

import datetime

from nodes import Node


class Dict(Node):
    char = "Y"
    args = 1
    results = 1
    contents = 256
        
    @Node.test_func([[["test", 2], [2,3]]], [{"test":2,2:3}])
    def func(self, a: Node.sequence):
        """Turn a sequence into a dict. If that fails, take the mean"""
        try:
            return dict(a)
        except TypeError:
            return sum(a) / len(a)

    def digits(self, num: int):
        return [[int(i) for i in str(num)]]

    def get_day_of_year(self, time: Node.clock):
        new_time = datetime.datetime(*time.time_obj[:7])
        return new_time.timetuple().tm_yday
