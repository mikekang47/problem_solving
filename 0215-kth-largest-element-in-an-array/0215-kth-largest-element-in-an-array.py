import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [0] * 20002
        for i in nums:
            arr[i+10000] += 1
        
        cnt = k
        for i in range(len(arr)-1, 0, -1):
            if arr[i] != 0:
                if cnt == 1:
                    return i-10000
                else:
                    cnt -= arr[i]
                    if cnt <= 0:
                        return i - 10000
        return 0

