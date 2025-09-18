# Last updated: 19/09/2025, 00:16:52
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False

        count=Counter(hand)
        for card in sorted(count):
            if count[card]>0:
                need=count[card]
                for i in range(card,card+groupSize):
                    if count[i]<need:
                        return False
                    count[i]-=need

        return True

        