class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        """
        :type nums: List[int]
        :type queries: List[int]
        :type x: int
        :rtype: List[int]
        """
        ls=[]
        ls1=[]
        for i in range(len(nums)):
            if nums[i]==x:
                ls.append(i)
        n=len(ls)
        for i in range(len(queries)):
            if n<queries[i]:
                ls1.append(-1)
            else:
                ls1.append(ls[queries[i]-1])
        return ls1
