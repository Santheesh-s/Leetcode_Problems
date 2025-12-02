class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        n=len(nums)
        ls=[]
        for i in range(n-2):
            if(i>0 and nums[i]==nums[i-1]): continue
            left=i+1
            right=n-1
            while(left<right):
                s=nums[left]+nums[right]+nums[i]
                if(s==0):
                    ls.append([nums[left],nums[right],nums[i]])
                    left_val = nums[left]
                    right_val = nums[right]
                    while left < right and nums[left] == left_val:
                        left += 1
                    while left < right and nums[right] == right_val:
                        right -= 1
                elif s>0:
                    right-=1
                else:
                    left+=1
        return ls
