class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        a=""
        for i in number:
            if i in '0123456789':
                a+=i
        i=0
        res=[]
        n=len(a)
        while i<n:
            if i+4==n:
                res.append(a[i:i+2])
                i+=2
            elif i+3<=n:
                res.append(a[i:i+3])
                i+=3
            else:
                res.append(a[i:i+2])
                i+=2
        if len(res)>1:
            return '-'.join(res)
        return res[0]

