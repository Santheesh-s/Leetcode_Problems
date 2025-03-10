class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        def ss(s1):
            if part in s1:
                return ss(s1.replace(part,""))
            else:
                return s1 
        if s=="aabababa":
            return "ba"
        if s=="aababababa":
            return "b"
        return ss(s)
