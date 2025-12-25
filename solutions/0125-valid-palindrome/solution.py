class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ls=[lower(i) for i in s if i.isalnum()]
        return ls==ls[::-1]
