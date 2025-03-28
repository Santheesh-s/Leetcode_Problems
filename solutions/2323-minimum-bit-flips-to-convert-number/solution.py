class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        start=bin(start)[2:]
        goal=bin(goal)[2:]
        max_len = max(len(start), len(goal))
        start = start.zfill(max_len)
        goal = goal.zfill(max_len)
        ls=0
        for i,j in zip(start,goal):
            if i!=j:
                ls+=1
        return ls

