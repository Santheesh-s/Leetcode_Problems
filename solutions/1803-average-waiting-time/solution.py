class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        ls=[]
        tot=0
        for i in customers:
            if tot>i[0]:
                ls.append(tot-i[0]+i[1])
                tot+=i[1]
            else:
                tot=i[0]
                tot+=i[1]
                ls.append(i[1])
        return float(sum(ls))/len(ls)
