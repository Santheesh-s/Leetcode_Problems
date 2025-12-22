class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        d={}
        for i in range(len(names)):
            d[heights[i]]=names[i]
        d=sorted(d.items(),reverse=True)
        return [name for height, name in d]
