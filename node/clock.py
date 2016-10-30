#!/usr/bin/env python

from nodes import Node
import datetime
import time
from type.type_time import TypeTime


class Time(Node):
    char = "C"
    args = 0
    results = 0
    default_arg = -1
    datetime_attrs = ["second",
                      "minute",
                      "hour",
                      "day",
                      "month",
                      "year",
                      "2dyear"]
    date_attrs = ["weekday",
                  "isocalendar"]

    months = ["PADDING",
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
    
    contents = ["Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday"]
    
    def __init__(self, methods: Node.NumericLiteral):
        if methods == -1:
            self.func = self.get_time
            self.results = 1
        else:
            self.methods = [int(i)for i in str(methods)]
            self.results = len(self.methods)
        
    now = datetime.datetime.now()
    @Node.test_func([], [now.date().weekday(), now.year, now.day], "075")  
    def func(self):
        """Default - time.time()
0 - weekday - 0 based. Monday is 0, Sunday is 6.
1 - isocalendar
2 - seconds
3 - minutes
4 - hours
5 - days
6 - months
7 - year (full)
8 - year (tens and units)
9 - Months of the year (1 indexed, 0 is "PADDING")
Default contents: days of the week"""
        date_time = datetime.datetime.now()
        rtn = []
        for meth in self.methods:
            added = False
            if not added and meth < len(self.date_attrs):
                added = True
                rtn.append(getattr(date_time.date(), self.date_attrs[meth])())
            meth -= len(self.date_attrs)
            if not added and meth < len(self.datetime_attrs):
                added = True
                if self.datetime_attrs[meth] == "2dyear":
                    rtn.append(date_time.year%100)
                else:
                    rtn.append(getattr(date_time, self.datetime_attrs[meth]))
            
            if not added:
                rtn.append(self.months)
        return rtn

    def get_time(self):
        return [TypeTime(time.gmtime())]
    
    @classmethod
    def reset_tests(cls):
        now = datetime.datetime.now()
        cls.func.tests = [[[], [now.date().weekday(), now.year, now.day], "075"]]