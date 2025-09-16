class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        n=len(nums);
        ls=[]
        for i in range(0,n-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue;
            left=i+1
            right=n-1;
            while(left<right):
                sum=nums[left]+nums[right]+nums[i];
                if(sum==0):
                    ls.append((nums[left],nums[right],nums[i]));
                    left+=1;
                    right-=1;
                elif(sum>0):
                    right-=1
                else:
                    left+=1
        return [list(t) for t in set(ls)]
