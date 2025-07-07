class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        l=[]
        k=0
        for i in str(n)[::-1]:
            if k==3:
                l.append('.')
                l.append(i)
                k=1
            else:
                l.append(i)
                k+=1
        return ''.join(l[::-1])
