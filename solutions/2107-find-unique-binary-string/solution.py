class Solution(object):
    def findDifferentBinaryString(self, nums):
        if len(nums[0])==1 and nums[0]=='1':
            return '0'
        elif len(nums[0])==1 and nums[0]=='0':    
            return "1"
        ls=[int(i,2) for i in nums]
        c=len(nums[0])
        a=2**c-1
        for i in range(a):
            if i not in ls:
                return (bin(i)[2:]).zfill(c)
