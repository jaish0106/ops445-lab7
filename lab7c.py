#!/usr/bin/env python3
#Author: ajjayaratnam
from lab7b import *

def time_to_sec(time):
    """Convert a time object to seconds since midnight."""
    return time.hour * 3600 + time.minute * 60 + time.second

def sec_to_time(seconds):
    """Convert seconds since midnight to a Time object."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    """Add two Time objects using seconds calculation."""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)
