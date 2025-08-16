class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<=1:
            return nums
        ls=[]
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d=sorted(d.items(),key=lambda x: x[0])
        for i in range(1,len(d)-1):
            if d[i][1]==1 and d[i-1][0]!=d[i][0]-1 and d[i][0]+1!=d[i+1][0]:
                ls.append(d[i][0])
        if d[0][1]==1 and d[0][0]+1!=d[1][0]:
            ls.append(d[0][0])
        if d[-1][1]==1 and d[-1][0]-1!=d[-2][0]:
            ls.append(d[-1][0])
        return ls
