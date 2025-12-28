class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        def solve(S):
            @lru_cache(None)
            def f(i,d,lim,st,odd):
                if i==len(S):
                    return 1 if st and d==0 else 0
                res,top=0,(int(S[i]) if lim else 9)
                for x in range(top+1):
                    res+=f(i+1,d+(x if odd else -x) if st or x>0 else 0,lim and x==top ,st or x>0,not odd if st or x>0 else True)
                return res
            return f(0,0,True,False,True)
        return solve(str(high))-solve(str(low-1))
            
