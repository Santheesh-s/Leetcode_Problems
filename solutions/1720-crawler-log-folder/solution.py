class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        c=0
        for i in logs:
            if i=="../":
                c-=1
                c=0 if c<0 else c
            elif i=="./":
                c=c
            else:
                c+=1
        return c
