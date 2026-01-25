class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        res=0
        one=k
        for i in range(50,-1,-1):
            if one<=0:
                break;
            count=math.comb(i,one)
            if count<n:
                res|=(1<<i)
                n-=count
                one-=1
        return res
