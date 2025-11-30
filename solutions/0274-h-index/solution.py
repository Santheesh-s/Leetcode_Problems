class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations=sorted(citations,reverse=True)
        res=1;
        for i in range(len(citations)):
            if(citations[i]<res):
                return res-1;
            res+=1;
        return res-1;
