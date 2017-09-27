#
# message_history.py
#
# statbot - Store Discord records for later analysis
# Copyright (c) 2017 Ammon Smith
#
# statbot is available free of charge under the terms of the MIT
# License. You are free to redistribute and/or modify it under those
# terms. It is distributed in the hopes that it will be useful, but
# WITHOUT ANY WARRANTY. See the LICENSE file for more details.
#

from .range import MultiRange

__all__ = [
    'MessageHistory',
]

class MessageHistory(MultiRange):
    __slots__ = (
        'first',
    )

    def __init__(self, *ranges, first=None):
        super().__init__(*ranges)
        self.first = first

    def find_first_hole(self, start):
        ''' Finds the first hole in the MultiRange starting from the given point '''

        current = start
        for range in reversed(self.ranges):
            if start > range.max():
                break
            current = range.min()

        if self.first is None or self.first < current:
            return min(start, current)
        else:
            return None

    def to_ranges(self):
        ''' Converts this object into two lists for insertion into the database '''

        starts = []
        ends = []

        for range in self.ranges:
            starts.append(range.start)
            ends.append(range.end)
        return starts, ends

    def __repr__(self):
        leng = len(self.ranges)
        if leng > 4:
            return f"<MessageHistory object: {self.first}, {leng} chunks>"
        elif leng == 0:
            return f"<MessageHistory object: {self.first}, []>"
        else:
            return f"<MessageHistory object: {self.first}, {self}>"
