#!/usr/bin/env python3
#Author: ajjayaratnam
from lab7a import *

def change_time(time, seconds):
    """Modify the time object based on seconds."""
    time.second += seconds
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    while time.second < 0:
        time.second += 60
        time.minute -= 1
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1
    return None
