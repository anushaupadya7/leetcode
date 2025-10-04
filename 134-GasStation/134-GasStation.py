# Last updated: 05/10/2025, 01:36:45
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas=sum(gas)
        total_cost=sum(cost)
        fuel=0
        start=0

        if total_gas<total_cost:
            return -1

        for i in range(len(gas)):
            fuel+=gas[i]-cost[i]

            if fuel<0:
                start = i + 1
                fuel = 0

        return start