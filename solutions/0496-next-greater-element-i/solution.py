class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m=max(nums2)
        for i,j in enumerate(nums1):
            if j==m:
                nums1[i]=-1
            else:
                for k in range(nums2.index(j),len(nums2)):
                    if nums2[k]>j:
                        nums1[i]=nums2[k]
                        break;
                else:
                    nums1[i]=-1
        return nums1;
                
