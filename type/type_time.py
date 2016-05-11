#!/usr/bin/env python

import datetime, time

def time_eval(string):
    return TypeTime.parse_strtime(string)

class TypeTime(object):
    formats = ["%c",
               "%H:%M",
               "%H:%M:%S",
               "%d/%m/%y",
               "%d/%m/%Y",
               "%d/%m/%y %H:%M:%S",
               "%d/%m/%Y %H:%M:%S",
               "%d/%m/%y %H:%M",
               "%d/%m/%Y %H:%M",
               "%H:%M:%S %d/%m/%y",
               "%H:%M:%S %d/%m/%Y",
               "%H:%M %d/%m/%y",
               "%H:%M %d/%m/%Y"]    
    values = ("year", "month", "day", "hour", "min", "sec")
    
    def __init__(self, time_obj):
        self.time_obj = time_obj
        self.year = self.time_obj.tm_year
        self.month = self.time_obj.tm_mon
        self.day = self.time_obj.tm_mday
        self.hour = self.time_obj.tm_hour
        self.min = self.time_obj.tm_min
        self.sec = self.time_obj.tm_sec
        
    def __setattr__(self, attr, val):
        super(TypeTime, self).__setattr__(attr, val)
        if attr not in TypeTime.values:
            return
        new_lst = []
        for i in self.time_obj:
            new_lst.append(i)
        new_lst[TypeTime.values.index(attr)] = val
        self.time_obj = time.struct_time(new_lst)
        #print(self.time_obj)
        try:
            if {self.sec, self.min, self.hour} == {None}:            
                self.datetime_obj = 0
            elif {self.day, self.month, self.year} == {None}:            
                self.datetime_obj = 0
            elif None in [self.sec, self.min, self.hour, self.day, self.month, self.year]:
                pass#print("BAD")
            else:
                pass#print(time.mktime(self.time_obj))
        except AttributeError:
            pass
    
    def __eq__(self, obj):
        return self.time_obj == obj
        
    def __str__(self):
        return time.strftime("%c", self.time_obj)
    
    def __add__(self, other_time):
        #print(self)
        #print(other_time)
        dt_1 = datetime.datetime(*self.time_obj[:5]+(min(self.time_obj[5], 59),))
        dt_2 = time.mktime(other_time.time_obj)
        return dt_1+dt_2
    
    @staticmethod
    def parse_strtime(string):
        for in_form in TypeTime.formats:
            try:
                time_obj = time.strptime(string, in_form)
            except ValueError:pass
            else:
                new = TypeTime(time_obj)
                if in_form != "%c":
                    if "%S" not in in_form: new.sec = None
                    if "%M" not in in_form: new.min = None
                    if "%H" not in in_form: new.hour = None
                    if "%d" not in in_form: new.day = None
                    if "%m" not in in_form: new.month = None
                    if "%y" not in in_form: new.year = None
                return new
            
    @staticmethod
    def parse_struct_time(lst):
        return TypeTime(time.struct_time(lst))
            
TypeTime.default_time = TypeTime.parse_strtime("01/01/1990 00:00:00")