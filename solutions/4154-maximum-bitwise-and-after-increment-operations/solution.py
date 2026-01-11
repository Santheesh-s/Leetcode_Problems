class Solution(object):
    def maximumAND(self, nums, k, m):
        """
        :type nums: List[int]
        :type k: int
        :type m: int
        :rtype: int
        """
        ans=0
        for b in range(30,-1,-1):
            target=ans|(1<<b)
            cost=[]
            for x in nums:
                v=target
                for i in range(30,-1,-1):
                    if not (target&(1<<i)):
                        if v|((1<<i)-1) <x:
                            v|=(1<<i)
                cost.append(v-x)
            cost.sort()
            if sum(cost[:m])<=k:
                ans=target
        return ans
                
