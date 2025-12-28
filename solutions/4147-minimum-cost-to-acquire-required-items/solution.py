class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        cost=(need1*cost1)+(need2*cost2)
        over=min(need1,need2)
        cost_over=(over*costBoth)+(max(0,need1-over)*cost1)+(max(0,need2-over)*cost2)

        cost_combo=max(need1,need2)*costBoth

        return min(cost,cost_over,cost_combo)
