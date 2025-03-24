class Solution(object):
    def numberOfMatches(self, n):
        ls=[]
        while(n//2>=1):
            ls.append(n//2)
            n-=n//2
        return sum(ls)
