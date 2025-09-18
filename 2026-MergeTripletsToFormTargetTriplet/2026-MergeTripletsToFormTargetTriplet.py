# Last updated: 19/09/2025, 00:16:29
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found_x = found_y = found_z = False
        a, b, c = target

        for x, y, z in triplets:
            if x > a or y > b or z > c:
                continue

            if x == a:
                found_x = True
            if y == b:
                found_y = True
            if z == c:
                found_z = True

        return found_x and found_y and found_z
