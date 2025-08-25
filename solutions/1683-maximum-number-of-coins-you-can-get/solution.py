class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles=sorted(piles)[::-1]
        sum1=0
        for i in range(1,len(piles)-len(piles)/3,2):
            sum1+=piles[i]
        return sum1
