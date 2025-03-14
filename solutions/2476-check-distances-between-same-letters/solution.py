class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        if len(s):
            a=set(list(s))
            for i in a:
                if not distance[ord(i)-97]==abs(s.find(i)-s.rfind(i))-1:
                    return False
        return True
