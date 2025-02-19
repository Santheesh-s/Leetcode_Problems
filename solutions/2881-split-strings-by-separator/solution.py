class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        l1=separator.join(words)
        return [item for item in l1.split(separator) if item]
