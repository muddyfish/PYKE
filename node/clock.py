#!/usr/bin/env python

from nodes import Node
import datetime
import time

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
            self.func = lambda: time.time()
            self.results = 1
        else:
            self.methods = [int(i)for i in str(methods)]
            self.results = len(self.methods)
        
    
    def func(self):
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