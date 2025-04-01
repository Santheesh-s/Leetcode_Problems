class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s1=s1.split()
        s2=s2.split()
        l1=set([i for i in s1 if s1.count(i)==1 and i not in s2])
        l2=set([i for i in s2 if s2.count(i)==1 and i not in s1])
        return list(l1.symmetric_difference(l2))
