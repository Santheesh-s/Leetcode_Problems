class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        l=set(nums1)& set(nums2)
        m=set(nums2)& set(nums3)
        n=set(nums1)&set(nums3)
        return list(l|m|n)
