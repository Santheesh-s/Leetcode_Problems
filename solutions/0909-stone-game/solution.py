class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        piles=sorted(piles)[::-1]
        odd,even=0,0
        for i in range(len(piles)-1):
            odd+=piles[i]
            even+=piles[i+1]
        return odd>even

