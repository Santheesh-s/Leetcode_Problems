class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c,d=0,0
        a=set(nums1)
        b=set(nums2)
        for i in nums1:
            if i in b:
                c+=1
        for j in nums2:
            if j in a:
                d+=1
        return [c,d]
