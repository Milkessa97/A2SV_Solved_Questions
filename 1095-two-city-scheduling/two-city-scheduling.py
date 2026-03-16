class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0]-x[1])
        total_cost = 0
        turn = len(costs)/2
        for idx in range(len(costs)):
            if idx < turn:
                total_cost += costs[idx][0]
            else:
                total_cost += costs[idx][1]
        return total_cost