class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        n=text.count(' ')
        text=text.split()
        m=len(text)
        if m==1:
            q=0
            r=n
        else:
            q=n/(m-1)
            r=n%(m-1)
        return (" "*q).join(text)+" "*r
