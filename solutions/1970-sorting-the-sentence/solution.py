class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls=s.split()
        ls=sorted(ls,key=lambda x:x[-1])
        s=[i[:-1 ]for i in ls]
        return " ".join(s)

