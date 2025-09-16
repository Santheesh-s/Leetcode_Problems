class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        ls=set()
        n=len(nums)
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            if d[i]>n/3:
                ls.add(i)
        return list(ls)
