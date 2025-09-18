# Last updated: 19/09/2025, 00:16:40
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)  
        
        return [list(set1 - set2), list(set2 - set1)]
        