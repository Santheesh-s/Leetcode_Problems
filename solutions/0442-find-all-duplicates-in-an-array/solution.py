class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ls={}
        ls1=[]
        for i in nums:
            if i in ls:
                ls[i]+=1
            else:
                ls[i]=1
            if ls[i]==2:
                ls1.append(i)
        return ls1
