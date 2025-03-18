class Solution(object):
    def sortEvenOdd(self, nums):
        ls=[]
        l1=sorted([nums[i] for i in range(0,len(nums),2)])
        l2=sorted([nums[i] for i in range(1,len(nums),2)],reverse=True)
        for i,j in zip(l1,l2):
            ls.extend([i,j])
        if len(l1)>len(l2):
            ls.append(l1[-1])
        return ls
