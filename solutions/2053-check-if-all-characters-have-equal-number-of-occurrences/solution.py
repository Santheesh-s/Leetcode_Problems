class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=set(list(s))
        ls=[s.count(i) for i in st]
        for i in ls:
            if i!=ls[0]:
                return False
        return True
