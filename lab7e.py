#!/usr/bin/env python3
#Author :ajjayaratnam
from lab7d import Time

class Time(Time):
    def __str__(self):
        """Return string representation for printing."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return interactive representation with dots."""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'
