from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        print(len(intervals), intervals)
        if not intervals or len(intervals) < 1 or len(intervals) > 105 or not all([len(item) == 2 and all([type(value) == int and value >= -5 * 104 and value <= 5 * 104 for value in item]) and item for item in intervals]):
            raise ValueError()
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
