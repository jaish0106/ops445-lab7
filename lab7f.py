#!/usr/bin/env python3
#Author : ajjayaratnam
from lab7e import Time

class Time(Time):
    def __add__(self, t2):
        """Overload the + operator to sum Time objects."""
        # Sum the times and return the formatted string
        result_time = self.sum_times(t2)
        return result_time.format_time()

