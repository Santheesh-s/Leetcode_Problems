class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        d={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=cost[i]
            else:
                d[s[i]]=cost[i]
        d=sorted(d.values())
        return sum(d[:-1])
