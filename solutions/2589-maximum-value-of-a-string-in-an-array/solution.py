class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        ls=[]
        for i in strs:
            if not i.isdigit():
                ls.append(len(i))
            else:
                ls.append(int(i))
        return max(ls)
        
