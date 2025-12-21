class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=''.join(list(map(str,digits)))
        s=int(s)+1
        s=str(s)
        s=list(map(int,s))
        return s
