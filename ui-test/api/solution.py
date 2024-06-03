from typing import List

class Solution:
    @staticmethod
    def eraseOverlapIntervals(string: str) -> int:
        if not string or len(string) == 0:
            raise ValueError("empty string")
        available_values = '-1234567890,;'
        for i in string:
            if i not in available_values:
                raise ValueError("only digits , and ; are allowed")
        data = string.strip().split(";")
        intervals: List[List[int]] = []
        for k in data[0:]:
            values = k.strip().split(",")
            temp_array = [int(val) for val in values]
            intervals.append(temp_array)
        if not intervals or len(intervals) < 1:
            raise ValueError("intervals is empty")
        if len(intervals) > 105:
            raise ValueError("there must be less than 105 intervals")
        for interval in intervals:
            if len(interval) != 2:
                raise ValueError("every interval must have exactly two elements")
            if interval[0] > interval[1]:
                raise ValueError("second value in interval must be bigger than first value")
            if interval[0] <= -5 * 104 or interval[1] <= -5 * 104 or interval[0] >= 5 * 104 or interval[1] >= 5 * 104:
                raise ValueError("values must be between -5 * 104 and -5 * 104")
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res