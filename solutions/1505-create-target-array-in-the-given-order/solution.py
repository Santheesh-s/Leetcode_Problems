class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        ls=[]
        j=0
        for i in index:
            ls.insert(i,nums[j])
            j+=1
        return ls
