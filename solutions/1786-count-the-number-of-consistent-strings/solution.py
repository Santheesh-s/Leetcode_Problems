class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count=0
        allow=set(allowed)
        for i in words:
            if set(i).issubset(allow):
                count+=1
        return count
