class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """

        a=int("".join(map(str,num)));
        return map(int,list(str(a+k)))

