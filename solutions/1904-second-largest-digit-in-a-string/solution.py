class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls=sorted(list(set([int(i) for i in s if i.isdigit()])))
        if len(ls)<=1:
            return -1
        return ls[-2]
