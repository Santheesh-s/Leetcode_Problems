class Solution(object):
    def getSneakyNumbers(self, nums):
        ls=[]
        for i in set(nums):
            if nums.count(i)==2:
                ls.append(i)
        return ls
