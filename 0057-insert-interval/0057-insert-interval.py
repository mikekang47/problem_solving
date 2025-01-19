import bisect
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = bisect.bisect(intervals, newInterval)        
        intervals.insert(res, newInterval)
        i = 0
        while i+1 < len(intervals):
            if self.canMerge(intervals[i], intervals[i+1]):
                intervals[i] = self.merge(intervals[i], intervals[i+1])
                intervals.remove(intervals[i+1])
            else:
                i += 1
        return intervals

    def canMerge(self, l1: List[int], l2: List[int]) -> bool:
        return l2[0] <= l1[1]
    
    def merge(self, l1: List[int], l2: List[int]) -> List[int]:
        if l2[1] < l1[1]:
            return [l1[0], l1[1]]
        else:
            return [l1[0], l2[1]]
        