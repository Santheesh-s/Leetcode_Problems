class Solution(object):
    def countDistinctIntegers(self, nums):
        s=",".join(list(map(str,nums)))
        n=s.split(",")[::-1]
        for i in range(len(n)):
            n[i]=(n[i][::-1]).strip('0')
        n+=s.split(",")
        return len(set(n))
