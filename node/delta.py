#!/usr/bin/env python

import datetime

from nodes import Node


class Delta(Node):
    char = "$"
    args = 1
    results = 1
    contents = ["PADDING",
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"]
    
    @Node.test_func([[1, 2, 3, 5]], [[1, 1, 2]])
    def delta(self, seq: Node.sequence):
        """Return the difference in terms in the input sequence.
Returns a sequence of the same type, one shorter."""
        deltas = []
        for i in range(len(seq)-1):
            deltas.append(seq[i+1]-seq[i])
        return[type(seq)(deltas)]
    
    def float(self, inp:Node.number):
        """float(inp)"""
        return float(inp)

    @Node.test_func(["HELLO"], [0])
    @Node.test_func(["world"], [1])
    @Node.test_func(["@"], [0])
    def is_lower(self, string:str):
        """Is a string lower case?"""
        return int(string.islower())

    def get_day_of_week(self, time: Node.clock):
        new_time = datetime.datetime(*time.time_obj[:7])
        return new_time.weekday()
