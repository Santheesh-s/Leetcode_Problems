class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        n=len(pref)
        ls=[pref[0]]*n
        for i in range(1,n):
            ls[i]=pref[i]^pref[i-1]
        return ls
        


