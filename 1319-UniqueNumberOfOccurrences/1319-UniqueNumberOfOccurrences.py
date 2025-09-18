# Last updated: 19/09/2025, 00:16:41
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr) 
        occurrences = set(freq.values()) 
        return len(freq) == len(occurrences)  
