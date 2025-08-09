class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        ls=[]
        tot=0
        for i in bank:
            m=i.count('1')
            if m!=0:
                ls+=[m]
        for i in range(len(ls)-1):
            tot+=ls[i]*ls[i+1]
        return tot
