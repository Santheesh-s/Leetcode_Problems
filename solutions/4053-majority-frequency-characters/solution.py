class Solution(object):
    def majorityFrequencyGroup(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        for i in s:
            if(i not in d):
                d[i]=1
            else:
                d[i]+=1
        a=sorted(d.values())[::-1]
        m=0
        l=0
        for i in a:
            if l<a.count(i):
                m=i
                l=a.count(i)
        res=""
        for i,j in d.items():
            if j==m:
                res+=i
        return res
