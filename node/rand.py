#!/usr/bin/env python

import datetime
import random

import ephem

from nodes import Node


class Random(Node):
    char = "H"
    args = 1
    results = 1
    
    def random_choice(self, inp:Node.indexable):
        """Choose one in a list randomly"""
        return [random.choice(inp)]
        
    def randint(self, inp:int):
        """Random number between 0 and inp inclusive"""
        return random.randint(0,inp)

    def get_next_new_moon(self, time: Node.clock):
        """Gets the date of the next new moon"""
        new_time = datetime.datetime(*time.time_obj[:7])

        return ephem.next_new_moon(new_time)
