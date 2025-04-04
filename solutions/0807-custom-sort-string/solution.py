class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        ls=""
        for i in order:
            if i in s:
                ls+=i*s.count(i)
                s=s.replace(i,"")
        return ls+s
