class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n=len(nums)
        nums=sorted(nums)
        ls=set()
        for i in range(n-3):
            for j in range(i+1,n-2):
                left=j+1
                right=n-1
                while(left<right):
                    s=nums[left]+nums[right]+nums[i]+nums[j]
                    if(s==target):
                        ls.add((nums[i],nums[j],nums[left],nums[right]))
                        left += 1
                        right -= 1
                    elif(s>target):
                        right-=1
                    else:
                        left+=1
        return [list(i) for i in ls]
