class Solution(object):
    def numJewelsInStones(self, jewels, stones):
       
        count=0
        for i in jewels:
            count+=stones.count(i)
        return count

        
