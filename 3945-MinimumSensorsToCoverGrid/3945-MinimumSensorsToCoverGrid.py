# Last updated: 9/18/2025, 11:53:47 PM
class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        no_of_steps=2*k+1
        return math.ceil(n/no_of_steps)*math.ceil(m/no_of_steps)