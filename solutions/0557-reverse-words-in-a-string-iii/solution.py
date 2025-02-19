class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls=s.split()
        for i in range(0,len(ls)):
            ls[i]=ls[i][::-1]
        return " ".join(ls)
