# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            result = isBadVersion(mid)
            if not result:
                left = mid + 1
            else:
                answer = mid
                right = mid - 1
        return answer
        