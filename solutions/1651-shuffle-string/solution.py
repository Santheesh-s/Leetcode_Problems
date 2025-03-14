class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        n=len(indices)
        f=["."]*n
        for i in range(0,n):
            f[indices[i]]=s[i]
        return "".join(f)
