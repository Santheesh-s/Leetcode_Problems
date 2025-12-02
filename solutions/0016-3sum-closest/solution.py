class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        bestsum = nums[0] + nums[1] + nums[2]
        bestdiff = abs(bestsum - target)
        nums=sorted(nums)
        n=len(nums)
        for i in range(n-2):
            left=i+1
            right=n-1
            while(left<right):
                s=nums[i]+nums[left]+nums[right]
                diff = abs(s - target)
                if diff < bestdiff:
                    bestdiff = diff
                    bestsum = s
                if s==target:
                    return s
                elif s>target:
                    right-=1
                else:
                    left+=1
        return bestsum
                        
