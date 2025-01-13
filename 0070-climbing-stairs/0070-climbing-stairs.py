class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0] * 48
        arr[1]= 1
        arr[2] = 2
        for i in range(3, 46):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n]