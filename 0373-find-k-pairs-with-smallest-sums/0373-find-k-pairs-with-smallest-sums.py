import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # 결과를 저장할 리스트
        result = []
        
        # 예외 처리: 빈 배열이 있거나 k가 0이면 빈 리스트 반환
        if not nums1 or not nums2 or k == 0:
            return result

        # 최소 힙 생성, (합, nums1의 인덱스, nums2의 인덱스) 형태로 삽입
        heap = []
        for i in range(min(len(nums1), k)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        # 힙에서 최소 원소를 k번 뽑아 결과에 추가
        while heap and len(result) < k:
            total, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])

            # 다음 원소 쌍을 힙에 추가, nums2에서 다음 원소와 쌍을 만듦
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result

        