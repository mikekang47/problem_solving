class Solution:
   def twoSum(self, nums, target: int):
        dic = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in dic:
                return [dic[temp], i]
            dic[nums[i]] = i
        return []
        