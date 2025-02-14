class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        ls=[]
        for i in sentences:
            ls.append(len(i.split(" ")))
        return max(ls)
