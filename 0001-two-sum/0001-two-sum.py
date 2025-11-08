class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i # 2,0 7,1  11,2

        for i in range(len(nums)):
            if map.get(target-nums[i]) != None:
                element = map.get(target-nums[i])
                if element == i:
                    continue
                return [i, element]
                