class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        ls=sorted(list(set(nums1)&set(nums2)))
        if len(ls):
            return ls[0]
        else:
            a=int(str(min(nums1))+str(min(nums2)))
            b=int(str(min(nums2))+str(min(nums1)))
            return a if a<b else b
