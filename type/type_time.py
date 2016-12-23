#!/usr/bin/env python

import time

from dateutil.relativedelta import relativedelta


def time_eval(string):
    return TypeTime.parse_strtime(string)


class TypeTime(object):
    formats = ["%c",
               "%H:%M",
               "%H:%M:%S",
               "%d/%m/%Y",
               "%d/%m/%y",
               "%d/%m/%Y %H:%M:%S",
               "%d/%m/%y %H:%M:%S",
               "%d/%m/%Y %H:%M",
               "%d/%m/%y %H:%M",
               "%H:%M:%S %d/%m/%Y",
               "%H:%M:%S %d/%m/%y",
               "%H:%M %d/%m/%Y",
               "%H:%M %d/%m/%y",
               "%Y/%m/%d",]
    values = ("year", "mon", "mday", "hour", "min", "sec")
    undefined = ("%y", "%m", "%d", "%H", "%M", "%S")
    
    def __init__(self, time_obj):
        self.time_obj = time_obj
        self.defined_values = [True]*6
    
    def __eq__(self, obj):
        return self.time_obj == obj

    def __getattribute__(self, item):
        conversion = {"month": "mon", "day": "mday", "minute": "min", "second": "sec"}
        item = conversion.get(item, item)
        if item in TypeTime.values:
            if self.defined_values[TypeTime.values.index(item)]:
                return getattr(self.time_obj, "tm_"+item)
            return None
        else:
            return super(TypeTime, self).__getattribute__(item)
        
    def __str__(self):
        try:
            return time.strftime(self.get_display_format(), self.time_obj)
        except ValueError:
            return "time({})".format(str(list(zip(self.values, self.time_obj)))[1:-1])

    def __add__(self, other: "TypeTime"):
        return TypeTime.parse_time_delta(self.get_rel_delta() + other.get_rel_delta(), extra_months=2)

    def __sub__(self, other: "TypeTime"):
        return TypeTime.parse_time_delta(self.get_rel_delta() - other.get_rel_delta(), extra_months=2)

    def __mul__(self, other):
        return TypeTime.parse_time_delta(self.get_rel_delta() * other, extra_months=other)

    __rmul__ = __mul__

    def divide_int(self, other):
        return TypeTime.parse_time_delta(
            relativedelta(years=self.time_obj.tm_year  * self.defined_values[0] / other,
                          months=self.time_obj.tm_mon  * self.defined_values[1] / other,
                          days=self.time_obj.tm_mday   * self.defined_values[2] / other,
                          hours=self.time_obj.tm_hour  * self.defined_values[3] / other,
                          minutes=self.time_obj.tm_min * self.defined_values[4] / other,
                          seconds=self.time_obj.tm_sec * self.defined_values[5] / other).normalized())

    def floordiv_int(self, other):
        return TypeTime.parse_time_delta(self.get_rel_delta() / other)

    def divide_time(self, other):
        return self.get_seconds() / other.get_seconds()

    def floordiv_time(self, other):
        return self.get_seconds() // other.get_seconds()

    def get_seconds(self):
        assert self.defined_values[0] is False, "Can't divide years"
        assert self.defined_values[1] is False, "Can't divide months"
        days = self.defined_values[2] and self.time_obj.tm_mday
        hours = self.defined_values[3] and self.time_obj.tm_hour
        minutes = self.defined_values[4] and self.time_obj.tm_min
        seconds = self.defined_values[5] and self.time_obj.tm_sec
        return ((days*24+hours)*60+minutes)*60+seconds

    def get_display_format(self):
        formats = [TypeTime.get_defined(format) for format in TypeTime.formats[1:]]
        filtered = []
        for i, format in enumerate(formats):
            allowed = []
            for uses_type, is_defined in zip(format, self.defined_values):
                allowed.append(uses_type or not is_defined)
            if all(allowed):
                filtered.append(TypeTime.formats[i+1])
        return min(filtered, key=len)

    def get_rel_delta(self):
        return relativedelta(years=self.time_obj.tm_year  * self.defined_values[0],
                             months=self.time_obj.tm_mon  * self.defined_values[1] - 1,
                             days=self.time_obj.tm_mday   * self.defined_values[2],
                             hours=self.time_obj.tm_hour  * self.defined_values[3],
                             minutes=self.time_obj.tm_min * self.defined_values[4],
                             seconds=self.time_obj.tm_sec * self.defined_values[5]).normalized()

    @staticmethod
    def get_defined(format):
        rtn = [time_type in format for time_type in TypeTime.undefined]
        rtn[0] |= "%Y" in format
        return rtn

    @staticmethod
    def parse_strtime(string):
        if not string:
            return
        for in_form in TypeTime.formats:
            try:
                time_obj = time.strptime(string, in_form)
            except ValueError:
                pass
            else:
                new = TypeTime(time_obj)
                if in_form != "%c":
                    new.defined_values = TypeTime.get_defined(in_form)
                return new
        try:
            nums = []
            formats = []
            while string:
                cur_num = ""
                while string[0].isdigit():
                    cur_num += string[0]
                    string = string[1:]
                format = string[0]
                formats.append("%"+format)
                nums.append(cur_num)
                string = string[1:]
            formats = "-".join(formats)
            nums = "-".join(nums)
            new = TypeTime(time.strptime(nums, formats))
            new.defined_values = TypeTime.get_defined(formats)
            return new
        except:
            return None
            
    @staticmethod
    def parse_struct_time(lst):
        lst = list(map(int, lst))
        bad_year = False
        if lst[0] == 0:
            lst[0] = 1
            bad_year = True
        try:
            struct_time = time.struct_time(lst)
        except TypeError:
            struct_time = time.struct_time(lst+[0, 0, 0])
        new = TypeTime(struct_time)
        new.defined_values = [element != 0 for element in struct_time[:-3]]
        if bad_year:
            new.defined_values[0] = False
        return new

    @staticmethod
    def parse_time_delta(delta, extra_months=1):
        rtn = TypeTime.parse_struct_time([delta.years,
                                          delta.months + extra_months,
                                          delta.days,
                                          delta.hours,
                                          delta.minutes,
                                          delta.seconds])
        return rtn

TypeTime.default_time = TypeTime.parse_strtime("01/01/1990 00:00:00")
