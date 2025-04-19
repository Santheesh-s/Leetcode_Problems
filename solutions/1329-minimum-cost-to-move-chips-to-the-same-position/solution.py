class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        e=0
        o=0
        for i in position:
            if(i&1)==1:
                o+=1;
            else:
                e+=1;
        return o if o<e else e
