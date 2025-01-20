class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda k: sqrt(k[0]*k[0] + k[1]*k[1]))
        return points[:k]