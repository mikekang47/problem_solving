class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = set(nums)
        m = 0
        v = 0
        for i in s:
            cnt = nums.count(i)
            if m < cnt:
                m = cnt
                v = i
        return v

